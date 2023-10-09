from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_default", desc="Tag for default parrot mode")
ctx.matches = "tag: user.parrot_default"

# @ctx.action_class("user")
# class ParrotSettings:
#     def parrot_mode_color(): return "white"
#     def parrot_mode_on_enable(): actions.user.parrot_default_enable()
#     def parrot_mode_on_disable(): actions.user.parrot_default_disable()

@ctx.action_class("user")
class ParrotCommands:

    # nn -> cluck -> parrot command to set
    def parrot_cluck(): actions.user.parrot_mode_disable()

    # settable to click, double click, right click,
    # set pop - flex
    def parrot_pop(): actions.user.parrot_mouse_click(0)

    # set with nn
    # otherwise repeat
    # set palette - flex
    def parrot_palate(): actions.core.repeat_phrase()

    def parrot_ah(): actions.user.parrot_mouse_drag(0)
    # set oh
    def parrot_oh(): actions.user.parrot_mouse_drag(2)

    # set with nn
    # otherwise toggle tool
    # set trap
    def parrot_t(): actions.user.kingfisher_parrot_trigger_virtual_key()

    def parrot_nn():
        actions.user.parrot_activate_special_briefly()
        actions.user.parrot_set_modifier('shift')
        # actions.user.parrot_side_b_enable()

    # set with nn
    # otherwise position
    def parrot_eh(): actions.user.parrot_position_mode_enable()

    def parrot_ee(): actions.user.parrot_mouse_and_scroll_stop()

    # set with nn
    # flex
    def parrot_guh(): actions.user.parrot_run_flex_macro()

    # settable
    # flex
    def parrot_tut(): actions.user.parrot_mouse_click(1)

    # something with nn
    def parrot_er(): actions.user.parrot_mouse_rpg_mode_enable()

    def parrot_hiss(): actions.user.parrot_scroll_down()
    def parrot_hiss_stop(): actions.user.parrot_scroll_stop_soft()
    def parrot_shush(): actions.user.parrot_scroll_up()
    def parrot_shush_stop(): actions.user.parrot_scroll_stop_soft()
