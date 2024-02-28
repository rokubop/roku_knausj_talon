not mode: sleep
and not mode: user.parrot
# and not mode: user.parrot_v2
# and not mode: user.parrot_v4
# and not mode: user.parrot_v4_global
# and not mode: user.parrot_v4_app
# and not tag: user.parrot_game_temp
# and not tag: user.game_v2
-
# I need to figure out why `mode: command` doesn't work
# v four:                     user.parrot_v4_mode_enable()
# parrot(cluck):              user.parrot_mode_enable()
# parrot(cluck):              user.parrot_v4_mode_enable()
parrot(tut):                user.on_tut()
parrot(palate_click):       user.on_palate()
parrot(pop):
    # user.parrot_v5_mode_enable()
    # user.parrot_v5_positioner()
    user.on_pop()
