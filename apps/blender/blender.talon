app: blender
mode: command
-
settings():
    speech.timeout = 0.05

# camera
cam set:                    key(ctrl-alt-keypad_0)
cam dog:                    key(keypad_0)
cam top:                    key(keypad_7)
cam bottom:                 key(ctrl-keypad_7)
cam (side | right):         key(keypad_3)
cam (backside | left):      key(ctrl-keypad_3)
cam front:                  key(keypad_1)
cam back:                   key(ctrl-keypad_1)
cam:                        user.mouse_drag(2)
orthogonal | orthog:        key(keypad_5)

# views
show graph:                 key(shift-f6)
show three D:               key(shift-f5)
show (shader | material):   key(shift-f3)
show ((timeline | time) | dope [sheet]): key(shift-f12)
show video:                 key(shift-f8)
show geometry:              key(shift-f3)
show image:                 key(shift-f10)

# operations
focus:                      key(keypad_decimal)
add:                        key(shift-a)
box:                        user.mouse_drag(0)
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
head:                       key(shift-left)
play:                       key(space)
tail:                       key(shift-right)
stop:                       key(space)
record [dog]:               key(ctrl-alt-r)
(record | record) animation: key(ctrl-f12)
