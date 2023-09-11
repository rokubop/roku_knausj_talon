app: bg_3
mode: user.parrot
and not mode: sleep
tag: user.parrot_bg_cam_movement
-
parrot(pop): user.parrot_omega_mouse()
parrot(cluck):
    user.release_dir_keys_all()
    user.disable_parrot_bg_cam_movement()
    user.parrot_use_default_tracking()
parrot(ah): user.hold_dir_key_mutually_exclusive('a')
parrot(oh): user.hold_dir_key_mutually_exclusive('d')
parrot(shush): user.hold_dir_key_mutually_exclusive('s')
parrot(hiss:stop): print("shush stop")
parrot(hiss): user.hold_dir_key_mutually_exclusive('w')
parrot(shush:stop): print("hiss stop")
parrot(er): user.hold_dir_key_mutually_exclusive('q')
parrot(eh): user.hold_dir_key_mutually_exclusive('e')
parrot(ee):
    user.release_dir_keys_all()
    user.parrot_freeze_mouse()
parrot(nn): user.bg_zoom_tag_enable()
parrot(tut): key(home)
