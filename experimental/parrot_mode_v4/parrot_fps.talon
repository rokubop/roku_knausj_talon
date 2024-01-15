mode: user.parrot_v4_app
tag: user.parrot_v4_fps
-
settings():
    user.parrot_v4_show_cursor_color = false
    user.parrot_v4_fps_x_turn_speed = 10.0
    user.parrot_v4_fps_x_180_calibration = 3200

parrot(cluck):              user.parrot_v4_mode_disable()
parrot(nn):                 user.parrot_v4_fps_go_stop()
parrot(eh):                 user.parrot_v4_fps_menu_mode()
parrot(guh):                user.parrot_v4_fps_go_back_stop()
parrot(hiss):               user.parrot_v4_fps_turn_right()
parrot(hiss:stop):          user.parrot_v4_fps_turn_stop()
parrot(shush):              user.parrot_v4_fps_turn_left()
parrot(shush:stop):         user.parrot_v4_fps_turn_stop()
parrot(ee):                 user.parrot_v4_fps_stopper()
parrot(er):                 user.parrot_v4_fps_mode_b_enable()

parrot(ah):                 user.parrot_v4_fps_flex_a()
parrot(oh):                 user.parrot_v4_fps_flex_b()
parrot(pop):                user.parrot_v4_fps_flex_x()
parrot(palate_click):       user.parrot_v4_fps_flex_y()

parrot(t):
    user.parrot_v4_fps_toggle_sprint()
    user.parrot_v4_activate_side_b_briefly()
parrot(tut):
    user.parrot_v4_fps_reset_cam_center()
    user.parrot_v4_activate_side_c_briefly()
