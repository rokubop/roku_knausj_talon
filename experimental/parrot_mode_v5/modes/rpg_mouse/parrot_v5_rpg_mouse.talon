mode: user.parrot_v5
and mode: user.parrot_v5_rpg_mouse
-
parrot(cluck):              user.parrot_v5_mode_disable()
parrot(nn):                 user.parrot_v5_click_primary()
parrot(pop):
    user.parrot_v5_click_primary()
    user.parrot_v5_mode_disable()
# todo: migrate to a v5 pattern
parrot(ah):                 user.rpg_mouse_move_left()
parrot(oh):                 user.rpg_mouse_move_right()
parrot(hiss):               user.rpg_mouse_move_down()
parrot(shush):              user.rpg_mouse_move_up()
parrot(palate_click):       user.rpg_mouse_repeat_dir_by_increment()
parrot(tut):                user.rpg_mouse_repeat_reverse_dir_by_increment()
parrot(ee):                 user.rpg_mouse_stop()
parrot(t):                  user.rpg_mouse_move_slow()
parrot(guh):                user.rpg_mouse_move_fast()
parrot(eh):
    user.rpg_mouse_stop()
    user.parrot_v5_mode_enable("user.parrot_v5_default")
    user.parrot_v5_positioner()
parrot(er):
    user.rpg_mouse_stop()
    user.parrot_v5_mode_switch("user.parrot_v5_default")
