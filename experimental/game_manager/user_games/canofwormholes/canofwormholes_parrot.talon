app: canofwormholes
mode: user.game_canofwormholes_parrot
-
<phrase>:                   skip()
parrot(ah):                 user.game_v2_move_dir("a")
parrot(oh):                 user.game_v2_move_dir("d")
parrot(hiss):               user.game_v2_move_dir("s")
parrot(shush):              user.game_v2_move_dir("w")
parrot(cluck):              user.game_v2_canofwormholes_game_parrot_mode_disable()

# parrot(eh):                 user.game_v2_move_dir("w")
# parrot(guh):                user.game_v2_move_dir("s")
parrot(ee):                 user.game_v2_stop_layer_by_layer()
parrot(palate_click):       user.repeat()
parrot(tut):                key(z)
parrot(er):                 user.game_v2_canofwormholes_nav_discrete_toggle()
parrot(nn):                 key(x)
parrot(pop):
    user.event_mouse_click()
    user.game_v2_canofwormholes_game_parrot_mode_disable()

# parrot(t):                  key("shift")
# parrot(pop):                user.game_v2_look_down_toggle()
