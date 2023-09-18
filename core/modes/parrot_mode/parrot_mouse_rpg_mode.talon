mode: user.parrot_mouse_rpg
and not mode: user.parrot
and not mode: sleep
-
settings():
    user.parrot_rpg_increment_x = 26
    user.parrot_rpg_increment_y = 26

parrot(cluck): user.parrot_mouse_rpg_mode_disable()

parrot(pop):
    user.parrot_mouse_rpg_stop()
    user.mouse_click()

parrot(ah): user.parrot_mouse_rpg_move_left()
parrot(oh): user.parrot_mouse_rpg_move_right()
parrot(hiss): user.parrot_mouse_rpg_move_down()
parrot(shush): user.parrot_mouse_rpg_move_up()

parrot(palate_click): user.parrot_mouse_rpg_repeat_dir_by_increment()
parrot(tut): user.parrot_mouse_rpg_repeat_reverse_dir_by_increment()

parrot(ee): user.parrot_mouse_rpg_stop()
parrot(eh):
    user.parrot_mouse_rpg_mode_disable()
    user.parrot_mode_enable()
    user.parrot_teleport_mouse_soft()
parrot(nn): user.parrot_mouse_rpg_move_slow()
parrot(guh): user.parrot_mouse_rpg_move_fast()

parrot(er):print("er")