from talon import Module, ctrl
import platform

mod = Module()
os = platform.system().lower()

if os.startswith("windows"):
    import win32api, win32con

class MouseMover():
    def __init__(self):
        self.mouse_move_job = None
        if os.startswith("windows"):
            self._mouse_move = self._mouse_move_windows
        else:
            self._mouse_move = self._mouse_move_generic

    def _mouse_move_generic(self, dx: int, dy: int):
        (x, y) = ctrl.mouse_pos()
        ctrl.mouse_move(x + dx, y + dy)

    def _mouse_move_windows(self, dx: int, dy: int):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

    def move_start(self, dx: int, dy: int, speed: int = 1, acceleration: int = 1, min_speed: int = 100, max_speed: int = 200):
        """Start moving the mouse in a direction at a speed"""
        pass

    # def move_to_camera_angle_relative(self, x_degree: int, y_degree: int, duration_ms: int = 700, curve: str = "linear"):
    #     """Move to a camera angle relative to current position in a 360 degree space over a duration"""
    #     pass

    # def move_to_camera_angle_absolute(self, x_degree: int, y_degree: int, duration_ms: int = 0, curve: str = "linear"):
    #     """Move to a specific camera angle based on an anchor point in a 360 degree space over a duration"""
    #     pass

    def move_to_pos_relative(self, x: int, y: int, duration_ms: int = 700, curve: str = "linear"):
        """Move to a xy position relative to the cursor over a duration"""
        pass

    # def move_to_pos_absolute(self, x: int, y: int, duration_ms: int = 0, curve: str = "linear"):
    #     """Move to a xy screen position over a duration"""
    #     pass

    def stop_hard(self):
        pass

    def stop_soft(self, duration_ms: int = 700, curve: str = "ease_out"):
        pass

mouse_mover = MouseMover()

@mod.action_class
class Actions:
    def mouse_move_to_pos_relative(x: int, y: int, duration_ms: int = 700, curve: str = "linear"):
        """Move to a xy position relative to the cursor over a duration"""
        mouse_mover.move_to_pos_relative(x, y, duration_ms, curve)
