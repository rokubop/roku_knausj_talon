from talon import actions, Context, Module

mod = Module()
mod.tag("fl_studio_pedal_zoom_horizontally", desc="pedal zoom")
mod.tag("fl_studio_pedal_play", desc="pedal play")
ctx = Context()
ctx_pedal_zoom = Context()
ctx_pedal_play = Context()
ctx.matches = """
app: fl studio
"""
ctx_pedal_zoom.matches = """
app: fl studio
tag: user.fl_studio_pedal_zoom_horizontally
"""
ctx_pedal_play.matches = """
app: fl studio
tag: user.fl_studio_pedal_play
"""

@ctx.action_class("user")
class Actions:
    def pedal_available_tags():
        return ["user.fl_studio_pedal_zoom_horizontally", "user.fl_studio_pedal_play", "user.pedal_head_gaze", "user.fl_studio_ui"]

@ctx_pedal_zoom.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('warning', '<*Pedal: Zoom horizontally />')

    def pedal_left_down():
        actions.user.pause_eye_tracking()
        actions.key("ctrl:down")
        actions.user.mouse_scrolling("up")

    def pedal_left_up():
        actions.user.mouse_scroll_stop()
        actions.key("ctrl:up")

    def pedal_center_down():
        actions.user.pause_eye_tracking()
        actions.key("ctrl:down")
        actions.user.mouse_scrolling("down")

    def pedal_center_up():
        actions.user.mouse_scroll_stop()
        actions.key("ctrl:up")

@ctx_pedal_play.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('error', '<*Pedal: Play />')

    def pedal_left_down():
        actions.key("space")

    def pedal_left_up():
        actions.skip()

    def pedal_center_down():
        actions.skip()

    def pedal_center_up():
        actions.skip()
