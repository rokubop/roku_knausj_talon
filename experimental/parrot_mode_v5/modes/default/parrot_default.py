from talon import Module, Context, actions, settings, ctrl

mod = Module()
ctx = Context()

ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_default
"""

is_tracking = False

def teleport_and_track_head():
    global is_tracking
    if not actions.tracking.control_enabled():
        actions.tracking.control_toggle(True)
    actions.tracking.control_head_toggle(False)
    actions.tracking.control_gaze_toggle(True)
    actions.sleep("50ms")
    actions.tracking.control_gaze_toggle(False)
    actions.tracking.control_head_toggle(True)
    is_tracking = True

def freeze_tracking():
    global is_tracking
    if is_tracking:
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(False)
        is_tracking = False

@ctx.action_class("user")
class Actions:
    def on_parrot_v5_mode_enable():
        actions.user.add_red_cursor()

    def on_parrot_v5_mode_disable():
        actions.user.clear_screen_regions()
        actions.user.parrot_v5_stopper()

    def on_event_mouse_button_down():
        freeze_tracking()
        actions.user.add_red_cursor()

    def on_event_mouse_scroll_start():
        freeze_tracking()
        actions.user.add_red_cursor()

    def on_event_mouse_drag_start():
        actions.user.add_blue_cursor()

    def on_event_mouse_drag_stop():
        actions.user.add_red_cursor()

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
        freeze_tracking()

    def parrot_v5_positioner():
        """Use cursor/tracking positioning"""
        actions.user.add_green_cursor()
        teleport_and_track_head()

    def parrot_v5_mode_b_enable():
        """Enable secondary mode for example rpg mouse"""
        actions.user.parrot_v5_mode_enable("user.parrot_v5_rpg_mouse")