mode: user.game_talos_2_parrot
-
# parrot(pop):                user.parrot_flex_a()

parrot(cluck):              user.game_v2_talos_2_game_parrot_mode_disable()
parrot(eh):                 user.game_v2_move_dir("w")
parrot(guh):                user.game_v2_move_dir("s")
parrot(ee):                 user.game_v2_stop_layer_by_layer()
parrot(ah):                 user.game_v2_soft_left()
parrot(oh):                 user.game_v2_soft_right()
parrot(hiss):               user.game_v2_turn_right_hold_start()
parrot(hiss:stop):          user.game_v2_turn_right_hold_release()
parrot(shush):              user.game_v2_turn_left_hold_start()
parrot(shush:stop):         user.game_v2_turn_left_hold_release()
parrot(palate):             user.repeat()
parrot(tut):                user.game_v2_reset_center_y()
parrot(nn):                 mouse_click()
parrot(t):                  user.game_v2_key_toggle_once("shift")
parrot(pop):                user.game_v2_look_down_toggle()
