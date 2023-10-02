from talon import Module, Context, actions, ctrl
mod = Module()
ctx = Context()
ctx_parrot = Context()
ctx_parrot_default = Context()

mod.apps.chants_of_sennaar = r"""
app.exe: Chants Of Sennaar.exe
"""

ctx_parrot.matches = r"""
app: chants_of_sennaar
mode: user.parrot
"""

ctx.matches = r"""
app: chants_of_sennaar
"""

ctx_parrot_default.matches = r"""
app: chants_of_sennaar
tag: user.parrot_mode_default
"""

ctx_parrot.settings = {
    "user.parrot_mode_mouse_freeze_on_click": False,
    "user.parrot_rpg_increment_y": 75,
    "user.parrot_rpg_increment_x": 75,
}

@ctx.action_class("user")
class Actions:
    def pedal_center_down():
        ctrl.mouse_click(button=1, down=True)

    def pedal_center_up():
        ctrl.mouse_click(button=1, up=True)

@ctx_parrot_default.action_class("user")
class Actions:
    def parrot_hiss(): actions.user.parrot_mouse_click(track="gaze")
    def parrot_hiss_stop(): pass
    def parrot_shush(): actions.user.parrot_mouse_click(track="head")
    def parrot_shush_stop(): pass