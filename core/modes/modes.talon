not mode: sleep
-
dictate [<phrase>]$:
    print("dictate")
    mode.enable("dictation")
    user.parse_phrase(phrase or "")
^dictation mode$:
    print("dictation mode")
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    user.gdb_disable()
^command mode$:
    print("command mode")
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("user.game")
    mode.enable("command")
^mixed mode$:
    mode.disable("user.game")
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
# ziemus_talon
^game mode$:
    print("game mode")
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("dictation")
    # user.game_sprint_state_reset()
    user.game_movement_state_reset()
    user.release_held_game_keys()
    # user.game_noise_control_reset()
    # _nullify_current_movement_direction_key()

    user.release_held_game_keys()
    # user.game_sprint_state_reset()
    user.game_movement_state_reset()
    mode.enable("user.game")
