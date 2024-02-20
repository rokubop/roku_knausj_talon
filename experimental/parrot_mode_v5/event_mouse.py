from talon import Module, actions, ctrl, settings, cron
from collections import defaultdict
from typing import Literal
import platform
import time
import math
os = platform.system().lower()

if os.startswith("windows"):
    import win32api, win32con

mod = Module()
mod.setting("event_mouse_scroll_speed", float, 1, "Setting for event mouse scroll speed")

class EventBus:
    def __init__(self):
        self.events = defaultdict(list)

    def register(self, event_name, callback):
        self.events[event_name].append(callback)

    def unregister(self, event_name, callback):
        if event_name in self.events:
            self.events[event_name] = list(filter(lambda c: c != callback, self.events[event_name]))

    def notify(self, event_name):
        for callback in self.events[event_name]:
            callback()

        method = getattr(actions.user, f"on_event_mouse_{event_name}", None)
        if method:
            method()


class Buttons:
    def __init__(self, event_bus):
        self.held_buttons = []
        self.event_bus = event_bus

    def click(self, button: int = 0):
        if self.held_buttons:
            self.drag_stop()
        else:
            self.event_bus.notify("button_down")
            ctrl.mouse_click(button=button, hold=16000)
            self.event_bus.notify("button_up")
            self.event_bus.notify("click")

    def drag(self, button: int = 0):
        if button not in self.held_buttons:
            self.held_buttons.append(button)
            self.event_bus.notify("button_down")
            self.event_bus.notify("drag_start")
            ctrl.mouse_click(button=button, down=True)

    def drag_stop(self):
        if self.held_buttons:
            for button in self.held_buttons:
                ctrl.mouse_click(button=button, up=True)
            self.held_buttons.clear()
            self.event_bus.notify("button_up")
            self.event_bus.notify("drag_stop")

class Scrolling:
    def __init__(self, event_bus):
        self.scroll_job = None
        self.scroll_dir = 1
        self.scroll_start_ts = None
        self.scroll_stop_soft_ts = None
        self.debounce_start_duration = 0.0
        self.debounce_stop_duration = 0.170
        self.event_bus = event_bus

    def scroll_start(self, direction: str):
        """Start scrolling until stop is called"""
        new_scroll_dir = -1 if direction == "up" else 1
        self.scroll_stop_soft_ts = None

        if self.scroll_job:
            if new_scroll_dir != self.scroll_dir:
                self.scroll_dir = new_scroll_dir
                self.scroll_start_ts = time.perf_counter()
            # scroll_job already exists
            return

        self.scroll_dir = new_scroll_dir
        self.scroll_start_ts = time.perf_counter()
        self.event_bus.notify("scroll_start")
        self.scroll_tick()
        self.scroll_job = cron.interval("16ms", self.scroll_tick)

    def scroll_tick(self):
        ts = time.perf_counter()
        if ts - self.scroll_start_ts < self.debounce_start_duration:
            return

        if self.scroll_stop_soft_ts and ts - self.scroll_stop_soft_ts > self.debounce_stop_duration:
            self.scroll_stop_hard()
            return

        acceleration_speed = 1 + min((ts - self.scroll_start_ts) / 0.5, 4)
        y = (
            settings.get("user.event_mouse_scroll_speed")
            * acceleration_speed
            * self.scroll_dir
        )
        actions.mouse_scroll(y, by_lines=True)

    def scroll_stop_soft(self):
        self.scroll_stop_soft_ts = time.perf_counter()

    def scroll_stop_hard(self):
        if self.scroll_job:
            cron.cancel(self.scroll_job)
            self.scroll_start_ts = None
            self.scroll_stop_soft_ts = None
            self.scroll_job = None
            self.event_bus.notify("scroll_stop")

    def is_scrolling(self):
        return self.scroll_job is not None

xy_dir = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

class Movement:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.mouse_move_job = None
        self.current_dx = 0
        self.current_dy = 0
        self._callbacks = set()

        # new
        self.x_dir = None
        self.y_dir = None
        self.move_job = None
        self.move_start_ts = None
        self.move_stop_soft_ts = None
        self.debounce_stop_duration = 0.170
        self.decay_start_ts = None
        self.peak_dx = None
        self.peak_dy = None
        self.power = 15

        if os.startswith("windows"):
            self._mouse_move = self._mouse_move_windows
        else:
            self._mouse_move = self._mouse_move_generic

    def _mouse_move_generic(self, dx: int, dy: int):
        (x, y) = ctrl.mouse_pos()
        ctrl.mouse_move(x + dx, y + dy)

    def _mouse_move_windows(self, dx: int, dy: int):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

    # new code start

    def move_start_new(self, direction: str):
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
        self.move_job = cron.interval("16ms", self._move_tick)

    def _decay_tick(self, ts: float):
        if not self.decay_start_ts:
            self.decay_start_ts = ts
            speed = (1 + min((ts - self.move_start_ts) / 0.5, 1.3))
            self.peak_dx = self.power * speed
            self.peak_dy = self.power * speed

        decay_elapsed = ts - self.decay_start_ts
        decay_factor = decay_elapsed / (decay_elapsed + 1) ** 0.5

        dx = self.peak_dx * (1 - decay_factor) ** 3
        dy = self.peak_dy * (1 - decay_factor) ** 3

        if dx < 1 and dy < 1:
            self.move_stop_hard()
            return

        self._mouse_move(round(dx * self.x_dir), round(dy * self.y_dir))

    def _accel_tick(self, ts: float):
        self.decay_start_ts = None
        acceleration_speed = 1 + min((ts - self.move_start_ts) / 0.5, 1.3)

        dx = self.power * acceleration_speed * self.x_dir
        dy = self.power * acceleration_speed * self.y_dir
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
        self.mouse_move_job = cron.interval("16ms", update_position)

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

        update_interval_ms = 16
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
        self.mouse_move_job = cron.interval("16ms", update_position)

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
        self.mouse_move_job = cron.interval("16ms", update_position)

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

class EventMouse:
    def __init__(self, Buttons, Scrolling, Movement):
        self.event_bus = EventBus()
        self.buttons = Buttons(self.event_bus)
        self.scrolling = Scrolling(self.event_bus)
        self.movement = Movement(self.event_bus)

        # self.event_bus.register("button_down", self.on_button_down)
        # self.event_bus.register("scroll_start", self.on_scroll_start)

        self.click = self.buttons.click
        self.drag = self.buttons.drag
        self.drag_stop = self.buttons.drag_stop
        self.scroll_start = self.scrolling.scroll_start
        self.scroll_stop_soft = self.scrolling.scroll_stop_soft
        self.scroll_stop_hard = self.scrolling.scroll_stop_hard
        self.move_start = self.movement.move_start
        self.move_start_new = self.movement.move_start_new
        self.move_stop_soft = self.movement.move_stop_soft
        self.move_stop_hard = self.movement.move_stop_hard
        self.is_scrolling = self.scrolling.is_scrolling
        self.is_moving = self.movement.is_moving

    # def on_button_down(self):
    #     self.scrolling.scroll_stop_hard()
    #     actions.user.tracking_control_freeze()

    # def on_scroll_start(self):
    #     actions.user.tracking_control_freeze()

event_mouse = EventMouse(Buttons, Scrolling, Movement)

def no_op():
    pass

@mod.action_class
class Actions:
    def event_mouse_click(button: str = 0):
        """Event mouse click""";
        event_mouse.click(button)

    def event_mouse_drag(button: int = 0):
        """Event mouse drag"""
        event_mouse.drag(button)

    def event_mouse_drag_stop():
        """Event mouse drag stop"""
        event_mouse.drag_stop()

    def event_mouse_scroll_start(direction: str = "down"):
        """Event mouse scroll start"""
        event_mouse.scroll_start(direction)

    def event_mouse_scroll_stop_soft():
        """Event mouse scroll stop soft"""
        event_mouse.scroll_stop_soft()

    def event_mouse_scroll_stop_hard():
        """Event mouse scroll stop hard"""
        event_mouse.scroll_stop_hard()

    def event_mouse_move_start(direction: Literal["up", "down", "left", "right"]):
        """Start moving mouse in a direction"""
        event_mouse.move_start_new(direction)

    def event_mouse_move_stop_soft():
        """Debounced stop moving the mouse"""
        event_mouse.move_stop_soft()

    def event_mouse_move_stop_hard():
        """Immediately stop moving the mouse"""
        event_mouse.move_stop_hard()

    def event_mouse_is_scrolling():
        """Event mouse scroll stop hard"""
        return event_mouse.is_scrolling()

    def event_mouse_is_moving():
        """Event mouse check is moving"""
        return event_mouse.is_moving()

    def on_event_mouse_click():
        """On mouse click"""
        no_op()

    def on_event_mouse_button_down():
        """On mouse down"""
        no_op()

    def on_event_mouse_button_up():
        """On mouse up"""
        no_op()

    def on_event_mouse_drag_start():
        """On drag start"""
        no_op()

    def on_event_mouse_drag_stop():
        """On drag stop"""
        no_op()

    def on_event_mouse_scroll_start():
        """On scroll start"""
        no_op()

    def on_event_mouse_scroll_stop():
        """On scroll stop"""
        no_op()
