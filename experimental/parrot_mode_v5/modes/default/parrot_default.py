from talon import Module, Context, actions, settings, ctrl

mod = Module()
ctx = Context()

ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_default
"""

@ctx.action_class("user")
class Actions:
    def parrot_v5_on_mode_enable():
        print("On parrot default enable")
        actions.user.add_red_cursor()

    def parrot_v5_on_mode_disable():
        print("On parrot default disable")
        actions.user.clear_screen_regions()

@mod.action_class
class Actions:
    def parrot_v5_click_primary():
        """Click the primary mouse button"""
        actions.user.event_mouse_click(0)

    def parrot_v5_click_alternate():
        """Click the alternate mouse button"""
        actions.user.event_mouse_click(1)

    def parrot_v5_drag_primary():
        """Drag primary mouse"""
        actions.user.event_mouse_drag(0)

    def parrot_v5_scroller_down():
        """Start scrolling down"""
        actions.user.event_mouse_scroll_start("down")

    def parrot_v5_scroller_up():
        """Start scrolling up"""
        actions.user.event_mouse_scroll_start("up")

    def parrot_v5_scroller_stop():
        """Stop scrolling"""
        actions.user.event_mouse_scroll_stop_soft()

    def parrot_v5_stopper():
        """Generic all purpose stopper"""
        actions.user.event_mouse_scroll_stop_hard()
