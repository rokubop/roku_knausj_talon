parrot(cluck):              user.parrot_v5_mode_enable()
parrot(tut):                user.on_tut()
parrot(palate_click):       user.on_palate()
parrot(pop):                user.on_pop()

parrot mode:                user.parrot_v5_mode_enable("user.parrot_v5_default")
RPG:                        user.parrot_v5_mode_enable("user.rpg_mouse")

parrot oh right [click]:    user.parrot_v5_set_click_alternate("right")
parrot oh right drag:       user.parrot_v5_set_click_alternate("right_drag")
parrot oh mid [click]:      user.parrot_v5_set_click_alternate("mid")
parrot oh mid drag:         user.parrot_v5_set_click_alternate("mid_drag")
scroll by lines:            user.event_mouse_scroll_by_lines_toggle()
