from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_position", desc="Tag for position parrot mode")

ctx.matches = r"""
tag: user.parrot_position
mode: user.parrot
"""

@ctx.action_class("user")
class ParrotCommands:
    def parrot_pop(): actions.user.parrot_mouse_click(0)
    def parrot_cluck():
        if actions.user.parrot_is_mouse_moving():
            actions.user.parrot_mouse_click(0)
        actions.user.parrot_position_mode_disable()
        actions.user.parrot_mode_disable()
    def parrot_eh(): actions.user.parrot_teleport_mouse_soft()
    def parrot_ah(): actions.user.parrot_mouse_drag(0)
    def parrot_ee(): actions.user.parrot_mouse_and_scroll_stop()
    def parrot_tut(): actions.user.parrot_mouse_click(1)
    def parrot_guh():
        actions.user.parrot_mouse_click(0)
        actions.user.parrot_mode_disable()
        # actions.user.parrot_mode_disable(preserve_tag="user.parrot_position")
    def parrot_er(): actions.user.parrot_rpg_mouse_mode_enable()
    def parrot_hiss(): actions.user.parrot_scroll_down()
    def parrot_hiss_stop(): actions.user.parrot_scroll_stop_soft()
    def parrot_shush(): actions.user.parrot_scroll_up()
    def parrot_shush_stop(): actions.user.parrot_scroll_stop_soft()


@mod.action_class
class Actions:
    def parrot_position_mode_enable():
        """Enable parrot position mode"""
        print("parrot position mode enabled")
        actions.user.parrot_teleport_mouse_soft()
        if actions.user.parrot_is_active_mouse_enabled():
            # don't enter this mode if mouse is active
            return
        actions.user.parrot_mode_append_tag("user.parrot_position")
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