mode: user.parrot
and not mode: sleep
-
parrot(pop):
    user.parrot_mouse_click(0)
parrot(palate_click):
    user.parrot_mouse_click(1)
parrot(cluck):
    user.parrot_mouse_click(0, 2)
parrot(ah):
    user.parrot_mouse_drag(0)
parrot(oh):
    user.parrot_mouse_drag(1)
parrot(jj):
    user.parrot_mouse_drag(2)
parrot(hiss):
    user.parrot_scroll_down()
parrot(shush):
    user.parrot_scroll_up()
parrot(ee):
    user.parrot_mouse_and_scroll_stop()
parrot(guh):
    user.parrot_set_modifier('ctrl')
parrot(nn):
    user.parrot_set_modifier('shift')
parrot(eh):
    user.parrot_set_modifier('alt')
parrot(tut):
    user.parrot_cancel_modifiers()
    key(ctrl-z)
parrot(er):
    user.parrot_mode_disable()
    # user.parrot_trigger_virtual_key()
