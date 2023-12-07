from talon import Module, ui, actions, scope, app

mod = Module()

game_list = [
    "The Forgotten City",
    "Unity playback engine.",
    "Planet of Lana"
]

def game_reset_actions():
    actions.user.game_sprint_state_reset()
    actions.user.game_movement_state_reset()
    actions.user.release_held_game_keys()
    actions.user.game_noise_control_reset()

# def on_app_switch(application):
#     global game_reset_actions;
#     modes = scope.get("mode")
#     if modes is None:
#         return

#     # automatically activate game mode for games
#     if application.name in game_list:
#         if "user.game" not in modes:
#             actions.mode.disable("command")
#             game_reset_actions()
#             actions.mode.enable("user.game")

#     # automatically deactivate game mode for other applications
#     else:
#         if "user.game" in modes:
#             game_reset_actions()
#             actions.mode.disable("user.game")
#             actions.mode.disable("sleep")
#             actions.mode.disable("dictation")
#             actions.mode.enable("command")

# ui.register("app_activate", on_app_switch)