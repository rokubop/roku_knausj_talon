app: octopath_traveler2
-
tag(): user.game_basic_movement_arrows
tag(): user.game_arrow_keys_toggle_wsad_movement

# go up: key(w:down)
up stop:                    key(w:up)
# go down: key(s:down)
# down stop: key(s:up)
stop:                       key(w:up s:up a:up d:up)

# [user.game_directions]:
go up:
    user.game_movement_toggle_direction_switch("w")
go down:
    user.game_movement_toggle_direction_switch("s")
go left:
    user.game_movement_toggle_direction_switch("a")
go right:
    user.game_movement_toggle_direction_switch("d")
[movement] [direction] [switch] {user.game_directions}:
    user.switch_game_movement_direction(game_directions)
move:
    user.switch_game_movement(1)
freeze:
    user.switch_game_movement(0)
