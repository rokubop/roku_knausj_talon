app: octopath_traveler_2
mode: user.parrot
and not mode: sleep
-
settings():
    key_hold = 64.0
    key_wait = 16.0
#     user.mouse_hold = 64000
#     user.mouse_wait = 0

# Reserved for switching to parrot mode
# parrot(cluck)
parrot(cluck):
    user.parrot_mode_disable()
    key(a:up)
    key(d:up)
    key(s:up)
    key(w:up)

parrot(tut): key(c)
parrot(pop): user.parrot_mouse_click(0)
# parrot(palate_click): key(space)
parrot(guh): print('guh')
parrot(nn): print('nn')
parrot(eh): print('eh')
parrot(er): print('er')
parrot(ah):
    print('ah')
    key(a:down)
    key(d:up)
    key(s:up)
    key(w:up)
parrot(oh):
    print('oh')
    key(d:down)
    key(a:up)
    key(s:up)
    key(w:up)
parrot(hiss):
    print('hiss')
    key(s:down)
    key(a:up)
    key(d:up)
    key(w:up)
parrot(hiss:stop): print('hiss:stop')
parrot(shush):
    print('shush')
    key(s:up)
    key(a:up)
    key(d:up)
    key(w:down)
parrot(shush:stop): print('shush:stop')
parrot(ee):
    print('ee')
    key(a:up)
    key(d:up)
    key(s:up)
    key(w:up)