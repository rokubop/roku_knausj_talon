app: the_forgotten_city
and mode: user.game
and not mode: sleep
-
settings():
    user.game_turn_around_mouse_delta = 1617
    user.game_turn_horizontally_mouse_delta = 250
    user.game_turn_vertically_mouse_delta = 100
    user.game_noise_hiss_binding_default = "jump"

tag(): user.game_action_rpg

# user alphabet
fine:                       key(f)
each:                       key(e)
scrape:                     key(escape)
air:                        key(a)
drum:                       key(d)

test:                       key(down)
# custom commands
light | flash | flashlight: key(2)
exam | examine:
    mouse_drag(1)
exam stop:
    mouse_release(1)
file save:                  key(f5)
file load:                  key(f9)
# track:                      tracking.control_toggle()

# north:                      key(up)
# south:                      key(down)
quest | journal:            key(tab)
