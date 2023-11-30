from talon import Module, Context, actions
mod = Module()
ctx = Context()
ctx_parrot = Context()
ctx_parrot_default = Context()

mod.apps.f_l_studio = r"""
app.exe: FL64.exe
"""

ctx.matches = r"""
app: f_l_studio
"""

ctx_parrot.matches = r"""
app: f_l_studio
mode: user.parrot
"""

ctx_parrot_default.matches = r"""
app: f_l_studio
tag: user.parrot_default_interactive
"""

# ctx_parrot.settings = {
#     "user.rpg_mouse_increment_y": 75,
#     "user.rpg_mouse_increment_x": 75,
#     "user.rpg_mouse_interaction_axis_y_pos": 75,
# }

# @ctx.action_class("user")
# class Actions:

# @ctx_parrot_default.action_class("user")
# class Actions:
#     def parrot_palate():
#         actions.key("space")
