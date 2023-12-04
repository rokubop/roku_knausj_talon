from talon import actions, Module, Context

mod = Module()
mod.tag("pedal_head_gaze", desc="head or gaze")
ctx = Context()
ctx.matches = "tag: user.pedal_head_gaze"

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('success', '<*Pedal: Head/Gaze />')

    def pedal_left_down():
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)

    def pedal_left_up():
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)

    def pedal_center_down():
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)

    def pedal_center_up():
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
