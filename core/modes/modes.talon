not mode: sleep
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    user.gdb_disable()
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")

# ziemus_talon
^game mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("dictation")
    user.enable_game_mode()
