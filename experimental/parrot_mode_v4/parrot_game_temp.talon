tag: user.parrot_game_temp
-
parrot(eh):
    user.game_v2_disable_parrot()
    user.parrot_mode_enable()
    user.parrot_position_mode_enable()
parrot(nn):                 user.game_v2_move_dir_toggle('w')
parrot(ee):                 user.game_v2_stop_layer_by_layer()
parrot(pop):                user.game_v2_move_dir_step('w')
parrot(palate):             key(space)
parrot(ah):                 user.game_v2_soft_left(15)
parrot(oh):                 user.game_v2_soft_right(15)
parrot(hiss):               actions.user.fps_turn_left()
parrot(hiss:stop):          actions.user.fps_turn_left_stop()
parrot(shush):              actions.user.fps_turn_right()
parrot(shush:stop):         actions.user.fps_turn_right_stop()
