from talon import Module
from ..event_mouse import event_mouse
from .profiles import profile_dash, profile_nav

def no_op():
    pass

mod = Module()

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

    def event_mouse_move_start(direction: str):
        """Start moving mouse in a direction"""
        event_mouse.move_start_new(direction)

    def event_mouse_dash(direction: str):
        """Dash in a direction"""
        event_mouse.update_profile(profile_dash)
        event_mouse.move_start_new(direction)

    def event_mouse_nav(direction: str):
        """Start navigating in a direction"""
        event_mouse.update_profile(profile_nav)
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
