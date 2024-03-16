app: hi_fi_rush
mode: user.parrot_v5
and mode: user.hi_fi_rush_peppermint
-
parrot(cluck):
    user.rpg_mouse_stop()
    user.clear_screen_regions()
    key(alt)
    user.parrot_v5_mode_disable()
parrot(nn):
    user.rpg_mouse_stop()
    user.mouse_click()
parrot(pop):
    user.rpg_mouse_stop()
    user.mouse_click()
    user.clear_screen_regions()
    key(alt)
    user.parrot_v5_mode_enable("user.hi_fi_rush_parrot")
parrot(ah):                 user.rpg_mouse_move_left()
parrot(oh):                 user.rpg_mouse_move_right()
parrot(hiss):               user.rpg_mouse_move_down()
parrot(shush):              user.rpg_mouse_move_up()
parrot(palate):             user.rpg_mouse_repeat_dir_by_increment()
parrot(tut):                user.rpg_mouse_repeat_reverse_dir_by_increment()
parrot(ee):                 user.rpg_mouse_stop()
parrot(t):                  user.rpg_mouse_move_slow()
parrot(guh):                user.rpg_mouse_move_fast()
parrot(er):
    user.rpg_mouse_stop()
    user.clear_screen_regions()
    key(alt)
    user.parrot_v5_mode_enable("user.hi_fi_rush_parrot")
