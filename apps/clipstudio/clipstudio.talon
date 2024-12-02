app: clip_studio_paint
-

move | hand:                key(m)
pen | brush:                key(d)
paint:                      key(g)
take:
    key(f)
    mouse_drag()
box:                        key(f)
show shortcuts:             key(ctrl-shift-alt-k)
small:                      key(q)
big:                        key(w)
export [<phrase>]:
    key(alt-f r r right p)
    sleep(0.2)
    insert(user.formatted_text(phrase, 'SNAKE_CASE'))
new [from] clip [board]:
    key(alt-f down enter)
crop:
    key(alt-e z)
wand: key(k)