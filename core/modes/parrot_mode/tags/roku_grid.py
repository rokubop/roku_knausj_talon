from talon import Module, actions
import win32api, win32con

mod = Module()
mod.mode("roku_grid", "Tag for roku grid mode")

@mod.action_class
class Actions:
    def map_show():
        """Show the map"""
        actions.user.canvas_test_three()

    def map_hide():
        """Hide the map"""
        actions.user.canvas_test_freeze()

    # def mouse_move_native(x: int, y: int):
    #     """Move the mouse to the given coordinates"""
    #     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x - 1920/2), int(y - 1080/2))
