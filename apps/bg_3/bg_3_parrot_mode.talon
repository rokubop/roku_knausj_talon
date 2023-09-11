app: bg_3
mode: user.parrot
and not mode: sleep
-
parrot(eh):
    user.parrot_hiss_pop_mouse_disable()
    user.enable_parrot_bg_cam_movement()
# parrot(shush): user.parrot_scroll_down()
# parrot(shush:stop): user.parrot_scroll_stop_soft()
# parrot(hiss): user.parrot_scroll_up()
# parrot(hiss:stop): user.parrot_scroll_stop_soft()
parrot(tut): key(escape)
# parrot(nn): user.parrot_use_head_tracking_only()
# parrot(palate_click): user.enable_parrot_bg_cam_movement()
parrot(guh): tracking.control_toggle()
parrot(pop): user.parrot_hiss_pop_mouse_click()
parrot(hiss): user.parrot_hiss_pop_mouse_and_scroll_start()
parrot(hiss:stop): user.parrot_hiss_pop_mouse_and_scroll_stop_soft()
parrot(ee):
    user.parrot_mouse_and_scroll_stop()
    user.parrot_hiss_pop_mouse_halt_no_click()
parrot(shush): user.parrot_hiss_pop_mouse_set_default_tracking()