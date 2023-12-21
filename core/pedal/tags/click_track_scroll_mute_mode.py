from talon import actions, ctrl, Module, Context, cron

mod = Module()
mod.tag("pedal_dynamic_1", desc="track, scroll, mute, click")
ctx = Context()
ctx.matches = "tag: user.pedal_dynamic_1"

left_side_b = False
left_hold_timer = None
center_side_b = False
center_double_tap_timer = None
right_side_b = False
right_hold_timer = None
scroll_dir = "down"
speech_toggle_flag = True

def set_left_side_b():
    global left_side_b
    left_side_b = True
    actions.user.hud_publish_mouse_particle('float_up', '20b2aa')

def unset_center_side_b():
    global center_side_b
    center_side_b = False

def set_right_side_b():
    global right_side_b
    right_side_b = True
    actions.user.hud_publish_mouse_particle('float_up', '20b2aa')

def start_left_hold_timer():
    global left_hold_timer
    reset_left_hold_timer()
    left_hold_timer = cron.after("1s", set_left_side_b)

def reset_left_hold_timer():
    global left_side_b, left_hold_timer
    left_side_b = False
    if left_hold_timer:
        cron.cancel(left_hold_timer)
        left_hold_timer = None

def start_center_double_tap_timer():
    global center_double_tap_timer, center_side_b
    reset_center_double_tap_timer()
    center_side_b = True
    center_double_tap_timer = cron.after("1s", unset_center_side_b)

def reset_center_double_tap_timer():
    global center_side_b, center_double_tap_timer
    center_side_b = False
    if center_double_tap_timer:
        cron.cancel(center_double_tap_timer)
        center_double_tap_timer = None

def start_right_hold_timer():
    global right_hold_timer
    reset_right_hold_timer()
    right_hold_timer = cron.after("1s", set_right_side_b)

def reset_right_hold_timer():
    global right_side_b, right_hold_timer
    right_side_b = False
    if right_hold_timer:
        cron.cancel(right_hold_timer)
        right_hold_timer = None

def microphone_toggle():
    global speech_toggle_flag
    if speech_toggle_flag:
        actions.user.hud_publish_mouse_particle('float_up', '30F343')
        actions.sound.set_microphone("Microphone (Yeti X)")
        actions.user.hud_add_log('event', '<*Voice: on/>')
    else:
        actions.user.hud_publish_mouse_particle('float_up', 'ff0000')
        actions.sleep("1s")
        actions.sound.set_microphone("None")
        actions.user.hud_add_log('error', '<*Voice: off />')
    speech_toggle_flag = not speech_toggle_flag


@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('event', '<*Pedal: Dynamic 1 />')

    def pedal_left_down():
        actions.user.tracking_control_gaze_toggle(False)
        actions.user.tracking_control_head_toggle(False)
        start_left_hold_timer()

    def pedal_left_up():
        global left_side_b
        if left_side_b:
            if actions.user.tracking_control_was_moving():
                actions.user.tracking_control_head_toggle(False)
                actions.user.tracking_control_gaze_toggle(False)
            else:
                actions.user.tracking_control_head_toggle(True)
                actions.user.tracking_control_gaze_toggle(True)
        else:
            ctrl.mouse_click()
            actions.user.tracking_control_resume()

        reset_left_hold_timer()

    def pedal_center_down():
        global center_side_b, scroll_dir

        if center_side_b:
            scroll_dir = "up" if scroll_dir == "down" else "down"

        actions.user.mouse_scrolling(scroll_dir)
        start_center_double_tap_timer()

    def pedal_center_up():
        actions.user.mouse_scroll_stop()

    def pedal_right_down():
        start_right_hold_timer()

    def pedal_right_up():
        global right_side_b
        if right_side_b:
            actions.user.pedal_tag_switch()
        else:
            microphone_toggle()

        reset_right_hold_timer()


