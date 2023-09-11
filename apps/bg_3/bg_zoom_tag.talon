app: bg_3
mode: user.parrot
and not mode: sleep
tag: user.bg_zoom_tag
-
parrot(cluck):
    user.bg_zoom_tag_disable()
    user.disable_parrot_bg_cam_movement()
parrot(shush): user.parrot_scroll_down()
parrot(shush:stop): user.parrot_scroll_stop_soft()
parrot(hiss): user.parrot_scroll_up()
parrot(hiss:stop): user.parrot_scroll_stop_soft()
parrot(ee):
    user.release_dir_keys_all()
    user.bg_zoom_tag_disable()
parrot(nn): skip()
parrot(er): user.hold_dir_key_mutually_exclusive('q')
parrot(eh): user.hold_dir_key_mutually_exclusive('e')