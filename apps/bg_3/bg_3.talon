app: bg_3
-
parrot(tut): mouse_click(1)
# parrot(cluck): user.parrot_mode_select('bg_3_follow')

# parrot(cluck): user.parrot_mode_enable()
fly: user.parrot_mode_bg_fly_toggle()

highlight [yes]: key(alt:down)
highlight (off | no | stop): key(alt:up)

cam top: key(o)
(focus | follow) [me] | cam me | home: key(home)

car one: key(f1)
car two: key(f2)
car three: key(f3)
car four: key(f4)

disk | quick save: key(f5)
quick load: key(f8)

hide ui: key(f10)