mode: user.parrot_mouse_rpg
and not mode: user.parrot
and not mode: sleep
-
parrot(cluck): user.parrot_mouse_rpg_mode_disable()
parrot(pop):
    user.parrot_mouse_rpg_mode_disable()
    user.parrot_mouse_click(0)
parrot(ah): user.parrot_mouse_rpg_move_left()
parrot(oh): user.parrot_mouse_rpg_move_right()
parrot(hiss): user.parrot_mouse_rpg_move_down()
parrot(shush): user.parrot_mouse_rpg_move_up()
parrot(nn): user.parrot_mouse_rpg_move_slow()
parrot(t): user.parrot_mouse_rpg_move_fast()
parrot(er):print("er")
parrot(ee): user.parrot_mouse_rpg_stop()
parrot(guh): user.parrot_mouse_rpg_move_slow()