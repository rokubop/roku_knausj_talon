from talon import Module, Context, actions, ui, skia, cron, ctrl
from talon.screen import Screen
from talon.canvas import Canvas, MouseEvent
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia import RoundRect
from talon.types import Rect, Point2d

mod = Module()

@mod.action_class
class Actions:
    def ui_get_current_screen():
        """Get the current screen"""
        current_screen = None
        (x, y) = ctrl.mouse_pos()
        for screen in ui.screens():
            if screen.contains(x, y):
                current_screen = screen
                break
        return current_screen
