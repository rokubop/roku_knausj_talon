from talon import actions, Context, Module

mod = Module()

# ui mode
mod.tag("fl_studio_ui", desc="ui mode")

ctx_ui = Context()
ctx_ui_parrot = Context()

ctx_ui.matches = """
app: fl studio
tag: user.fl_studio_ui
os: windows
"""

ctx_ui_parrot.matches = """
app: fl studio
tag: user.fl_studio_ui
mode: user.parrot
os: windows
"""

@ctx_ui.action_class("user")
class Actions:
    def pedal_left_down():    actions.user.rpg_mouse_move_up()
    def pedal_left_up():      actions.user.rpg_mouse_stop()
    def pedal_center_down():  actions.user.rpg_mouse_move_down()
    def pedal_center_up():    actions.user.rpg_mouse_stop()

@ctx_ui_parrot.action_class("user")
class Actions:
    def parrot_oh():
        if actions.user.parrot_mode_has_tag("user.rpg_mouse"):
            actions.next()
        else:
            actions.user.parrot_mouse_drag()
            actions.user.parrot_rpg_mouse_mode_enable()
