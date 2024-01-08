from talon import Module, actions

mod = Module()
mod.mode("parrot_v2", "parrot mode v2")

@mod.action_class
class Actions:
    def on_ctx_enter():
        """Actions to take when entering context"""
        pass

    def on_ctx_exit():
        """Actions to take when exiting context"""
        pass

    def mode_enable_parrot_v2():
        """Enable parrot mode v2"""
        actions.mode.enable("user.parrot_v2")

    def use_parrot_mode_default():
        """Enable parrot mode v2 default"""
        actions.mode.enable("user.parrot_v2")
        actions.mode.enable("user.parrot_default_v2")
        actions.user.on_ctx_enter()

    def mode_disable_parrot_v2():
        """Disable parrot mode v2"""
        actions.user.on_ctx_exit()
        actions.mode.disable("user.parrot_v2")
        actions.mode.disable("user.parrot_default_v2")

    def flex_mouse_drag(): """Flex mouse drag"""; pass
    def flex_use_modifier(modifier: str): """Flex use modifier"""; pass
    def flex_use_side_b_briefly(): """Flex use side b briefly"""; pass
    def flex_use_side_c_briefly(): """Flex use side c briefly"""; pass
    def flex_use_side_d_briefly(): """Flex use side d briefly"""; pass