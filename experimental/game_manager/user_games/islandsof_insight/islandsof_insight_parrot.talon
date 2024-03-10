app: islandsof_insight
mode: user.parrot_v5
and mode: user.islandsof_insight_parrot
-
<phrase>:                   skip()
parrot(eh):                 user.game_v2_move_dir("w")
parrot(guh):                user.game_v2_move_dir("s")
parrot(ee):                 user.game_v2_stop_layer_by_layer()
parrot(ah):                 user.event_mouse_nav("left")
parrot(oh):                 user.event_mouse_nav("right")
parrot(hiss):               user.event_mouse_dash("left")
parrot(hiss:stop):          user.event_mouse_move_stop_soft()
parrot(shush):              user.event_mouse_dash("right")
parrot(shush:stop):         user.event_mouse_move_stop_soft()
parrot(palate_click):       user.repeat()
parrot(tut):                user.game_v2_reset_center_y()
parrot(er):                 user.islandsof_insight_nav_mode_enable()
parrot(nn):                 user.event_mouse_click()
parrot(t):                  key("shift")
parrot(pop):                user.game_v2_look_down_toggle()
