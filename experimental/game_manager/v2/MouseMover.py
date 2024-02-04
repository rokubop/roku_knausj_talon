from talon import Module, Context, actions, ctrl, settings, cron
import platform
import math

mod = Module()
mod.setting("mouse_move_calibrate_360_x", type=int, default=1000)
ctx = Context()
os = platform.system().lower()

if os.startswith("windows"):
    import win32api, win32con

class MouseMover():
    def __init__(self):
        self.mouse_move_job = None
        self.current_dx = 0
        self.current_dy = 0
        self._callbacks = set()

        if os.startswith("windows"):
            self._mouse_move = self._mouse_move_windows
        else:
            self._mouse_move = self._mouse_move_generic

    def _mouse_move_generic(self, dx: int, dy: int):
        (x, y) = ctrl.mouse_pos()
        ctrl.mouse_move(x + dx, y + dy)

    def _mouse_move_windows(self, dx: int, dy: int):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

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
        return self.mouse_move_job is not None


mouse_mover = MouseMover()

@mod.action_class
class Actions:
    def mouse_move_delta_ease_out(x: int, y: int, duration_ms: int = 700, callback_stop: callable=None):
        """Move to a xy position relative to the cursor over a duration"""
        mouse_mover.move_to_pos_relative(x, y, duration_ms, callback_stop)

    def mouse_drag_delta_ease_out(button: int, x: int, y: int, duration_ms: int = 700):
        """Drag to a xy position relative to the cursor over a duration"""
        buttons_down = ctrl.mouse_buttons_down()
        if button not in buttons_down:
            ctrl.mouse_click(button=button, down=True)
            mouse_mover.move_to_pos_relative(
                x,
                y,
                duration_ms,
                lambda: ctrl.mouse_click(button=button, up=True))
        else:
            mouse_mover.move_to_pos_relative(x, y, duration_ms)

    def mouse_move_delta_degrees_ease_out(degrees_x: int, degrees_y: int, duration_ms: int = 700):
        """Drag to a xy position relative to the cursor over a duration"""
        dx_360 = settings.get("user.mouse_move_calibrate_360_x")
        x = dx_360 / 360 * degrees_x
        mouse_mover.move_to_pos_relative(x, 0, duration_ms)

    def mouse_drag_delta_degrees_ease_out(button: int, degrees_x: int, degrees_y: int, duration_ms: int = 700):
        """Drag to a xy position relative to the cursor over a duration"""
        buttons_down = ctrl.mouse_buttons_down()

        dx_360 = settings.get("user.mouse_move_calibrate_360_x")
        x = dx_360 / 360 * degrees_x

        if button not in buttons_down:
            ctrl.mouse_click(button=button, down=True)
            mouse_mover.move_to_pos_relative(
                x,
                0,
                duration_ms,
                lambda: ctrl.mouse_click(button=button, up=True))
        else:
            mouse_mover.move_to_pos_relative(x, 0, duration_ms)

    def mouse_move_constant(dx: int, dy: int):
        """Start moving in a direction at a constant speed"""
        mouse_mover.move_start(dx, dy)

    def mouse_drag_constant(button: int, dx: int, dy: int):
        """Start dragging in a direction at a cobnstant speed"""
        buttons_down = ctrl.mouse_buttons_down()
        if button in buttons_down:
            mouse_mover.move_start(dx, dy)
        else:
            ctrl.mouse_click(button=button, down=True)
            mouse_mover.move_start(dx, dy, lambda: ctrl.mouse_click(button=button, up=True))

    def mouse_move_stop():
        """Stop moving in a direction at a constant speed"""
        mouse_mover.stop_hard()

    def mouse_drag_stop():
        """Stop moving in a direction at a constant speed"""
        buttons_down = ctrl.mouse_buttons_down()
        for button in buttons_down:
            ctrl.mouse_click(button=button, up=True)
        mouse_mover.stop_hard()

    def mouse_move_calibrate_360_x(number: int):
        """Calibrate the 360 degree x axis"""
        mouse_mover.move_to_pos_relative(number, 0, 700, callback_tick=lambda x, y: actions.user.game_v2_canvas_refresh(f"Calibrate x: {int(x)}"))

    def mouse_drag_calibrate_360_x(button: int, number: int):
        """Calibrate the 360 degree x axis"""
        buttons_down = ctrl.mouse_buttons_down()
        if button in buttons_down:
            mouse_mover.move_to_pos_relative(number, 0, 700, callback_tick=lambda x, y: actions.user.game_v2_canvas_refresh(f"Calibrate x: {int(x)}"))
        else:
            ctrl.mouse_click(button=button, down=True)
            mouse_mover.move_to_pos_relative(number, 0, 700, lambda: ctrl.mouse_click(button=button, up=True), callback_tick=lambda x, y: actions.user.game_v2_canvas_refresh(f"Calibrate x: {int(x)}"))

    def mouse_move_delta_instant(dx: int, dy: int):
        """Move to a xy position relative to the cursor instantly"""
        mouse_mover._mouse_move(dx, dy)



@ctx.action_class("user")
class Actions:
    def parrot_pop():
        actions.user.mouse_drag_stop()
        actions.next()
