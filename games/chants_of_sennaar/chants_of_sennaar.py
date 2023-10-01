from talon import Module, Context, actions
mod = Module()
ctx_parrot_mode = Context()
ctx_parrot_mode_default = Context()
ctx_parrot_mode_rpg = Context()

mod.apps.chants_of_sennaar = r"""
os: windows
and app.exe: Chants Of Sennaar.exe
"""

ctx_parrot_mode.matches = r"""
app: chants_of_sennaar
mode: user.parrot_mode
"""

ctx_parrot_mode_default.matches = r"""
app: chants_of_sennaar
tag: user.parrot_mode_default
"""

ctx_parrot_mode_rpg.matches = r"""
app: chants_of_sennaar
tag: user.parrot_mouse_rpg
"""

ctx_parrot_mode.settings = {
    "user.parrot_mode_mouse_freeze_on_click": False,
}

ctx_parrot_mode_rpg.settings = {
    "user.parrot_rpg_increment_y": 75,
    "user.parrot_rpg_increment_x": 75,
}

@ctx_parrot_mode_default.action_class("user")
class Actions:
    def parrot_hiss(): actions.user.parrot_mouse_click(track="gaze")
    def parrot_hiss_stop(): pass
    def parrot_shush(): actions.user.parrot_mouse_click(track="head")
    def parrot_shush_stop(): pass