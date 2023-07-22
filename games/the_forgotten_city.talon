app: the_forgotten_city
and mode: user.game
and not mode: sleep
-
settings():
    # key_hold = 64.0
    # key_wait = 16.0
    # user.mouse_hold = 64000
    # user.mouse_wait = 0
    user.game_turn_around_mouse_delta = 1617
    user.game_turn_horizontally_mouse_delta = 300
    user.game_turn_vertically_mouse_delta = 100
# settings():

    # user.game_noise_pop_binding_default = "move"
    # user.game_noise_hiss_binding_default = "jump"
    # user.game_sprint_hold_to_walk = False
    # user.game_sprint_state_default = False

# tag(): user.game_action_rpg
tag(): user.wsad_game_controls
tag(): user.first_person_game_controls

# alphabet
fine:                       key(f)
each:                       key(e)

exam | examine:
    mouse_drag(1)
exam stop:
    mouse_release(1)
track:                      tracking.control_toggle()
swap:
    key(alt:down)
    key(tab)
    sleep(50ms)
    key(alt:up)
