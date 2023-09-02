mode: user.parrot
and not mode: sleep
-
settings():
    user.scroll_speed_multiplier = 0.6

parrot(cluck): user.parrot_mode_disable()

parrot(pop):
    user.parrot_mouse_click(0)
    user.parrot_mouse_click(0)
parrot(palate_click): core.repeat_phrase()
    # user.parrot_mouse_click(1)
parrot(er): user.parrot_mouse_click(0, 2)

parrot(ah): user.parrot_mouse_drag(0)
# parrot(oh): user.parrot_zoom()
    # user.parrot_mouse_drag(1)
# parrot(jj): user.parrot_mouse_drag(2)

parrot(ee): user.parrot_mouse_and_scroll_stop()

parrot(guh): user.parrot_track_toggle()
# parrot(tut): user.parrot_track_toggle()

# parrot(guh): user.parrot_set_modifier('ctrl')
# parrot(nn): user.parrot_set_modifier('shift')

parrot(nn): user.parrot_mouse_rpg_mode_enable()
    # user.parrot_trigger_virtual_key()

parrot(hiss): user.parrot_scroll_down()
parrot(hiss:stop): user.parrot_scroll_stop_soft()
parrot(shush): user.parrot_scroll_up()
parrot(shush:stop): user.parrot_scroll_stop_soft()