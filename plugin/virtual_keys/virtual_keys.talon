
virtual keys set: user.hud_set_virtual_keyboard('example_keyboard')
virtual keys remove: user.hud_set_virtual_keyboard()
virtual keys show: user.hud_set_virtual_keyboard_visibility(1)
virtual keys hide: user.hud_set_virtual_keyboard_visibility(0)
key this: user.hud_activate_virtual_key()

dwell toolbar set: user.hud_set_dwell_toolbar('example_toolbar')
dwell toolbar remove: user.hud_set_dwell_toolbar()
dwell toolbar show: user.hud_set_dwell_toolbar_visibility(1)
dwell toolbar hide: user.hud_set_dwell_toolbar_visibility(0)
dwell this: user.hud_activate_dwell_key()
dwell clear: user.hud_deactivate_dwell_key()

yellow cursor: user.add_yellow_cursor()
red cursor: user.add_red_cursor()
split cursor: user.add_split_cursor_regions()
show example regions: user.add_example_screen_regions()
clear regions: user.clear_screen_regions()

test: user.hud_create_virtual_key()
red particle: user.hud_publish_mouse_particle('float_up', 'FF0000')
blue particle: user.hud_publish_particle('float_up', '0000FF', '', 10, 100, 100)

start counting: user.start_counting()
pause counting: user.pause_counting()
stop counting: user.stop_counting()