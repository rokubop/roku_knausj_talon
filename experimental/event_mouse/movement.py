from talon import ctrl, cron, settings
from typing import Literal
from .typings import Profile, MovementBase
import math
import time
import platform
os = platform.system().lower()

if os.startswith("windows"):
    import win32api, win32con

xy_dir = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

class MovementDefault(MovementBase):
    def __init__(self, event_bus, profile):
        self.event_bus = event_bus
        self.mouse_move_job = None
        self.current_dx = 0
        self.current_dy = 0
        self._callbacks = set()

        # new
        self.profile: Profile = profile

        self.x_dir = None
        self.y_dir = None
        self.move_job = None
        self.move_start_ts = None
        self.move_stop_soft_ts = None
        self.debounce_stop_duration = 0.170
        self.decay_start_ts = None
        self.peak_dx = None
        self.peak_dy = None

        if os.startswith("windows"):
            self._mouse_move = self._mouse_move_windows
        else:
            self._mouse_move = self._mouse_move_generic

    def update_profile(self, new_profile):
        self.profile = new_profile

    def _mouse_move_generic(self, dx: int, dy: int):
        (x, y) = ctrl.mouse_pos()
        ctrl.mouse_move(x + dx, y + dy)

    def _mouse_move_windows(self, dx: int, dy: int):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

    # new code start

    def move_start_new(self, direction: Literal["up", "down", "left", "right"]):
        """Start moving until stop is called"""
        (new_x_dir, new_y_dir) = xy_dir[direction]
        self.move_stop_soft_ts = None

        if self.move_job:
            if new_x_dir != self.x_dir or new_y_dir != self.y_dir:
                self.x_dir = new_x_dir
                self.y_dir = new_y_dir
                self.move_start_ts = time.perf_counter()
            # move_job already exists
            return

        self.x_dir = new_x_dir
        self.y_dir = new_y_dir
        self.move_start_ts = time.perf_counter()
        self._move_tick()
        ms = f"{settings.get('user.event_mouse_refresh_interval_ms')}ms"
        self.move_job = cron.interval(ms, self._move_tick)

    def _decay_tick(self, ts: float):
        if not self.decay_start_ts:
            self.decay_start_ts = ts
            speed = (1 + min((ts - self.move_start_ts) / 0.5, 1.3))
            self.peak_dx = self.profile["base_speed"] * speed
            self.peak_dy = self.profile["base_speed"] * speed

        decay_elapsed = ts - self.decay_start_ts

        dx_decel = self.profile["deceleration_curve"](decay_elapsed)
        dx = self.peak_dx * dx_decel
        dy = self.peak_dy * dx_decel

        # decay_factor = decay_elapsed / (decay_elapsed + 1) ** 0.5

        # dx = self.peak_dx * (1 - decay_factor) ** 3
        # dy = self.peak_dy * (1 - decay_factor) ** 3

        if dx < 1 and dy < 1:
            self.move_stop_hard()
            return

        self._mouse_move(round(dx * self.x_dir), round(dy * self.y_dir))

    def _accel_tick(self, ts: float):
        self.decay_start_ts = None
        acceleration_speed = 1 + min((ts - self.move_start_ts) / 0.5, 1.3)

        dx = self.profile["base_speed"] * acceleration_speed * self.x_dir
        dy = self.profile["base_speed"] * acceleration_speed * self.y_dir
        self._mouse_move(round(dx), round(dy))

    def _move_tick(self):
        ts = time.perf_counter()

        if self.move_stop_soft_ts and ts - self.move_stop_soft_ts > self.debounce_stop_duration:
            self._decay_tick(ts)
        else:
            self._accel_tick(ts)

    def move_stop_soft(self):
        self.move_stop_soft_ts = time.perf_counter()

    def move_stop_hard(self):
        if self.move_job:
            cron.cancel(self.move_job)
            self.move_start_ts = None
            self.move_stop_soft_ts = None
            self.move_job = None
            self.peak_dx = None
            self.peak_dy = None
            self.decay_start_ts = None
            self.x_dir = None
            self.y_dir = None

    # new code stop

    def move_start(self, dx: int, dy: int, speed: int = 1, acceleration: int = 1, min_speed: int = 100, max_speed: int = 200, callback_stop: callable = None):
        """Start moving the mouse in a direction at a speed"""
        if callback_stop:
            self._callbacks.add(callback_stop)
        self.stop_transition()

        self.current_dx = dx
        self.current_dy = dy

        def update_position():
            self._mouse_move(self.current_dx, self.current_dy)

        update_position()
        ms = f"{settings.get('user.event_mouse_refresh_interval_ms')}ms"
        self.mouse_move_job = cron.interval(ms, update_position)

    def move_to_pos_relative(self, x: int, y: int, duration_ms: int = 700, callback_stop: callable = None, callback_tick: callable = None):
        """Move to a xy position relative to the cursor over a duration"""
        if callback_stop:
            self._callbacks.add(callback_stop)

        self._mouse_move_natural(x, y, duration_ms, callback_tick=callback_tick)

    def move_to_pos_relative_linear(self, x: int, y: int, duration_ms: int = 700, callback_stop: callable = None, callback_tick: callable = None):
        """Move to a xy position relative to the cursor over a duration"""
        if callback_stop:
            self._callbacks.add(callback_stop)
        self._mouse_move_linear(x, y, duration_ms, callback_tick=callback_tick)

    def _mouse_move_natural(self, x: int = None, y: int = None, duration_ms: int = 700, degrees_x: int = None, degrees_y: int = None, calibrate_x_override=0, calibrate_y_override=0, callback_tick=None):
        self.stop_transition()

        update_interval_ms = settings.get("user.event_mouse_refresh_interval_ms")
        steps = max(1, duration_ms // update_interval_ms)
        step_count = 0
        last_x, last_y = 0, 0
        accumulated_dx, accumulated_dy = 0.0, 0.0

        print("x_total", x)
        def update_position():
            nonlocal step_count, last_x, last_y, accumulated_dx, accumulated_dy

            step_count += 1
            if step_count > steps:
                self.stop_hard()
                return

            progress = step_count / steps
            eased_progress = math.sin(progress * math.pi / 2)

            current_x = x * eased_progress
            current_y = y * eased_progress

            dx_step = current_x - last_x
            dy_step = current_y - last_y

            accumulated_dx += dx_step - int(dx_step)
            accumulated_dy += dy_step - int(dy_step)

            if abs(accumulated_dx) >= 0.5:
                dx_step += int(math.copysign(1, accumulated_dx))
                accumulated_dx -= int(math.copysign(1, accumulated_dx))

            if abs(accumulated_dy) >= 0.5:
                dy_step += int(math.copysign(1, accumulated_dy))
                accumulated_dy -= int(math.copysign(1, accumulated_dy))

            # print("dx_step", dx_step, "dy_step", dy_step, "accumulated_dx", accumulated_dx, "accumulated_dy")

            self._mouse_move(int(dx_step), int(dy_step))
            last_x, last_y = current_x, current_y

            if callback_tick:
                callback_tick(last_x, last_y)

        update_position()
        ms = f"{settings.get('user.event_mouse_refresh_interval_ms')}ms"
        self.mouse_move_job = cron.interval(ms, update_position)

    def _mouse_move_linear(self, x: int, y: int, duration_ms: int = 700, callback_tick=None):
        self.stop_transition()

        update_interval_ms = 16
        steps = max(1, duration_ms // update_interval_ms)
        step_count = 0
        start_x, start_y = 0, 0
        expected_x, expected_y = start_x, start_y  # Initialize expected position to start position

        dx_total = x - start_x
        dy_total = y - start_y
        actual_x, actual_y = start_x, start_y  # Track the actual position after each move

        def update_position():
            nonlocal step_count, actual_x, actual_y, expected_x, expected_y

            step_count += 1
            if step_count > steps:
                self.stop_hard()
                return

            # Calculate the expected position at this step
            progress = step_count / steps
            expected_x = start_x + dx_total * progress
            expected_y = start_y + dy_total * progress
            print("expected_x", expected_x, "expected_y", expected_y, "actual_x", actual_x, "actual_y", actual_y, "dx_total", dx_total, "dy_total", dy_total, "progress", progress, "steps", steps)

            # Determine the next step based on the difference between the expected and actual positions
            dx_step = round(expected_x - actual_x)
            dy_step = round(expected_y - actual_y)

            # Move the mouse by the calculated step to correct any discrepancy
            self._mouse_move(dx_step, dy_step)

            # Update the actual position based on the movement made
            actual_x += dx_step
            actual_y += dy_step

            if callback_tick:
                callback_tick(actual_x, actual_y)

            # If this is the last step, ensure the mouse is exactly at the target position
            if step_count == steps:
                self.stop_hard()  # Ensure the function stops after completing the movement

        # Execute the first update immediately to start the movement
        update_position()

        # Schedule the rest of the updates
        ms = f"{settings.get('user.event_mouse_refresh_interval_ms')}ms"
        self.mouse_move_job = cron.interval(ms, update_position)

    def stop_hard(self):
        if self.mouse_move_job:
            cron.cancel(self.mouse_move_job)
            if self._callbacks:
                for callback in self._callbacks:
                    callback()
                self._callbacks.clear()

            self.mouse_move_job = None
            self.current_dx = 0
            self.current_dy = 0

    def stop_transition(self):
        if self.mouse_move_job:
            cron.cancel(self.mouse_move_job)
            self.mouse_move_job = None

    def stop_soft(self, duration_ms: int = 700, curve: str = "ease_out"):
        pass

    def is_moving(self):
        return self.mouse_move_job is not None or self.move_job is not None