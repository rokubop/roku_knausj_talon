from talon import Context, actions, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
"""

@mod.action_class
class Actions:
    def window_maximize():
        """Maximize window"""
        # actions.key("alt-space");
        # actions.sleep(300ms);
        # actions.key("x");
        actions.key("win-up")

    def window_restore():
        """Restore window"""
        # actions.key("alt-space");
        # actions.sleep(300ms);
        # actions.key("r");
        actions.key("win-down")