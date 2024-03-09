from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def islandsof_insight_nav_mode_enable():
        """Enable nav mode"""
        actions.user.game_v2_canvas_box_color("FCD12A")
        actions.user.game_v2_canvas_status_update("mode", "nav")
        actions.mode.enable("user.game_v2_nav_mode")

    def islandsof_insight_nav_mode_disable():
        """Disable nav mode"""
        actions.mode.disable("user.game_v2_nav_mode")
        actions.user.event_mouse_move_stop_hard()
        actions.user.game_v2_talos_2_game_parrot_mode_enable()