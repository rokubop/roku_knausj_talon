mode: user.parrot_v2
and not mode: sleep
-
parrot(pop):                user.flex_special()
parrot(nn):                 user.flex_mouse_click()
parrot(ah):                 user.flex_mouse_drag()
parrot(oh):                 user.flex_mouse_secondary()
parrot(hiss):               user.flex_scroll_down()
parrot(hiss:stop):          user.flex_scroll_down_stop()
parrot(shush):              user.flex_scroll_up()
parrot(shush:stop):         user.flex_scroll_up_stop()
parrot(ee):                 user.flex_stop()
parrot(eh):                 user.flex_position()
parrot(er):                 user.flex_alternate_mode()
parrot(palate):             user.flex_repeater()
parrot(t):
    user.flex_use_modifier('shift')
    user.flex_use_side_b_briefly()
parrot(guh):
    user.flex_use_modifier('ctrl')
    user.flex_use_side_c_briefly()
parrot(tut):
    user.flex_use_modifier('alt')
    user.flex_use_side_d_briefly()
parrot(cluck):              user.mode_disable_parrot_v2()
