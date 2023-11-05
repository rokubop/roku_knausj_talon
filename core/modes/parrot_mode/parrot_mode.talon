mode: user.parrot
and not mode: sleep
-
settings():
    user.scroll_speed_multiplier = 0.6

^<phrase>: skip()
parrot(pop): user.parrot_mode_pop()
parrot(cluck): user.parrot_mode_cluck()
parrot(palate_click): user.parrot_mode_palate()
parrot(ah): user.parrot_mode_ah()
parrot(oh): user.parrot_mode_oh()
parrot(ee): user.parrot_mode_ee()
parrot(eh): user.parrot_mode_eh()
parrot(er): user.parrot_mode_er()
parrot(guh): user.parrot_mode_guh()
parrot(nn): user.parrot_mode_nn()
parrot(t): user.parrot_mode_t()
parrot(tut): user.parrot_mode_tut()
parrot(hiss): user.parrot_mode_hiss()
parrot(hiss:stop): user.parrot_mode_hiss_stop()
parrot(shush): user.parrot_mode_shush()
parrot(shush:stop): user.parrot_mode_shush_stop()