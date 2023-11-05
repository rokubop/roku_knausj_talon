from talon import Module, Context, actions
mod = Module()
ctx = Context()
ctx_parrot = Context()
ctx_parrot_default = Context()
ctx_parrot_side_b = Context()

mod.apps.the_forgotten_city = r"""
app.exe: ModernStoryteller01-Win64-Shipping.exe
"""

ctx.matches = r"""
app: the_forgotten_city
"""

ctx_parrot.matches = r"""
app: the_forgotten_city
mode: user.parrot
"""

ctx_parrot_default.matches = r"""
app: the_forgotten_city
tag: user.parrot_default
"""

ctx_parrot_side_b.matches = r"""
app: the_forgotten_city
tag: user.parrot_side_b
"""

# ctx_parrot.settings = {
#     "user.rpg_mouse_increment_y": 75,
#     "user.rpg_mouse_increment_x": 75,
#     "user.rpg_mouse_interaction_axis_y_pos": 75,
# }

ctx.settings = {
    "key_hold": 64.0,
    "key_wait": 16.0,
}

# @ctx.action_class("user")
# class Actions:

@ctx_parrot_default.action_class("user")
class Actions:
    def parrot_hiss(): actions.user.hold_dir_key_mutually_exclusive('w')
    def parrot_hiss_stop(): pass
    def parrot_shush(): actions.key("space")
    def parrot_shush_stop(): pass
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    def parrot_ee():
        actions.user.fps_stop_layer()
        actions.key("shift:up")
        actions.key("ctrl:up")
    def parrot_guh(): actions.key("shift:down")

@ctx_parrot_side_b.action_class("user")
class Actions:
    def parrot_hiss(): actions.user.hold_dir_key_mutually_exclusive('w')
    def parrot_hiss_stop(): pass
    def parrot_shush(): actions.user.hold_dir_key_mutually_exclusive('s')
    def parrot_shush_stop(): pass
    def parrot_ah():
        actions.user.mouse_move_native_stop()
        actions.user.hold_dir_key_mutually_exclusive('a')
    def parrot_oh():
        actions.user.mouse_move_native_stop()
        actions.user.hold_dir_key_mutually_exclusive('d')
    def parrot_guh(): actions.key("ctrl:down")

# @ctx_parrot_side_b.action_class("user")
# class Actions:
#     def parrot_hiss(): actions.user.mouse_move_native_up()
#     def parrot_hiss_stop(): pass
#     def parrot_shush(): actions.user.mouse_move_native_down()
#     def parrot_shush_stop(): pass
#     def parrot_ah():
#         actions.user.mouse_move_native_stop()
#         actions.user.hold_dir_key_mutually_exclusive('a')
#     def parrot_oh():
#         actions.user.mouse_move_native_stop()
#         actions.user.hold_dir_key_mutually_exclusive('d')
#     def parrot_ee():
#         actions.user.fps_stop_layer()
#     # def parrot_eh():
#     #     actions.user.mouse_move_native_stop()
#     #     actions.user.hold_dir_key_mutually_exclusive('a')
#     # def parrot_er():
#     #     actions.user.mouse_move_native_stop()
#     #     actions.user.hold_dir_key_mutually_exclusive('d')
