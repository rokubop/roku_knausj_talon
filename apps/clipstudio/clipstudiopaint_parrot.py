from talon import Module, Context, actions
mod = Module()
ctx = Context()
ctx_parrot = Context()
ctx_parrot_default = Context()

mod.apps.clipstudiopaint = r"""
app.exe: CLIPStudioPaint.exe
"""

ctx.matches = r"""
app: clipstudiopaint
"""

ctx_parrot.matches = r"""
app: clipstudiopaint
mode: user.parrot
"""

ctx_parrot_default.matches = r"""
app: clipstudiopaint
tag: user.parrot_default_interactive
"""

# ctx_parrot.settings = {
#     "user.rpg_mouse_increment_y": 75,
#     "user.rpg_mouse_increment_x": 75,
#     "user.rpg_mouse_interaction_axis_y_pos": 75,
# }

# @ctx.action_class("user")
# class Actions:

@ctx_parrot_default.action_class("user")
class Actions:
    def parrot_hiss(): actions.user.parrot_mouse_drag(0)
    def parrot_hiss_stop(): actions.user.parrot_mouse_stop()
    def parrot_shush(): actions.user.parrot_set_modifier('alt')
    def parrot_shush_stop(): actions.skip()
