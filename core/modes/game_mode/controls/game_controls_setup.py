from talon import actions, ui
from .BasicMovementActions import _nullify_current_movement_direction_key
from ..GameModeHelper import GameModeHelper


def _on_app_launch_close(app):
    global current_game_movement_direction_key
    if GameModeHelper._is_game_in_library(app):
        actions.user.game_sprint_state_reset()
        actions.user.game_movement_state_reset()
        _nullify_current_movement_direction_key()
        actions.user.release_held_game_keys()
        actions.user.game_noise_control_reset()


ui.register("app_close", _on_app_launch_close)
ui.register("app_launch", _on_app_launch_close)


def on_app_activate(app):
    if GameModeHelper._is_game_in_library(app):
        actions.user.custom_game_setup()


def on_app_deactivate(deactivated_app):
    if GameModeHelper._is_game_in_library(deactivated_app):
        actions.user.custom_game_cleanup()


ui.register("app_activate", on_app_activate)
ui.register("app_deactivate", on_app_deactivate)