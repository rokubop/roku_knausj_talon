from talon import actions, Module, Context

mod = Module()
mod.tag("pedal_scroll_up_down", desc="pedal scrolling up or down")
ctx = Context()
ctx.matches = "tag: user.pedal_scroll_up_down"

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('event', '<*Pedal: Scrolling />')

    def pedal_left_down():
        actions.user.mouse_scrolling("up")

    def pedal_left_up():
        actions.user.mouse_scroll_stop()

    def pedal_center_down():
        actions.user.mouse_scrolling("down")

    def pedal_center_up():
        actions.user.mouse_scroll_stop()
