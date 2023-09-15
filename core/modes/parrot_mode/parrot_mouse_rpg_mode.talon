mode: user.parrot_mouse_rpg
and not mode: user.parrot
and not mode: sleep
-
parrot(cluck): user.parrot_mouse_rpg_mode_disable()
parrot(pop):
    user.parrot_mouse_rpg_stop()
    user.mouse_click()
    # user.parrot_mouse_click(0)
parrot(ah): user.parrot_mouse_rpg_move_left()
parrot(oh): user.parrot_mouse_rpg_move_right()
parrot(hiss): user.parrot_mouse_rpg_move_down()
parrot(shush): user.parrot_mouse_rpg_move_up()
parrot(tut): user.parrot_mouse_rpg_move_slow()
parrot(nn): user.parrot_mouse_rpg_move_slow()
parrot(eh): user.parrot_teleport_mouse_soft()
# parrot(palate_click): user.parrot_mouse_rpg_move_fast()
parrot(er):print("er")
parrot(ee): user.parrot_mouse_rpg_stop()
parrot(guh): user.parrot_mouse_rpg_move_fast()