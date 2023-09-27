app: fl studio
mode: user.parrot
os: windows
and not mode: sleep
tag: user.fl_studio_pan_mode
-
# settings():
#     user.roku_persist_frozen_mouse_on_exit = false

parrot(cluck): user.fl_studio_pan_mode_disable()
# parrot(palate_click):
parrot(eh):
    key(ctrl:down)
    user.mouse_scroll_up(5)
    key(ctrl:up)
parrot(er):
    key(ctrl:down)
    user.mouse_scroll_down(5)
    key(ctrl:up)
parrot(nn):
    key(alt:down)
    user.mouse_scroll_up(5)
    key(alt:up)
parrot(t):
    key(alt:down)
    user.mouse_scroll_down(5)
    key(alt:up)
parrot(ah): user.mouse_scroll_left(5)
parrot(oh): user.mouse_scroll_right(5)
# parrot(shush):
# parrot(hiss):
# parrot(oh):
# parrot(ah):
# parrot(ee):
# parrot(nn):
# parrot(t):
# parrot(tut):
# parrot(guh):
