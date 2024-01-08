from talon import Module, Context, actions, ctrl, cron, settings

mod = Module()
ctx = Context()

mod.mode("parrot_default_v2", desc="Tag for default parrot mode v2")

ctx.matches = """
mode: user.parrot_default_v2
"""

@ctx.action_class("user")
class Actions:
    def on_ctx_enter():
        actions.user.use_flex_scroller_default()
        actions.user.use_flex_mouse_secondary_default()
        actions.user.use_flex_special_default()
        actions.user.add_red_cursor()

    def on_ctx_exit():
        actions.user.clear_screen_regions()

    def flex_mouse_drag():
        ctrl.mouse_drag()

    def flex_use_modifier(modifier: str): """Flex use modifier"""; pass
    def flex_use_side_b_briefly(): """Flex use side b briefly"""; pass
    def flex_use_side_c_briefly(): """Flex use side c briefly"""; pass
    def flex_use_side_d_briefly(): """Flex use side d briefly"""; pass