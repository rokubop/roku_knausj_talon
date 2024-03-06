mode: user.parrot_v5
and mode: user.parrot_v5_default
-
settings():
    user.event_mouse_scroll_speed = 0.8

parrot(cluck):              user.parrot_v5_mode_disable()
parrot(nn):                 user.parrot_v5_click_primary()
parrot(pop):
    user.parrot_v5_click_primary()
    user.parrot_v5_mode_disable()
parrot(palate_click):       core.repeat_phrase()
parrot(ah):                 user.parrot_v5_drag_primary()
parrot(oh):                 user.parrot_v5_click_alternate()
parrot(ee):                 user.parrot_v5_stopper()
parrot(eh):                 user.parrot_v5_positioner()
parrot(er):                 user.parrot_v5_mode_b_enable()
parrot(t):                  user.parrot_v5_set_modifier('shift')
parrot(guh):                user.parrot_v5_set_modifier('ctrl')
parrot(tut):                user.parrot_v5_set_modifier('alt')
parrot(hiss):               user.parrot_v5_scroller_down()
parrot(hiss:stop):          user.parrot_v5_scroller_stop()
parrot(shush):              user.parrot_v5_scroller_up()
parrot(shush:stop):         user.parrot_v5_scroller_stop()

spot (mid | five):          user.mouse_move_center_active_window()
spot bar:                   user.mouse_move_relative_window(190, 338)
spot ledge:                 user.mouse_move_relative_window(28, 478)
spot ridge:                 user.mouse_move_relative_window(1911, 487)
spot (term | base):         user.mouse_move_relative_window(924, 939)
spot (left | one):          user.mouse_move_relative_window(709, 419)
spot (right | two):         user.mouse_move_relative_window(1293, 468)
spot rack:                  user.mouse_move_relative_window(1717, 459)
