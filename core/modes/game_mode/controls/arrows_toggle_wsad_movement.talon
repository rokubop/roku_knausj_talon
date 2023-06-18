tag: user.game_arrow_keys_toggle_wsad_movement
and mode: user.game
-
tag(): user.wsad_game_controls

key(up):
    user.game_movement_toggle_direction_switch("w")
key(down):
    user.game_movement_toggle_direction_switch("s")
key(left):
    user.game_movement_toggle_direction_switch("a")
key(right):
    user.game_movement_toggle_direction_switch("d")