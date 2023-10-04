from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_position", desc="Tag for position parrot mode")

ctx.matches = r"""
tag: user.parrot_position
"""

@ctx.action_class("user")
class ParrotCommands:
    def parrot_cluck():
        actions.user.parrot_position_mode_disable()
        actions.user.parrot_mode_disable()
    def parrot_eh(): actions.user.parrot_teleport_mouse_soft()

@mod.action_class
class Actions:
    def parrot_position_mode_enable():
        """Enable parrot position mode"""
        print("parrot position mode enabled")
        actions.user.parrot_mode_append_tag("user.parrot_position")
        actions.user.parrot_teleport_mouse_soft()
        if actions.user.parrot_mode_has_tag("user.parrot_side_b"):
            actions.user.add_color_cursor("00FFFF")
        else:
            actions.user.add_green_cursor()

    def parrot_position_mode_disable():
        """Disable parrot position mode"""
        print("parrot position mode disable")
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        actions.user.parrot_mode_reset_tags()