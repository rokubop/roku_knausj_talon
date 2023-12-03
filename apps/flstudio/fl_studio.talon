app: fl studio
os: windows
-

settings():
    speech.timeout = 0.20
    user.parrot_default_tag = "user.parrot_default_interactive"

# tracks
go <user.letters>:
    user.fl_click_track(letters)
    mouse_click(0)
track <user.letters>:       user.fl_click_track(letters)
track <user.letters> {user.fl_instrument}:
    user.fl_track_add_instrument(fl_instrument, letters)
track [add] {user.fl_instrument} | add {user.fl_instrument}:
    user.fl_track_add_instrument(fl_instrument, "")
track [<user.letters>] clone [<user.letters>]: user.fl_track_clone(letters or "")
track [<user.letters>] delete [<user.letters>]: user.fl_track_delete(letters or "")
track (add | make | new | insert):
    mouse_click(1)
    key(i)
track (group | indent | dedent):
    mouse_click(1)
    key(g)
track color:
    mouse_click(1)
    key(r)
    mouse_click(0)
track color group:
    mouse_click(1)
    key(down down enter)

slot [add] {user.fl_plugin}: user.fl_choose_plugin(fl_plugin)
slot [add] <user.text>:     user.fl_choose_plugin(text)
slot {user.fl_slot_y_position}:
    user.fl_click_slot(fl_slot_y_position)
slot {user.fl_slot_y_position} (dog | yes | no):
    user.fl_click_slot_light(fl_slot_y_position)
slot {user.fl_slot_y_position} delete:
    user.fl_click_slot_menu(fl_slot_y_position)
    key(e)
slot {user.fl_slot_y_position} {user.fl_plugin}:
    user.fl_move_mouse_to_slot(fl_slot_y_position)
    user.fl_choose_plugin(fl_plugin)
slot (remove | delete):
    mouse_click()
    key(e)

# tools
pen:                        key(p)
cut:                        key(c)
take:                       key(e)
mute:                       key(t)
hand:                       user.mouse_drag(2)
close | hide:               key(escape)
play | pause:               key(space)
tempo tap:                  key(ctrl-f5)
tempo <number>:
    mouse_move(493, 21)
    mouse_click(1)
    key(t)
    insert(number)
    key(enter)

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
midi | note | keys:         key(f7)
range | playlist | time | grid: key(f5)
rack | channels | inst:     key(f6)
cleanup | hide all | close all | high doll: key(f12 f5 f9)
layout (one | set | default | reset): user.fl_set_normalized_layout()
zen mode:                   key(enter)

(pat | pattern) clone:
    key(shift:down)
    mouse_drag()
    key(shift:up)

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

# pro q commands
# pro low cut
# pro high pass
# pro

# serum commands
# try windows ui to detect window title?

# vital commands

# pro mb commands

# track visualize number grid

# ss/sh parrot and foot pedal modes
# pan- SS sh nn. SS sh. t switch
# scroll - SS sh. nn. SS sh . t switch.  pal inc.
# zoom - SS sh. nn. SS sh.  t switch.  pal inc
# zoom y
# knob - SS sh palate tut pop acct.

# move y?
# move x?
# knob
# knob x | knob y - parrot and foot
# zoom x - parrot and foot pedal
# zoom y - parrot and foot pedal
# scroll x - parrot and foot pedal
# scroll y - parrot and foot pedal

[mode] zoom:
    user.fl_tag_remove("user.fl_studio_scroll")
    user.fl_tag_remove("user.pedal_head_gaze")
    user.fl_tag_remove("user.fl_studio_ui")
    user.fl_tag_add("user.fl_studio_zoom")
[mode] scroll:
    user.fl_tag_remove("user.fl_studio_zoom")
    user.fl_tag_remove("user.pedal_head_gaze")
    user.fl_tag_remove("user.fl_studio_ui")
    user.fl_tag_add("user.fl_studio_scroll")
mode UI:
    user.fl_tag_remove("user.fl_studio_zoom")
    user.fl_tag_remove("user.pedal_head_gaze")
    user.fl_tag_remove("user.fl_studio_scroll")
    user.fl_tag_add("user.fl_studio_ui")
mode gaze:
    user.fl_tag_remove("user.fl_studio_zoom")
    user.fl_tag_remove("user.fl_studio_ui")
    user.fl_tag_remove("user.fl_studio_scroll")
    user.fl_tag_add("user.pedal_head_gaze")
mode default:               user.fl_tag_reset()

# zoom [in]:
#     key("ctrl:down")
#     mouse_scroll(-1000)
#     key("ctrl:up")
# zoom out:
#     key("ctrl:down")
#     mouse_scroll(1000)
#     key("ctrl:up")
# shrink:
#     key("alt:down")
#     mouse_scroll(500)
#     key("alt:up")
# grow:
#     key("alt:down")
#     mouse_scroll(-500)
#     key("alt:up")

test:
    matches = user.mouse_helper_find_template_relative("2023-12-02_23.09.31.490836.png", 0, -12)
    user.marker_ui_show(matches)
# test:                       user.fl_test()
