from talon import actions, ctrl, Module, Context, cron
# from .obs_websocket import toggle_virtual_camera
mod = Module()
mod.tag("pedal_dynamic_1", desc="track, scroll, mute, click")
ctx = Context()
ctx.matches = "tag: user.pedal_dynamic_1"




left_side_b = False
left_hold_timer = None
right_side_b = False
right_hold_timer = None
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
    left_hold_timer = cron.after("300ms", set_left_side_b)

def reset_left_hold_timer():
    global left_side_b, left_hold_timer
    left_side_b = False
    if left_hold_timer:
        cron.cancel(left_hold_timer)
        left_hold_timer = None

def start_right_hold_timer():
    global right_hold_timer
    reset_right_hold_timer()
    right_hold_timer = cron.after("500ms", set_right_side_b)

def reset_right_hold_timer():
    global right_side_b, right_hold_timer
    right_side_b = False
    if right_hold_timer:
        cron.cancel(right_hold_timer)
        right_hold_timer = None

last_active_microphone = None

def microphone_toggle():
    global speech_toggle_flag, last_active_microphone
    current_microphone = actions.sound.active_microphone()
    if current_microphone and current_microphone != "None":
        last_active_microphone = current_microphone

    if speech_toggle_flag:
        actions.user.hud_publish_mouse_particle('float_up', '30F343')
        actions.sound.set_microphone(last_active_microphone)
        actions.user.hud_add_log('event', '<*Voice: on/>')
    else:
        actions.user.hud_publish_mouse_particle('float_up', 'ff0000')
        actions.sleep("1s")
        actions.sound.set_microphone("None")
        actions.user.hud_add_log('error', '<*Voice: off />')
    speech_toggle_flag = not speech_toggle_flag

double_tap_timeout_setting = "500ms"

double_tap_timer = None
double_tap_enabled = False

def start_double_tap_timer():
    global double_tap_timer, double_tap_enabled
    clear_double_tap_timer()
    double_tap_enabled = True
    double_tap_timer = cron.after(double_tap_timeout_setting, clear_double_tap_timer)

def clear_double_tap_timer():
    global double_tap_enabled, double_tap_timer
    double_tap_enabled = False
    if double_tap_timer:
        cron.cancel(double_tap_timer)
        double_tap_timer = None

use_click = False
use_active = False

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('event', '<*Pedal: Dynamic 1 />')

    def pedal_left_down():
        global use_click, double_tap_enabled, use_active

        if double_tap_enabled:
            use_click = not use_click
            if use_click:
                actions.user.hud_add_log('warning', '<*Click mode/>')
            else:
                actions.user.hud_add_log('event', '<*Scroll mode/>')

            color = 'd4a000' if use_click else 'ff5500'
            actions.user.hud_publish_mouse_particle('float_up', color)
            return

        start_double_tap_timer()

        # print(use_active)
        # if use_active:
        #     actions.tracking.control_gaze_toggle(True)
        #     actions.tracking.control_head_toggle(True)
        # else:
        #     actions.tracking.control_gaze_toggle(False)
        #     actions.tracking.control_head_toggle(False)

        # use_active = not use_active


        actions.user.tracking_control_gaze_toggle(True)
        actions.user.tracking_control_head_toggle(False)
        actions.sleep("50ms")
        actions.user.tracking_control_gaze_toggle(False)
        actions.user.tracking_control_head_toggle(True)

    def pedal_left_up():
        actions.user.tracking_control_gaze_toggle(False)
        actions.user.tracking_control_head_toggle(False)
        return

    def pedal_center_down():
        global use_click
        if use_click:
            ctrl.mouse_click(button=0, down=True)
        else:
            actions.user.pedal_scroll_up_or_down_dbl_tap()


    def pedal_center_up():
        global use_click
        if use_click:
            ctrl.mouse_click(button=0, up=True)
        else:
            actions.user.pedal_scroll_up_or_down_dbl_tap_stop()


    def pedal_right_down():
        # if I hold for one second
        # toggle obs
        # toggle mic- maybe virtual cable?
        # toggle_virtual_camera()
        microphone_toggle()

    def pedal_right_up():
        actions.skip()
