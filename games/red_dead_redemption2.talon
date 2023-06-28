app: rdr2
and mode: user.game
and not mode: sleep
-
settings():
    user.game_turn_around_mouse_delta = 2850
    user.game_turn_horizontally_mouse_delta = 600
    user.game_turn_vertically_mouse_delta = 600
    # user.game_noise_pop_binding_default = "move"
    # user.game_noise_hiss_binding_default = "jump"
    # user.game_sprint_hold_to_walk = False
    # user.game_sprint_state_default = False

tag(): user.game_action_rpg

<user.key>:                 key(key)
[go] (fast | faster) | run:
    user.switch_game_movement(0)
    key(w)
    user.switch_game_movement(1)
[go] (slow | slower) | walk:
    user.switch_game_movement(0)
    user.switch_game_movement(1)
long (<user.key>):          user.hold_game_key(key, "700ms")
hold (<user.key>):          user.hold_game_key(key)
horse go:                   user.rdr_horse_run()
horse stop:                 user.rdr_horse_stop()
^retry$:                    user.hold_game_key("enter", "2000ms")
(release | real | don't) (<user.key>): user.release_game_key(key)
(release | real | don't) all: user.release_held_game_keys()
loot:                       user.hold_game_key("r", "700ms")
skip scene:                 user.hold_game_key("space", "2s")
cancel:                     user.release_held_game_keys()
