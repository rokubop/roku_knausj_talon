from talon import Module, ui, actions, scope, app

mod = Module()

game_list = [
    "The Forgotten City",
]

def game_reset_actions():
    # actions.user.game_sprint_state_reset()
    actions.user.game_movement_state_reset()
    actions.user.release_held_game_keys()
    # actions.user.game_noise_control_reset()
    # _nullify_current_movement_direction_key()
    actions.user.release_held_game_keys()
    # actions.user.game_sprint_state_reset()
    actions.user.game_movement_state_reset()
    # print("this stuff was called")

def on_app_switch(application):
    global game_reset_actions;
    # print(f"App [{application.name}] triggered.")
    modes = scope.get("mode")
    if modes is None:
        return
    # if "sleep" in modes:
    #     return

    # automatically activate game mode for games
    if application.name in game_list:
        if "user.game" not in modes:
            actions.mode.disable("command")
            game_reset_actions()
            actions.mode.enable("user.game")
            # app.notify(f"App [{application.name}] triggered game mode.")
            # print(f"Command to game mode")

    # automatically deactivate game mode for other applications
    else:
        if "user.game" in modes:
            game_reset_actions()
            actions.mode.disable("user.game")
            actions.mode.disable("sleep")
            actions.mode.disable("dictation")
            actions.mode.enable("command")
            # app.notify(f"App [{application.name}] triggered command mode.")
            # print(f"Game to command mode")

ui.register("app_activate", on_app_switch)