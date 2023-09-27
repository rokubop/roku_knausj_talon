app: genshin_impact
mode: user.parrot
and tag: user.genshin_melee
and not mode: sleep
-
parrot(cluck):
    user.genshin_stop_layer()
    user.genshin_stop_layer()
    user.genshin_stop_fight()
    user.genshin_fight_mode_disable()
    user.parrot_mode_disable()

# movement
parrot(palate_click):
    user.genshin_stop_layer()
    user.genshin_stop_layer()
    user.genshin_stop_fight()
    user.genshin_fight_mode_disable()

parrot(hiss): user.hold_dir_key_mutually_exclusive('w')
parrot(hiss:stop): print("shush stop")
parrot(shush):
    user.genshin_stop_fight()
    user.hold_dir_key_mutually_exclusive('s')
parrot(shush:stop): print("hiss stop")
parrot(eh):
    print("eh from genshin melee")
    user.mouse_move_native_stop()
    user.hold_dir_key_mutually_exclusive('a')
parrot(er):
    user.mouse_move_native_stop()
    user.hold_dir_key_mutually_exclusive('d')
parrot(ah):
    user.mouse_move_native_left()
parrot(oh): user.mouse_move_native_right()
parrot(ee): user.genshin_stop_layer()

# combat
parrot(pop): user.genshin_toggle_fight()
parrot(nn): key(e)
parrot(guh): key(q)
parrot(tut): mouse_click(1)
# parrot(palate_click): user.genshin_repeater()