app: bg_3
mode: user.parrot
and not mode: sleep
-
# parrot(pop):
#     user.parrot_hiss_pop_mouse_click()
parrot(hiss):               user.fps_turn_left()
parrot(hiss_stop):          user.fps_turn_left_stop()
parrot(shush):              user.fps_turn_right()
parrot(shush_stop):         user.fps_turn_right_stop()
parrot(ee):
    user.fps_stop_layer()
    user.fps_turn_halt()
# parrot(tut):
#     key(escape)
# parrot(cluck):
#     user.release_dir_keys_all()
#     user.parrot_mode_disable()
#     user.parrot_use_default_tracking()
# parrot(oh):                 user.parrot_mode_bg_fly_toggle()
# # parrot(ah):                 user.hold_dir_key_mutually_exclusive('e')
# parrot(ee):
#     user.release_dir_keys_all()
#     user.parrot_hiss_pop_mouse_stop_if_preferred()

# parrot(eh):                 user.bg_toggle_highlight()
# parrot(t):                  mouse_click(1)
# parrot(guh):                skip()
