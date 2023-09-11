mode: user.parrot
and not mode: sleep
-
settings():
    user.scroll_speed_multiplier = 0.6

parrot(cluck): user.parrot_mode_disable()
parrot(pop): user.parrot_mouse_click(0)
parrot(palate_click): core.repeat_phrase()
parrot(ah): user.parrot_mouse_drag(0)
parrot(oh): user.parrot_mouse_drag(2)
# parrot(oh): user.parrot_zoom()
parrot(t): user.parrot_set_modifier('ctrl')
parrot(nn): user.parrot_set_modifier('shift')
parrot(eh): user.parrot_hiss_pop_mouse_enable()
# parrot(eh): user.parrot_set_modifier('alt')
parrot(ee): user.parrot_mouse_and_scroll_stop()
parrot(guh): user.parrot_track_toggle()
# parrot(guh): user.parrot_mouse_move_toggle()
# parrot(guh): user.parrot_tracking_mode_enable()
parrot(tut): user.parrot_mouse_click(1)
parrot(er): user.parrot_mouse_rpg_mode_enable()
# user.parrot_trigger_virtual_key()
# change into browsing mode with mouse position snapping
# ah for left position
# oh for right position
# eh for middle position
# back button
parrot(hiss): user.parrot_scroll_down()
parrot(hiss:stop): user.parrot_scroll_stop_soft()
parrot(shush): user.parrot_scroll_up()
parrot(shush:stop): user.parrot_scroll_stop_soft()