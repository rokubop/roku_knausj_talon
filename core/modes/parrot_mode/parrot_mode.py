import time
from talon import Module, Context, actions, ctrl, settings, app, speech_system, cron
from ....plugin.debouncer import Debouncer

mod = Module()
mod.mode("parrot", "Parrot Mode for controlling mouse, modifiers, and scrolling")
mod.tag("parrot_tracking", desc="Tag for parrot tracking mode")

ctx = Context()

is_dragging = False
modifiers = []

shush_debouncer = Debouncer(150, actions.user.parrot_scroll_up_start, actions.user.parrot_scroll_up_stop)
hiss_debouncer = Debouncer(150, actions.user.parrot_scroll_down_start, actions.user.parrot_scroll_down_stop)
is_mouse_moving = False
current_tracking_mode = 'default'
is_eye_tracker_enabled = False
use_active_mouse = False
flex_macro = None
special = False
recent_tools = []
mouse_pos_history = {
    'current': '1',
    '1': None,
    '2': None,
}

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

    def parrot_is_active_mouse_enabled() -> bool:
        """Is active mouse enabled"""
        global use_active_mouse
        return use_active_mouse

    def parrot_toggle_active_mouse():
        """Toggle active mouse"""
        global use_active_mouse
        use_active_mouse = not use_active_mouse
        print(f"use active mouse: {use_active_mouse}")
        if use_active_mouse:
            actions.user.hud_publish_mouse_particle('float_up', '30F343')
            actions.tracking.control_head_toggle(True)
            actions.tracking.control_gaze_toggle(True)
        else:
            actions.user.hud_publish_mouse_particle('float_up', 'F36D30')


    def parrot_mouse_drag(button: int):
        """Drag the mouse in a direction"""
        global is_dragging

        if not is_dragging:
            is_dragging = True
            actions.user.add_blue_cursor()
            for key in modifiers:
                actions.key(f"{key}:down")
            ctrl.mouse_click(button=button, down=True)

    def parrot_mouse_click(button: int = 0, times: int = 1, track: str = "freeze"):
        """Click the mouse"""
        global is_dragging, use_active_mouse

        if is_dragging:
            # if use_active_mouse:
            actions.user.parrot_mouse_and_scroll_stop_keep_modifiers()
            # else:
            #     actions.user.parrot_mouse_and_scroll_stop()
        else:
            for key in modifiers:
                actions.key(f"{key}:down")
            for i in range(times):
                ctrl.mouse_click(button=button, hold=16000)
            # if not use_active_mouse:
            #     actions.user.parrot_cancel_modifiers()

        print("setting for mouse freeze")
        print(settings.get("user.parrot_mode_mouse_freeze_on_click"))
        if track == "freeze" or settings.get("user.parrot_mode_mouse_freeze_on_click"):
            print("freeze mode")
            if not use_active_mouse:
                actions.user.parrot_freeze_mouse()
        elif track == "gaze":
            print("gaze mode")
            actions.user.parrot_use_default_tracking()
        elif track == "head":
            print("head mode")
            actions.user.parrot_use_head_tracking_only()

    def parrot_mouse_move_previous_position():
        """Move the mouse to the previous position"""
        global mouse_pos_history

        if mouse_pos_history['current'] == "1":
            mouse_pos_history["1"] = ctrl.mouse_pos()
            mouse_pos_history['current'] = "2"
            if mouse_pos_history["2"]:
                ctrl.mouse_move(*mouse_pos_history["2"])
        else:
            mouse_pos_history["2"] = ctrl.mouse_pos()
            mouse_pos_history['current'] = "1"
            if mouse_pos_history["1"]:
                ctrl.mouse_move(*mouse_pos_history["1"])

    def parrot_scroll_down():
        """Scroll the mouse down"""
        for key in modifiers:
            actions.key(f"{key}:down")
        hiss_debouncer.start()

    def parrot_scroll_up():
        """Scroll the mouse up"""
        for key in modifiers:
            actions.key(f"{key}:down")
        shush_debouncer.start()

    def parrot_scroll_stop_soft():
        """Stop scrolling the mouse"""
        shush_debouncer.stop()
        hiss_debouncer.stop()

    def parrot_set_cursor_color():
        """Set the cursor color"""
        if actions.user.parrot_mode_has_tag("user.parrot_side_b"):
            actions.user.add_color_cursor("FF00FF")
        elif actions.user.parrot_mode_has_tag("user.parrot_default_interactive"):
            actions.user.add_color_cursor("f22160")
        elif actions.user.parrot_mode_has_tag("user.parrot_pan"):
            actions.user.add_color_cursor("FFA500")
        else:
            actions.user.add_red_cursor()

    def parrot_mouse_stop():
        """Stop mouse"""
        global is_dragging
        if is_dragging:
            actions.user.parrot_set_cursor_color()
        is_dragging = False
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)

    def parrot_disable_running():
        """Disable running"""
        actions.user.parrot_mouse_stop()
        actions.user.parrot_cancel_modifiers()
        if not actions.user.parrot_is_active_mouse_enabled():
            actions.user.parrot_freeze_mouse()
        actions.user.mouse_scroll_stop()
        shush_debouncer.stop()
        hiss_debouncer.stop()

    def parrot_mouse_and_scroll_stop():
        """Stop mouse and scroll"""
        actions.user.parrot_mouse_stop()
        actions.user.parrot_cancel_modifiers()
        actions.user.parrot_freeze_mouse()
        actions.user.mouse_scroll_stop()
        shush_debouncer.stop()
        hiss_debouncer.stop()

    def parrot_mouse_and_scroll_stop_keep_modifiers():
        """Stop mouse and scroll but keep modifiers"""
        global is_dragging
        if is_dragging:
            actions.user.parrot_set_cursor_color()
        is_dragging = False
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)
        actions.user.parrot_freeze_mouse()
        actions.user.mouse_scroll_stop()
        shush_debouncer.stop()
        hiss_debouncer.stop()

    def parrot_set_modifier(key: str):
        """Set the modifier"""
        if not is_dragging and key not in modifiers:
            print("prepare modifier " + key)
            if key == 'shift':
                print("shift")
                actions.user.hud_add_ability('modifiers',
                    image='shift_down',
                    enabled=True,
                    colour='FFFFFF',
                    activated=True)
            elif key == 'ctrl':
                print("ctrl")
                actions.user.hud_add_ability('modifiers',
                    image='ctrl',
                    enabled=True,
                    colour='FFFFFF',
                    activated=True)
            elif key == 'alt':
                print("alt")
                actions.user.hud_add_ability('modifiers',
                    image='alt',
                    enabled=True,
                    colour='FFFFFF',
                    activated=True)

            modifiers.append(key)

    def parrot_cancel_modifiers():
        """Cancel modifiers"""
        for key in modifiers:
            actions.key(f"{key}:up")
        actions.user.hud_add_ability('modifiers', image='shift_down', enabled=False, colour='FFFFFF',  activated=False)
        modifiers.clear()

    def parrot_cursor_stay_toggle():
        """Toggle cursor stay"""
        actions.user.mouse_toggle_stay_in_place()

    def parrot_deactivates_special():
        """Deactivate special"""
        global special
        special = False
        actions.user.parrot_side_b_disable()
        # print(actions.user.parrot_mode_remove_tag("user.parrot_side_b"))
        # print(actions.user.parrot_mode_has_tag("user.parrot_default_interactive"))
        # print(actions.user.parrot_mode_has_tag("user.parrot_fps"))
        # print(actions.user.parrot_mode_has_tag("user.parrot_pan"))
        # actions.user.parrot_set_cursor_color()

    def parrot_activate_side_b_briefly():
        """Activate special briefly"""
        global special
        special = True
        actions.user.parrot_side_b_enable()
        # actions.user.parrot_mode_append_tag("user.parrot_side_b")
        # actions.user.add_color_cursor("FF00FF")
        cron.after("300ms", lambda : actions.user.parrot_deactivates_special())


    def parrot_trigger_virtual_key():
        """Trigger virtual key"""
        actions.user.hud_activate_virtual_key()

    def kingfisher_parrot_trigger_virtual_key():
        """Temporarily teleport mouse and trigger virtual key"""
        actions.user.hud_publish_mouse_particle('float_up', 'FFFF00')
        pos = ctrl.mouse_pos()
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle(True)
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        actions.user.hud_activate_virtual_key()
        ctrl.mouse_move(*pos)
        if is_mouse_moving:
            if current_tracking_mode == 'default':
                actions.user.parrot_use_default_tracking()
            else:
                actions.user.parrot_use_head_tracking_only()
        else:
            actions.user.parrot_freeze_mouse()

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
        global is_mouse_moving, special
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle(True)

        if special:
            actions.user.parrot_cancel_modifiers()
            actions.user.parrot_toggle_active_mouse()

        if actions.user.parrot_is_active_mouse_enabled():
            actions.tracking.control_gaze_toggle(True)
            actions.tracking.control_head_toggle(True)
            return

        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)
        if actions.user.parrot_mode_has_tag("user.parrot_side_b"):
            actions.user.add_color_cursor("00FFFF")
        else:
            actions.user.add_green_cursor()
        is_mouse_moving = True

    def parrot_is_mouse_moving():
        """Is mouse moving"""
        return is_mouse_moving

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
        actions.user.parrot_set_cursor_color()
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

    def parrot_set_flex_macro():
        """Set flex macro"""
        global flex_macro
        flex_macro = actions.user.history_get(1)

    def parrot_clear_flex_macro():
        """Clear flex macro"""
        global flex_macro
        flex_macro = None

    def parrot_run_flex_macro():
        """Run flex macro"""
        global flex_macro
        if flex_macro:
            actions.mode.disable("user.parrot")
            actions.mode.enable("command")
            actions.mimic(flex_macro)
            actions.mode.disable("command")
            actions.mode.enable("user.parrot")

    def parrot_tool_switch():
        """Parrot tool switch"""
        global recent_tools
        if not len(recent_tools):
            recent_tools = actions.user.parrot_tools_get()

        if recent_tools[1]:
            actions.key(recent_tools[1])
            recent_tools = [recent_tools[1], recent_tools[0], recent_tools[2:]]

    def parrot_tools_get():
        """Parrot get tools"""
        return ["p", "c", "t", "m"]

mod = Module()
@mod.action_class
class UserActions:
    # def parrot_mode_enable():
    #     """Enable parrot mode"""
    #     print("parrot mode enabled")
    #     actions.user.clear_screen_regions()
    #     actions.user.add_red_cursor()
    #     actions.mode.enable("user.parrot")
    #     actions.mode.disable("command")
    #     actions.mode.disable("dictation")

    # def parrot_mode_disable():
    #     """Disable parrot mode"""
    #     print('parrot mode disabled')
    #     actions.user.parrot_scroll_stop_soft()
    #     actions.user.parrot_mouse_and_scroll_stop()
    #     actions.user.clear_screen_regions()
    #     actions.user.mouse_scroll_stop()
    #     # is_eye_tracker_enabled = False
    #     actions.mode.disable("user.parrot")
    #     actions.mode.enable("command")
    #     actions.mode.disable("dictation")

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


    def virtual_region_one():
        """Virtual region one"""
        actions.user.parrot_set_flex_macro()
        print('region one')

    def virtual_region_two():
        """Virtual region two"""
        actions.user.parrot_track_toggle()
        actions.user.parrot_use_default_tracking()
        print('region two')

    def virtual_region_three():
        """Virtual region three"""
        print('region three')

    def virtual_region_four():
        """Virtual region four"""
        actions.user.parrot_toggle_active_mouse()
        print('region four')

    def virtual_region_five():
        """Virtual region five"""
        # if actions.user.parrot_mode_has_tag('user.parrot_side_b'):
        #     actions.user.parrot_side_b_disable()
        #     actions.user.parrot_mode_reset_tags()
        # else:
        #     actions.user.parrot_side_b_enable()
        print('region five')

    def virtual_region_six():
        """Virtual region six"""
        print('region six')

    def virtual_region_seven():
        """Virtual region seven"""
        actions.user.parrot_set_modifier('ctrl')
        print('region seven')
        print('holding ctrl')

    def virtual_region_eight():
        """Virtual region eight"""
        actions.user.parrot_set_modifier('shift')
        print('region eight')
        print('holding shift')

    def virtual_region_nine():
        """Virtual region nine"""
        actions.user.parrot_set_modifier('alt')
        print('region nine')
        print('holding alt')

def register_regions():
    keys = [
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_one, 'One'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_two, 'Two'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_three, 'Three'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_four, 'Four'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_five, 'Five'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_six, 'Six'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_seven, 'Seven'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_eight, 'Eight'),
	    actions.user.hud_create_virtual_key(actions.user.virtual_region_nine, 'Nine'),
	  ]
    actions.user.hud_register_virtual_keyboard('virtual_keyboard', keys)
    actions.user.hud_set_virtual_keyboard('virtual_keyboard')
    actions.user.hud_set_virtual_keyboard_visibility(0)

app.register('ready', register_regions)