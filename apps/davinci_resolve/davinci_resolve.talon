app: davinci_resolve
-
settings():
    speech.timeout = 0.20
    user.parrot_default_tag = "user.parrot_default_interactive"

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

# view
(show | hide) {user.davinci_mouse_location}:
    user.davinci_click_position(davinci_mouse_location)
{user.davinci_mouse_location} (yes | no | dog):
    user.davinci_click_position(davinci_mouse_location)

# command prompt when in material view / node editor
(node | prop) [<user.text>]:
    key(ctrl-space)
    insert(user.text)
