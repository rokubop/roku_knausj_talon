win.title: Planet of Lana
and mode: user.game
-
settings():
    key_hold = 64.0
    key_wait = 16.0
    user.mouse_hold = 16000
    user.mouse_wait = 0

tag(): user.game_side_scroller
# adds noise "pop" to go/stop
# adds noise "shush" for left
# adds noise "hiss" for right
# adds noise "palate" for jump

# eye tracking doesn't work for this game

# generic
north:                      key(w)
south:                      key(s)
tug:                        key(a)
push:                       key(d)
scrape:                     key(escape)
yep:                        key(enter)
touch:                      mouse_click()
each | use:                 key(e)
long each:
    key(e:down)
    sleep(1000ms)
    key(e:up)

# movement
right:                      user.game_side_scroller_right()
left:                       user.game_side_scroller_left()
up:                         user.game_side_scroller_up()
down:                       user.game_crouch()
jump:                       user.game_jump()
go | stop:                  user.game_side_scroller_start_stop()
down:                       user.game_crouch()
(grab | move):
    mouse_release()
    mouse_drag()
(grab | move) no:           mouse_release()

# cat commands
[cat] stay:                 key(q)
[cat] come:
    key(q:down)
    sleep(1000ms)
    key(q:up)
cat (go | send | move):
    mouse_drag(1)
[cat] cancel:
    mouse_release(1)
cat yes:
    mouse_click(0)
    mouse_release(1)
