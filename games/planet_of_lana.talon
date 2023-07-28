win.title: Planet of Lana
and mode: user.game
-
settings():
    # user.game_noise_hiss_binding_default = "jump"

tag(): user.game_side_scroller

# user alphabet
fine:                       key(f)
each:                       key(e)
scrape:                     key(escape)
air:                        key(a)
drum:                       key(d)

# custom commands
parrot(shush):              key(left)
parrot(hiss):               key(right)
parrot(pop):
    # this needs to be able to start or go
    key(right:up)
    key(left:up)
right:                      key(right)
left:                       key(left)
up | down:                  user.game_crouch()
