from talon import Module, actions
# from user.talon_hud.content.programming_language_poller import (
#     remove_statusbar_programming_icon,)

# from .GameModeHelper import GameModeHelper

game_mode_module = Module()
game_mode_module.mode("game", "Gaming Mode that doesn't accept regular commands")


@game_mode_module.action_class
class GameModeActions:

    def enable_game_mode():
        """Switches the game mode on"""
        # remove_statusbar_programming_icon()
        actions.mode.enable("user.game")
        # GameModeHelper.add_active_game_icon()

    def disable_game_mode():
        """Switches the game mode off"""
        actions.user.release_held_game_keys()
        # actions.user.game_sprint_state_reset()
        # GameModeHelper.game_hud_remove_icons()
        actions.user.game_movement_state_reset()
        actions.mode.disable("user.game")