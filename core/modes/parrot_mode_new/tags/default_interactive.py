from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_default_interactive", desc="Tag for interactive parrot mode")
ctx.matches = "tag: user.parrot_default_interactive"

@ctx.action_class("user")
class ParrotCommands:
    def parrot_cluck(): actions.user.parrot_mode_disable()
    def parrot_pop(): actions.user.parrot_mouse_click(0)
    def parrot_palate(): actions.core.repeat_phrase()
    def parrot_ah(): actions.user.parrot_mouse_drag(0)
    def parrot_oh(): actions.user.parrot_pan_mode_enable()
    # def parrot_t(): actions.user.kingfisher_parrot_trigger_virtual_key()
    def parrot_t(): actions.user.parrot_tool_switch()
    def parrot_nn():
        actions.user.parrot_activate_side_b_briefly()
        actions.user.parrot_set_modifier('shift')
    def parrot_eh(): actions.user.parrot_position_mode_enable()
    def parrot_ee(): actions.user.parrot_mouse_and_scroll_stop()
    def parrot_guh():
        actions.user.parrot_mouse_stop()
        actions.user.parrot_mouse_drag(1)
    # def parrot_guh(): actions.user.parrot_run_flex_macro()
    def parrot_tut(): actions.user.parrot_mouse_click(1)
    def parrot_er(): actions.user.parrot_mouse_rpg_mode_enable()
    def parrot_hiss(): actions.user.parrot_set_modifier('ctrl')
    def parrot_hiss_stop(): actions.skip()
    def parrot_shush(): actions.user.parrot_set_modifier('alt')
    def parrot_shush_stop(): actions.skip()
