from talon import Module, Context, actions, ctrl
from ....plugin.debouncer import Debouncer

mod = Module()
mod.mode("parrot", "Parrot Mode for controlling mouse, modifiers, and scrolling")
mod.tag("parrot_tracking", desc="Tag for parrot tracking mode")
mod.tag("parrot_hiss_pop_mouse", desc="Tag for hiss pop mouse")
ctx = Context()

is_dragging = False
modifiers = []

shush_debouncer = Debouncer(150, actions.user.parrot_scroll_up_start, actions.user.parrot_scroll_up_stop)
hiss_debouncer = Debouncer(150, actions.user.parrot_scroll_down_start, actions.user.parrot_scroll_down_stop)
is_mouse_moving = False
current_tracking_mode = 'default'
is_eye_tracker_enabled = False

@mod.action_class
class ParrotModeActions:
    def parrot_scroll_up_start():
        """Shush start"""
        actions.user.parrot_freeze_mouse()
        actions.user.mouse_scrolling("up")

    def parrot_scroll_up_stop():
        """Shush stop"""
        actions.user.mouse_scroll_stop()

    def parrot_scroll_down_start():
        """Hiss start"""
        actions.user.parrot_freeze_mouse()
        actions.user.mouse_scrolling("down")

    def parrot_scroll_down_stop():
        """Hiss stop"""
        actions.user.mouse_scroll_stop()

    def parrot_mouse_drag(button: int):
        """Drag the mouse in a direction"""
        global is_dragging

        if not is_dragging:
            is_dragging = True
            actions.user.add_blue_cursor()
            for key in modifiers:
                actions.key(f"{key}:down")
            ctrl.mouse_click(button=button, down=True)

    def parrot_mouse_click(button: int, times: int = 1):
        """Click the mouse"""
        global is_dragging

        if is_dragging:
            actions.user.parrot_mouse_and_scroll_stop()
        else:
            for key in modifiers:
                actions.key(f"{key}:down")
            for i in range(times):
                ctrl.mouse_click(button=button, hold=16000)
            for key in modifiers:
                actions.key(f"{key}:up")
        actions.user.parrot_freeze_mouse()
        actions.user.parrot_mode_disable()

    def parrot_scroll_down():
        """Scroll the mouse down"""
        for key in modifiers:
            actions.key(f"{key}:down")
        hiss_debouncer.start()
        # actions.user.mouse_scroll_down();

    def parrot_scroll_up():
        """Scroll the mouse up"""
        for key in modifiers:
            actions.key(f"{key}:down")
        shush_debouncer.start()
        # actions.user.mouse_scroll_up();

    def parrot_scroll_stop_soft():
        """Stop scrolling the mouse"""
        shush_debouncer.stop()
        hiss_debouncer.stop()

    def parrot_mouse_and_scroll_stop():
        """Stop mouse and scroll"""
        global is_dragging
        if is_dragging:
            actions.user.add_red_cursor()
        is_dragging = False
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)
        for key in modifiers:
            actions.key(f"{key}:up")
        actions.user.parrot_freeze_mouse()
        actions.user.mouse_scroll_stop()
        shush_debouncer.stop()
        hiss_debouncer.stop()
        modifiers.clear()

    def parrot_set_modifier(key: str):
        """Set the modifier"""
        if not is_dragging and key not in modifiers:
            print("prepare modifier " + key)
            modifiers.append(key)

    def parrot_cancel_modifiers():
        """Cancel modifiers"""
        for key in modifiers:
            actions.key(f"{key}:up")
        modifiers.clear()

    def parrot_cursor_stay_toggle():
        """Toggle cursor stay"""
        actions.user.mouse_toggle_stay_in_place()

    def parrot_trigger_virtual_key():
        """Trigger virtual key"""
        print("eh from parrot mode")
        actions.user.hud_activate_virtual_key()

    def parrot_zoom():
        """Zoom"""
        actions.user.mouse_toggle_zoom_mouse()

    def parrot_track_toggle():
        """Toggle track"""
        actions.user.hud_publish_mouse_particle('float_up', '20b2aa')
        actions.tracking.control_toggle()

    # hiss for speedup - gaze plus head
    # shush for slowdown - head tracking only
    # ee for stop or teleport
    # pop for click
    # tut for toggling movement
    # eh for toggling on or off

    def parrot_control_mouse_on():
        """Control mouse on"""
        actions.tracking.control_toggle(True)

    def parrot_control_mouse_off():
        """Control mouse off"""
        actions.tracking.control_toggle(False)

    def parrot_mouse_teleport_or_freeze():
        """Teleport or freeze mouse"""
        if is_mouse_moving:
            actions.user.parrot_freeze_mouse()
        else:
            actions.user.parrot_mouse_teleport()

    def parrot_teleport_mouse_soft():
        """Teleport mouse and enable head tracking until next action"""
        global is_mouse_moving
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)
        actions.user.add_green_cursor()
        is_mouse_moving = True

    def parrot_mouse_teleport():
        """Teleport mouse"""
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        if is_mouse_moving:
            if current_tracking_mode == 'default':
                actions.user.parrot_use_default_tracking()
            else:
                actions.user.parrot_use_head_tracking_only()
        else:
            actions.user.parrot_freeze_mouse()

    def parrot_mouse_move_toggle():
        """Toggle mouse move"""
        global is_eye_tracker_enabled, is_mouse_moving
        if not is_eye_tracker_enabled:
            actions.tracking.control_toggle(True)
            is_eye_tracker_enabled = True
        if is_mouse_moving:
            actions.user.parrot_freeze_mouse()
        else:
            actions.user.parrot_use_default_tracking()

    def parrot_freeze_mouse():
        """Freeze mouse"""
        global is_mouse_moving
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(False)
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        is_mouse_moving = False

    def parrot_use_head_tracking_only():
        """Use head tracking only"""
        global is_mouse_moving
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)
        is_mouse_moving = True
        # current_tracking_mode = 'head'

    def parrot_use_default_tracking():
        """Use head tracking only"""
        global is_mouse_moving, current_tracking_mode
        actions.tracking.control_gaze_toggle(True)
        actions.tracking.control_head_toggle(True)
        is_mouse_moving = True
        current_tracking_mode = 'default'

    def parrot_omega_mouse():
        """Omega mouse for parrot"""
        global is_mouse_moving
        if is_mouse_moving:
            actions.mouse_click()
            actions.user.parrot_freeze_mouse()
        else:
            actions.tracking.control_gaze_toggle(True)
            actions.tracking.control_head_toggle(False)
            actions.sleep("50ms")
            actions.tracking.control_gaze_toggle(False)
            actions.tracking.control_head_toggle(True)
            is_mouse_moving = True





mod = Module()
@mod.action_class
class UserActions:
    def parrot_mode_enable():
        """Enable parrot mode"""
        print("parrot mode enabled")
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        actions.mode.enable("user.parrot")
        actions.mode.disable("command")
        actions.mode.disable("dictation")

    def parrot_mode_disable():
        """Disable parrot mode"""
        print('parrot mode disabled')
        actions.user.parrot_scroll_stop_soft()
        actions.user.parrot_mouse_and_scroll_stop()
        actions.user.clear_screen_regions()
        actions.user.mouse_scroll_stop()
        # is_eye_tracker_enabled = False
        actions.mode.disable("user.parrot")
        actions.mode.enable("command")
        actions.mode.disable("dictation")

    def parrot_tracking_mode_enable():
        """Enable parrot tracking mode"""
        print("parrot tracking mode enabled")
        actions.user.parrot_mouse_move_toggle()
        actions.user.add_purple_cursor()
        ctx.tags = ["user.parrot_tracking"]

    def parrot_tracking_mode_disable():
        """Disable parrot tracking mode"""
        print("parrot tracking mode disable")
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        # actions.user.parrot_use_default_tracking()
        ctx.tags = []




@ctx.action_class("user")
class UserActions:
    def virtual_region_one():
        print('got it')