from talon import actions, Module, Context, ctrl

mod = Module()
mod.tag("pedal_head_gaze", desc="head or gaze")
ctx = Context()
ctx.matches = "tag: user.pedal_head_gaze"

tracking_flag = False

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('success', '<*Pedal: Head/Gaze />')

    def pedal_left_down():
        global tracking_flag
        ctrl.mouse_click()
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(False)
        tracking_flag = False

    def pedal_left_up():
        actions.skip()

    def pedal_center_down():
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)

    def pedal_center_up():
        global tracking_flag
        if tracking_flag:
            tracking_flag = False
            actions.tracking.control_head_toggle(False)
            actions.tracking.control_gaze_toggle(False)
        else:
            tracking_flag = True
            if not actions.tracking.control_enabled():
                actions.tracking.control_toggle(True)
            actions.tracking.control_head_toggle(True)
            actions.tracking.control_gaze_toggle(True)
