app: davinci_resolve
-

hand:                       user.mouse_drag(2)
tail:                       key(down)
head:                       key(up)
tail (file | time):         key(end)
head (file | time):         key(home)
take next:                  key(alt-right)
take last:                  key(alt-left)
snap:                       key(n)
track clone | clone [this]:
    key(ctrl-c)
    key(down)
    sleep(100ms)
    key(ctrl-v)
[track] reverse:
    key(r)
    insert(-100)
    key(enter)
clone reverse:
    key(ctrl-c)
    key(down)
    sleep(100ms)
    key(ctrl-v)
    sleep(200ms)
    key(r)
    insert(-100)
    key(enter)

sprint:                     key(shift-l)

zoom [in]:
    key(alt:down)
    mouse_scroll(-300)
    key(alt:up)

zoom out:
    key(alt:down)
    mouse_scroll(300)
    key(alt:up)
