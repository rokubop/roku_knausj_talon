app: blender
mode: user.parrot
and not mode: sleep
-
# settings()
    # speech.timeout = 0.15

parrot(oh): mouse_drag(2)
parrot(ee):
    mouse_release(0)
    mouse_release(2)
# parrot(tut): mouse_click(1)
# parrot(eh): user.parrot_mouse_nav_mode_enable()