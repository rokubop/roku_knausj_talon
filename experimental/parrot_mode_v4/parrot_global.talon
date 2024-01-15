mode: user.parrot_v4_global
-
settings():
    user.parrot_v4_scroll_speed_multiplier = 0.6
    user.parrot_v4_show_cursor_color = true
    user.parrot_v4_cursor_color = "d4287e"

^<phrase>:                  skip()
parrot(cluck):              user.parrot_v4_mode_disable()
parrot(nn):                 user.parrot_v4_click_primary()
parrot(pop):
    user.parrot_v4_click_primary()
    user.parrot_v4_mode_disable()
parrot(cluck):              user.parrot_v4_mode_disable()
parrot(palate_click):       core.parrot_v4_repeater()
parrot(ah):                 user.parrot_v4_drag_primary()
parrot(oh):                 user.parrot_v4_click_alternate()
parrot(ee):                 user.parrot_v4_stopper()
parrot(eh):                 user.parrot_v4_positioner()
parrot(er):                 user.parrot_v4_mode_b_enable()
parrot(t):
    user.parrot_v4_set_modifier('shift')
    user.parrot_v4_activate_side_b_briefly()
parrot(guh):
    user.parrot_v4_set_modifier('ctrl')
    user.parrot_v4_activate_side_c_briefly()
parrot(tut):
    user.parrot_v4_set_modifier('alt')
    user.parrot_v4_activate_side_d_briefly()
parrot(hiss):               user.parrot_v4_scroller_down()
parrot(hiss:stop):          user.parrot_v4_scroller_stop()
parrot(shush):              user.parrot_v4_scroller_up()
parrot(shush:stop):         user.parrot_v4_scroller_stop()
