app: fl studio
mode: command
-
add {user.fl_instrument}:
    mouse_click(1)
    key(t i)
    insert(fl_instrument)
    key(enter)
add {user.fl_plugin}:       user.fl_choose_plugin(fl_plugin)
bar (show | hide | toggle): user.fl_toggle_bar()
bar collapse:               key(ctrl-up)
<user.find> [<user.text>]:
    mouse_move(92, 1015)
    mouse_click(0)
    edit.delete_line()
    insert(text or "")
(show | hide | toggle) bar | bar dog: user.fl_toggle_bar()
cleanup | hide all | close all | high doll: key(f12 f5 f9)
layout (one | set | default | reset): user.fl_set_normalized_layout()

track color:
    mouse_click(1)
    key(r)
    mouse_click(0)
track clone:
    mouse_click(1)
    key(o o)
    key(enter enter)
track delete:
    mouse_click(1)
    key(e enter enter)
track (make | new | insert):
    mouse_click(1)
    key(i)


copy midi:                  key(f6 ctrl-c)
paste midi:                 key(f6 ctrl-v)
octave up:                  key(f7 ctrl-up escape)
octave down:                key(f7 ctrl-down escape)

group above:
    mouse_click(1)
    key(g)
make unique:
    mouse_click(0)
    key(m)
color:
    mouse_click(0)
    key(r)
    mouse_click(0)
(stretch | toggle stretch): key(shift-m)
(fade | toggle fade):       key(shift-f)
close | hide:               key(escape)
(color group | auto color group):
    mouse_click(1)
    key(down down enter)
resample only:
    mouse_click(0)
    key(down down enter)
prop | props:
    mouse_click(0)
    mouse_click(0)
(mute this | unmute this):
    key(t)
    mouse_click(0)
    key(p)
set <number>:
    mouse_click(1)
    key(t)
    insert(number)
    key(enter)
key | keys | keyboard:      user.fl_toggle_keys()

tempo:                      key(ctrl-f5)
take:                       key(e)
take (nothing | none):      key(ctrl-d)
take time:                  key(ctrl-enter)
pen:                        key(p)
cut:                        key(c)
mute:                       key(t)
norm | normal | normalize:  user.normalize()
# preview one:
#     key(alt:down)
#     mouse_click(button=1, hold=16000)
#     key(alt:up)
# preview:
    # key(alt-RButton:down) mouse_click(0) key(alt-RButton:up)
# (open instrument | instrument | edit instrument): user.fl_openInstrument
automate:
    mouse_move(243, 18)
    mouse_click(0)
    key(l a)
play next:                  key(down enter)
# start browsing: user.fl_startBrowsing
# (stop browsing | stop): user.fl_stopBrowsing
play | pause:               key(space)

playlist | range:           key(f5)
channels | inst:            key(f6)
# drag:                       mouse_drag(2)
(stop drag | drag up | drag stop): mouse_up(middle)
wrap:
    user.mouse_click("control")
    key(ctrl-enter)

clone (bar | time):         key(ctrl-b)

box:
    key("ctrl:down")
    mouse_drag()
    key("ctrl:up")

# mixer
mix:                        key(f9)
(base | mix) (show | hide | dog): key(f9)
mix start | pre mix:        user.fl_go_to_mixer_start()
mix {user.fl_mixer_x_position}: user.fl_click_mixer(fl_mixer_x_position)

(plug | slot) {user.fl_slot_y_position}:
    user.fl_click_slot(fl_slot_y_position)
(plug | slot) {user.fl_slot_y_position} dog:
    user.fl_click_slot_light(fl_slot_y_position)
(plug | slot) {user.fl_slot_y_position} delete:
    user.fl_click_slot_menu(fl_slot_y_position)
    key(e)
(plug | slot) {user.fl_slot_y_position} {user.fl_plugin}:
    user.fl_move_mouse_to_slot(fl_slot_y_position)
    user.fl_choose_plugin(fl_plugin)

zen mode:                   key(enter)
