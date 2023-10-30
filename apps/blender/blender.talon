app: blender
-
settings():
    speech.timeout = 0.05
    user.parrot_default_tag = "user.parrot_default_interactive"
    # parrot includes dragging mouse, ctrl, alt, shift, and pan and orbiting

# parrot(tut): mouse_click(1)

# command prompt in 3D view
please [<user.text>]:
    key(f3)
    sleep(50ms)
    insert(user.text or "")

# command prompt when in material view / node editor
(node | prop) [<user.text>]:
    key(shift-a)
    key(s)
    insert(user.text)

# movement rotation and scale
# e.g. gust plex 90
# e.g. red zip 180
# e.g. sun yank
<user.letter> <user.letter> <number>:
    key(letter_1 letter_2)
    insert(number)

add:                        key(shift-a)
add cube: key(shift-a m c)
add plane: key(shift-a m p)
add cylinder: key(shift-a m y)
add collection [instance] [<user.text>]:
    key(shift-a o)
    sleep(50ms)
    insert(user.text or "")
add [empty] arrow: key(shift-a e s)

# camera
cam:        key(keypad_0)
cam me:     key(ctrl-alt-keypad_0)
cam top:                    key(keypad_7)
cam bottom:                 key(ctrl-keypad_7)
cam (side | right):         key(keypad_3)
cam (backside | left):      key(ctrl-keypad_3)
cam front:                  key(keypad_1)
cam back:                   key(ctrl-keypad_1)
cam set [active]:
    key(f3)
    sleep(50ms)
    insert("set active cam")
    sleep(50ms)
    key(enter)
cam (fly | sta):                user.blender_activate_cam_fly_mode()
[cam] (orthogonal | orthog | ortho | orthographic | orthograph):        key(keypad_5)

# views
show asset:                 key(shift-f1)
show graph:                 key(shift-f6)
show three D:               key(shift-f5)
show (shader | material | geometry):   key(shift-f3)
show ((timeline | time) | dope [sheet]): key(shift-f12)
show video:                 key(shift-f8)
show image:                 key(shift-f10)

# operations
focus:                      key(keypad_decimal)
isolate:                    key(/)

pan:
    key(shift:down)
    user.mouse_drag(2)
    key(shift:up)
ex ray:                     key(alt-z)
zoom:
    key(ctrl:down)
    user.mouse_drag(2)
    key(ctrl:up)
snap:                       key(shift-tab)

# timeline
head:                       key(shift-left)
tail:                       key(shift-right)
play:                       key(space)
stop:                       key(space)
record [dog]:               key(ctrl-alt-r)

mode: key(ctrl-tab)
mode edit:
    key(ctrl-tab)
    key(e)
mode object:
    key(ctrl-tab)
    key(o)
mode pose:
    key(ctrl-tab)
    key(p)
mode draw:
    key(ctrl-tab)
    key(d)

pivot: key(.)
pivot active: key(. a)
pivot cursor: key(. d)
pivot individual [origins]: key(. o)

transform: key(,)
transform global: key(, g)
transform normal: key(, n)
transform local: key(, l)

cursor [to] (selected | selection):
    key(f3)
    sleep(50ms)
    insert("cursor selected")
    key(enter)
cursor [to] active:
    key(f3)
    sleep(50ms)
    insert("cursor active")
    key(enter)
origin [to] (selected | selection):
    key(f3)
    sleep(50ms)
    insert("origin selected")
    key(enter)
origin [to] cursor:
    key(f3)
    sleep(50ms)
    insert("origin cursor")
    key(enter)
(selected | selection) [to] cursor:
    key(f3)
    sleep(50ms)
    insert("selection cursor")
    key(enter)


zen mode:                   key(ctrl-space)

render animation: key(ctrl-f12)
render image: key(f12)

region (set | clear): key(alt-b)

# nodes/materials
preview: user.mouse_click("ctrl-shift-left")

scout clear:
    mouse_move(1698, 61)
    mouse_click()
    edit.delete_line()

scout <user.text>:
    mouse_move(1698, 61)
    mouse_click()
    edit.delete_line()
    insert(user.text or "")

take siblings: key(shift-g s)
take collection: key(shift-g o)

subdivide:
    mouse_click(1)
    key(s)