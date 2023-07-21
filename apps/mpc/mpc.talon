app.app: mpc
and os: windows
-
play | pause:               key(space)
go to:                      key(ctrl-g)
go [to] start:              key(home)

left:                       key(left)
tug | go back:
    key(left:3)
    key(ctrl-down:12 ctrl-up:2)
lefter:                     key(left:10)
big left:                   key(left:50)
right:                      key(right)
go forward:                 key(right)
writer:                     key(right:10)
big right:                  key(right:50)

sound up:                   key(up:3)
sound tiny up:              key(up:1)
sound upper:                key(up:6)
sound down:                 key(down:3)
sound tiny down:            key(down:1)
sound downer:               key(down:6)
sound (zero | mute):        key(down:20)
sound max:                  key(up:20)

speed (down | slow | slower): key(ctrl-down)
slow | slower:              key(ctrl-down)
[speed] slowest:            key(ctrl-down:12)
fast | faster:              key(ctrl-up)
speed (up | fast | faster): key(ctrl-up)
[speed] fastest:            key(ctrl-up:12)
[speed] (normal | default): key(ctrl-down:12 ctrl-up:2)

home:                       skip()
