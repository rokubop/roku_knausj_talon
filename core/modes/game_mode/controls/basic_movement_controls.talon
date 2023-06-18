tag: user.game_basic_movement
and mode: user.game
-
[movement] [direction] [switch] {user.game_directions}:
    user.switch_game_movement_direction(game_directions)
go | move:
    user.switch_game_movement(1)
stop | freeze:
    user.switch_game_movement(0)