mode: user.parrot_mouse_nav
and not mode: user.parrot
and not mode: sleep
-
# settings():
#     user.scroll_speed_multiplier = 0.6

parrot(cluck):
    user.parrot_mouse_nav_mode_disable()
    user.parrot_mode_enable()

parrot(ah): user.parrot_mouse_nav_move_left()
parrot(oh): user.parrot_mouse_nav_move_right()
parrot(hiss): user.parrot_mouse_nav_move_down()
parrot(shush): user.parrot_mouse_nav_move_up()
parrot(nn): user.parrot_mouse_nav_move_slow()
parrot(er): user.parrot_mouse_nav_move_fast()
parrot(ee): user.parrot_mouse_nav_stop()
parrot(guh): user.parrot_track_toggle()
# parrot(eh): user.parrot_trigger_virtual_key()
# parrot(hiss:stop): user.parrot_scroll_stop_soft()
# parrot(shush:stop): user.parrot_scroll_stop_soft()