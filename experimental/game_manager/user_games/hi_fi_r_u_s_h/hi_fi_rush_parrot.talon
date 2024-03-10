app: hi_fi_rush
and mode: user.parrot_v5
and mode: user.hi_fi_rush_parrot
-
<phrase>:                   skip()
parrot(eh):                 user.game_v2_move_dir("w")
parrot(guh):                user.game_v2_move_dir("s")
parrot(ah):                 user.game_v2_move_dir("a")
parrot(oh):                 user.game_v2_move_dir("d")
parrot(ee):                 user.game_v2_stop_layer_by_layer()

parrot(hiss):               key(r)
parrot(shush):              key(space)
parrot(palate_click):       key(q)
parrot(tut):                user.game_v2_reset_center_y()
parrot(cluck):              user.event_mouse_click(1)
parrot(pop):                user.event_mouse_click(0)
parrot(er):                 user.parrot_v5_mode_disable()
parrot(nn):                 key(e)
parrot(t):                  key(shift)
