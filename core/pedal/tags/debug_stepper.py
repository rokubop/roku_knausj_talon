from talon import actions, ctrl, Module, Context

mod = Module()
mod.tag("pedal_debug_stepper", desc="for stepping over or continuing such as in a chrome debugger")
ctx = Context()
ctx.matches = "tag: user.pedal_debug_stepper"

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('event', '<*Pedal: Debugger />')

    def pedal_left_down():
        actions.key("f10")

    def pedal_left_up():
        actions.skip()

    def pedal_center_down():
        actions.key("f8")

    def pedal_center_up():
        actions.skip()
