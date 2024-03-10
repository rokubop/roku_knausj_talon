from talon import Module, actions

mod = Module()
mod.mode("islandsof_insight_nav_mode", "Nav mode for islandsof_insight")

@mod.action_class
class Actions:
    def islandsof_insight_nav_mode_enable():
        """Enable nav mode"""
        actions.user.parrot_v5_mode_switch("user.islandsof_insight_nav_mode")

    def islandsof_insight_nav_mode_disable():
        """Disable nav mode"""
        actions.user.parrot_v5_mode_switch("user.islandsof_insight_parrot")