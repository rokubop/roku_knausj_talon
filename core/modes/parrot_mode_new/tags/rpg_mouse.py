from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_mouse_rpg", desc="Tag for the RPG mode of parrot")
ctx.matches = """
mode: user.parrot
tag: user.parrot_mouse_rpg
"""

@ctx.action_class("user")
class ParrotCommands:
    def parrot_cluck(): actions.user.parrot_mouse_rpg_mode_disable_full()
    def parrot_pop():
        actions.user.parrot_mouse_rpg_stop()
        actions.user.mouse_click()
    def parrot_ah(): actions.user.parrot_mouse_rpg_move_left()
    def parrot_oh(): actions.user.parrot_mouse_rpg_move_right()
    def parrot_hiss(): actions.user.parrot_mouse_rpg_move_down()
    def parrot_shush(): actions.user.parrot_mouse_rpg_move_up()
    def parrot_palate(): actions.user.parrot_mouse_rpg_repeat_dir_by_increment()
    def parrot_tut(): actions.user.parrot_mouse_rpg_repeat_reverse_dir_by_increment()
    def parrot_ee(): actions.user.parrot_mouse_rpg_stop()
    def parrot_eh():
        actions.user.parrot_mouse_rpg_mode_disable()
        actions.user.parrot_mode_enable()
        actions.user.parrot_teleport_mouse_soft()
    def parrot_nn(): actions.user.parrot_mouse_rpg_move_slow()
    def parrot_t(): actions.user.parrot_mouse_rpg_move_fast()
    def parrot_er(): actions.user.parrot_mouse_rpg_mode_disable()
    def parrot_guh(): actions.user.parrot_run_flex_macro()