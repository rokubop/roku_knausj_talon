from talon import Module, actions, ctrl

mod = Module()

@mod.action_class
class Actions:
    def flex_mouse_primary_click():
        """Flex - primary click"""
        ctrl.mouse_click(button=0, hold=16000)
        actions.user.on_mouse_click()

    def on_mouse_click():
        """Flex - Event triggered on click"""
        pass
