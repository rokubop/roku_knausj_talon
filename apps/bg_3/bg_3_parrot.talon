app: bg_3
mode: user.parrot
and not mode: sleep
-
parrot(pop):                user.parrot_hiss_pop_mouse_click()
parrot(hiss):               user.parrot_hiss_pop_mouse_and_scroll_start()
parrot(hiss:stop):          user.parrot_hiss_pop_mouse_and_scroll_stop_soft()
parrot(shush):              user.parrot_hiss_pop_mouse_set_default_tracking()
parrot(tut):                key(escape)
parrot(cluck):
    user.release_dir_keys_all()
    user.parrot_mode_disable()
    user.parrot_use_default_tracking()
parrot(oh):                 user.hold_dir_key_mutually_exclusive('q')
parrot(ah):                 user.hold_dir_key_mutually_exclusive('e')
parrot(ee):
    user.release_dir_keys_all()
    user.parrot_hiss_pop_mouse_stop_if_preferred()

parrot(eh):                 skip()
parrot(t):                  skip()
parrot(guh):                skip()
