app: bg_3
-
settings():
    user.parrot_rpg_increment_x = 43
    user.parrot_rpg_increment_y = 43
    speech.timeout = 0.20
    user.parrot_default_tag = "user.parrot_default_interactive"
# parrot(tut): mouse_click(1)

fly: user.parrot_mode_bg_fly_toggle()

highlight [yes]: key(alt:down)
highlight (off | no | stop): key(alt:up)

cam top: key(o)
(focus | follow) [me] | cam me | home: key(home)

car one: key(f1)
car two: key(f2)
car three: key(f3)
car four: key(f4)
car next: key("]")
car last: key("[")

disk | quick save: key(f5)
quick load: key(f8)

hide ui: key(f10)