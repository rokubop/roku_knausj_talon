from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_pan", desc="Tag for pan parrot mode")

ctx.matches = r"""
tag: user.parrot_pan
"""

@ctx.action_class("user")
class ParrotCommands:
    def parrot_cluck():
        # actions.user.parrot_mouse_rpg_stop()
        actions.user.parrot_pan_mode_disable()
        actions.user.parrot_mode_disable()
    def parrot_ah():
        actions.user.parrot_mouse_stop()
        actions.user.parrot_mouse_drag(1)
        # actions.user.parrot_mouse_rpg_move_left()
    def parrot_oh():
        actions.user.parrot_mouse_stop()
        actions.user.parrot_mouse_drag(2)
        # actions.user.parrot_mouse_rpg_move_right()
    def parrot_hiss():
        actions.user.parrot_mouse_stop()
        actions.user.parrot_scroll_down()
    def parrot_hiss_stop(): actions.user.parrot_scroll_stop_soft()
    def parrot_shush():
        actions.user.parrot_mouse_stop()
        actions.user.parrot_scroll_up()
    def parrot_shush_stop(): actions.user.parrot_scroll_stop_soft()
    def parrot_er():
        # actions.user.parrot_mouse_stop()
        actions.user.parrot_mouse_and_scroll_stop()
        actions.user.parrot_pan_mode_disable()
    # def parrot_ee():
    #     # actions.user.parrot_mouse_rpg_stop()
    #     actions.next()


@mod.action_class
class Actions:
    def parrot_pan_mode_enable():
        """Enable parrot pan mode"""
        print("parrot pan mode enabled")
        actions.user.parrot_mode_append_tag("user.parrot_pan")
        actions.user.parrot_mouse_drag(2)
        # actions.user.parrot_teleport_mouse_soft()
        if actions.user.parrot_mode_has_tag("user.parrot_side_b"):
            actions.user.add_color_cursor("FD6A02")
        else:
            actions.user.add_color_cursor("FFA500")
            # actions.user.add_green_cursor()

    def parrot_pan_mode_disable():
        """Disable parrot pan mode"""
        print("parrot pan mode disable")
        actions.user.parrot_mouse_stop()
        actions.user.clear_screen_regions()
        actions.user.parrot_scroll_stop_soft()
        actions.user.add_red_cursor()
        actions.user.parrot_mode_reset_tags()