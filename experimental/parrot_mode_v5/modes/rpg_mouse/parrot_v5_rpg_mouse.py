from talon import Module, Context, actions, settings, ctrl

mod = Module()
ctx = Context()

ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_rpg_mouse
"""

# @ctx.action_class("user")
# class Actions:
#     def parrot_v5_cluck(): actions.user.parrot_v5_mode_disable()
#     def parrot_v5_nn(): actions.user.parrot_v5_click_primary()
#     def parrot_v5_pop():
#         actions.user.parrot_v5_click_primary()
#         actions.user.parrot_v5_mode_disable()
#     def parrot_v5_ah(): actions.user.rpg_mouse_move_left()

@ctx.action_class("user")
class Events:
    def on_parrot_v5_mode_enable():
        actions.user.add_yellow_cursor()

    def on_parrot_v5_mode_disable():
        actions.user.rpg_mouse_stop()
        actions.user.rpg_mouse_reset_speed()
        actions.user.clear_screen_regions()

    def on_event_mouse_button_down():
        actions.user.rpg_mouse_stop()
