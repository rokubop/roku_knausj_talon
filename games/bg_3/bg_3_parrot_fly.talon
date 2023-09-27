app: bg_3
mode: user.parrot
and not mode: sleep
tag: user.parrot_fly
-
settings():
    user.roku_persist_frozen_mouse_on_exit = false

parrot(cluck):
    print("cluck")
    user.parrot_mode_bg_fly_disable()
    user.parrot_use_default_tracking()
    user.parrot_mode_disable()
parrot(palate_click):
    print("palate")
    user.parrot_mode_bg_fly_disable()
    user.parrot_use_default_tracking()
parrot(eh): user.hold_dir_key_mutually_exclusive('a')
parrot(er): user.hold_dir_key_mutually_exclusive('d')
parrot(shush): user.hold_dir_key_mutually_exclusive('s')
parrot(hiss:stop): print("shush stop")
parrot(hiss): user.hold_dir_key_mutually_exclusive('w')
parrot(shush:stop): print("hiss stop")
parrot(oh): user.hold_dir_key_mutually_exclusive('q')
parrot(ah): user.hold_dir_key_mutually_exclusive('e')
parrot(ee): user.release_dir_keys_all()
parrot(nn): mouse_scroll(-300)
parrot(t): mouse_scroll(1000)
parrot(tut): key(home)
parrot(guh): key(o)
