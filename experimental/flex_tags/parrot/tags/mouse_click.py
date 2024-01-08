from talon import Module, Context, actions

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def flex_mouse_click():
        """Flex mouse click"""
        actions.user.flex_mouse_before_click()
        actions.user.mouse_click()
        actions.user.flex_mouse_after_click()

    def flex_mouse_before_click():
        """Flex mouse before click"""
        pass

    def flex_mouse_after_click():
        """Flex mouse after click"""
        pass
