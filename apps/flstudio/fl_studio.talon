app: fl studio
os: windows
-

settings():
    speech.timeout = 0.20
    user.parrot_default_tag = "user.parrot_default_interactive"

# adding instruments (tracks) and plugins (mixer)
add {user.fl_instrument}:
    mouse_click(1)
    key(t i)
    insert(fl_instrument)
    key(enter)

add {user.fl_plugin}:       user.fl_choose_plugin(fl_plugin)

(plug | slot) {user.fl_slot_y_position}:
    user.fl_click_slot(fl_slot_y_position)
(plug | slot) {user.fl_slot_y_position} (dog | yes | no):
    user.fl_click_slot_light(fl_slot_y_position)
(plug | slot) {user.fl_slot_y_position} delete:
    user.fl_click_slot_menu(fl_slot_y_position)
    key(e)
(plug | slot) {user.fl_slot_y_position} {user.fl_plugin}:
    user.fl_move_mouse_to_slot(fl_slot_y_position)
    user.fl_choose_plugin(fl_plugin)

# tools
pen:                        key(p)
cut:                        key(c)
take:                       key(e)
mute:                       key(t)
hand:                       user.mouse_drag(2)
close | hide:               key(escape)
play | pause:               key(space)
tempo:                      key(ctrl-f5)

# selection
take box | box:
    key("ctrl:down")
    mouse_drag()
    key("ctrl:up")

pre time | time it:         user.fl_mouse_move_time()

time clear | take (nothing | none): key(ctrl-d)
take time:                  key(ctrl-enter)
take this:
    key("ctrl:down")
    mouse_click()
    key("ctrl:up")
take time this:
    key("ctrl:down")
    mouse_click()
    key("ctrl:up")
    key(ctrl-enter)

# sidebar
bar (show | hide | toggle): user.fl_toggle_bar()
bar collapse:               key(ctrl-up)
(show | hide | toggle) bar | bar dog: user.fl_toggle_bar()
<user.find> [<user.text>]:
    mouse_move(92, 1015)
    mouse_click(0)
    edit.delete_line()
    insert(text or "")

# windows
mix:                        key(f9)
midi:                       key(f7)
range | playlist | time:    key(f5)
channels | inst:            key(f6)
cleanup | hide all | close all | high doll: key(f12 f5 f9)
layout (one | set | default | reset): user.fl_set_normalized_layout()
zen mode:                   key(enter)

(pat | pattern) clone:
    key(shift:down)
    mouse_drag()
    key(shift:up)

# tracks
track clone:
    mouse_click(1)
    key(o o)
    key(enter enter)
track delete:
    mouse_click(1)
    key(e enter enter)
track (add | make | new | insert):
    mouse_click(1)
    key(i)
group above:
    mouse_click(1)
    key(g)
track color:
    mouse_click(1)
    key(r)
    mouse_click(0)
(color group | auto color group):
    mouse_click(1)
    key(down down enter)

# playlist/timeline actions
# pan:                        user.fl_studio_pan_mode_enable()
time (add | insert):        key(ctrl-insert)
slice:
    key(alt-shift:down)
    mouse_click()
    key(alt-shift:up)
preview | view:
    key(alt:down)
    user.mouse_drag(1)
    key(alt:up)
copy midi:                  key(f6 ctrl-c)
paste midi:                 key(f6 ctrl-v)
octave up:                  key(f7 ctrl-up escape)
octave down:                key(f7 ctrl-down escape)
make unique:
    mouse_click(0)
    key(m)
(stretch | toggle stretch): key(shift-m)
(fade | toggle fade):       key(shift-f)
clone (bar | time):         key(ctrl-b)
browse:
    key(down)
    key(enter)

# global actions
automate:
    mouse_move(243, 18)
    mouse_click(0)
    key(l a)
color:
    mouse_click(0)
    key(r)
    mouse_click(0)
(mute this | unmute this):
    key(t)
    mouse_click(0)
    key(p)
play next:                  key(down enter)

# props
prop | props:
    mouse_click(0)
    mouse_click(0)
set <number>:
    mouse_click(1)
    key(t)
    insert(number)
    key(enter)
norm | normal | normalize:  user.fl_normalize()
keys | keyboard:            user.fl_toggle_keys()
resample only:
    mouse_click(0)
    key(down down enter)

# mixer
mix start | pre mix:        user.fl_go_to_mixer_start()
mix {user.fl_mixer_x_position}: user.fl_click_mixer(fl_mixer_x_position)

# zoom
zoom [in]:
    key("ctrl:down")
    mouse_scroll(-1000)
    key("ctrl:up")
zoom out:
    key("ctrl:down")
    mouse_scroll(1000)
    key("ctrl:up")
shrink:
    key("alt:down")
    mouse_scroll(500)
    key("alt:up")
grow:
    key("alt:down")
    mouse_scroll(-500)
    key("alt:up")
