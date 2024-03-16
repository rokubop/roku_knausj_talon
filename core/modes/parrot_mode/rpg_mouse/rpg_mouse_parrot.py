from talon import Module, Context, actions, ctrl, cron, settings

mod = Module()
ctx = Context()
ctx_v5 = Context()

mod.tag("rpg_mouse", desc="Tag for the RPG mode of parrot")
mod.mode("rpg_mouse", desc="Mode for the RPG mode of parrot")
ctx.matches = """
mode: user.parrot
tag: user.rpg_mouse
"""

@ctx.action_class("user")
class ParrotCommands:
    def parrot_cluck(): actions.user.parrot_rpg_mouse_mode_disable_full()
    def parrot_nn():
        actions.user.rpg_mouse_stop()
        actions.user.mouse_click()
    def parrot_pop():
        actions.user.rpg_mouse_stop()
        actions.user.mouse_click()
        actions.user.parrot_rpg_mouse_mode_disable_full()
    def parrot_ah(): actions.user.rpg_mouse_move_left()
    def parrot_oh(): actions.user.rpg_mouse_move_right()
    def parrot_hiss(): actions.user.rpg_mouse_move_down()
    def parrot_shush(): actions.user.rpg_mouse_move_up()
    def parrot_palate(): actions.user.rpg_mouse_repeat_dir_by_increment()
    def parrot_tut(): actions.user.rpg_mouse_repeat_reverse_dir_by_increment()
    def parrot_ee(): actions.user.rpg_mouse_stop()
    def parrot_eh():
        actions.user.parrot_rpg_mouse_mode_disable()
        actions.user.parrot_mode_enable()
        actions.user.parrot_teleport_mouse_soft()
    def parrot_t(): actions.user.rpg_mouse_move_slow()
    def parrot_guh(): actions.user.rpg_mouse_move_fast()
    def parrot_er(): actions.user.parrot_rpg_mouse_mode_disable()

ctx_v5.matches = """
mode: user.parrot_v5
and mode: user.rpg_mouse
"""

@ctx_v5.action_class("user")
class Events:
    def on_parrot_v5_mode_enable(ev: dict):
        actions.user.parrot_v5_ui_cursor_yellow()

    def on_parrot_v5_mode_disable(ev: dict):
        actions.user.rpg_mouse_stop()
        actions.user.rpg_mouse_reset_speed()

        if not ev.get("transition", False):
            actions.user.parrot_v5_ui_clear()

#     def parrot_cluck():
#         actions.user.rpg_mouse_stop()
#         actions.user.clear_screen_regions()
#         # update_speed(speed_default)
#         # actions.user.parrot_mode_reset_tags()
#         actions.user.parrot_v5_mode_disable()
#         # actions.user.parrot_mode_disable()
#     def parrot_nn():
#         actions.user.rpg_mouse_stop()
#         actions.user.mouse_click()
#     def parrot_pop():
#         actions.user.rpg_mouse_stop()
#         actions.user.mouse_click()
#         actions.user.parrot_rpg_mouse_mode_disable_full()
#     def parrot_ah(): actions.user.rpg_mouse_move_left()
#     def parrot_oh(): actions.user.rpg_mouse_move_right()
#     def parrot_hiss(): actions.user.rpg_mouse_move_down()
#     def parrot_shush(): actions.user.rpg_mouse_move_up()
#     def parrot_palate(): actions.user.rpg_mouse_repeat_dir_by_increment()
#     def parrot_tut(): actions.user.rpg_mouse_repeat_reverse_dir_by_increment()
#     def parrot_ee(): actions.user.rpg_mouse_stop()
#     def parrot_eh():
#         actions.user.parrot_rpg_mouse_mode_disable()
#         actions.user.parrot_mode_enable()
#         actions.user.parrot_teleport_mouse_soft()
#     def parrot_t(): actions.user.rpg_mouse_move_slow()
#     def parrot_guh(): actions.user.rpg_mouse_move_fast()
#     def parrot_er(): actions.user.parrot_rpg_mouse_mode_disable()