mode: user.parrot
and not mode: sleep
tag: user.parrot_tracking
-
parrot(pop):
    mouse_click()
    user.parrot_freeze_mouse()
parrot(cluck): user.parrot_tracking_mode_disable()
parrot(hiss): user.parrot_use_default_tracking()
parrot(hiss:stop): user.parrot_use_head_tracking_only()
parrot(shush): user.parrot_use_head_tracking_only()
parrot(guh): user.parrot_mouse_move_toggle()
parrot(ee): user.parrot_mouse_move_toggle()
# parrot(eh): tracking.control_toggle()
parrot(er): tracking.control_toggle()