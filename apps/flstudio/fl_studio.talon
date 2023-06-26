app: fl studio
mode: command
-
add {user.fl_instrument}:
    mouse_click(1)
    key(t i instrument enter)
add {user.fl_plugin}:
    mouse_click(1)
    sleep(100ms)
    insert(fl_plugin or "")
    key(enter)
(show | hide | toggle) bar | bar dog: key(alt-f8)
cleanup:                    key(f12 f5 f9)
delete track:
    mouse_click(1)
    key(e enter enter)
copy midi:                  key(f6 ctrl-c)
paste midi:                 key(f6 ctrl-v)
octave up:                  key(f7 ctrl-up escape)
octave down:                key(f7 ctrl-down escape)
(insert | add) track:
    mouse_click(1)
    key(i)
group above:
    mouse_click(1)
    key(g)
make unique:
    mouse_click(0)
    key(m)
change color:
    mouse_click(0)
    key(r)
    mouse_click(0)
(stretch | toggle stretch): key(shift-m)
(fade | toggle fade):       key(shift-f)
close:                      key(escape)
(color group | auto color group):
    mouse_click(1)
    key(down down enter)
resample only:
    mouse_click(0)
    key(down down enter)
props:
    mouse_click(0)
    mouse_click(0)
(mute this | unmute this):
    key(t)
    mouse_click(0)
    key(p)
type <number>:
    mouse_click(1)
    key(t)
    "{number}"
    key(enter)
tempo:                      key(ctrl-f5)
take:                       key(e)
pen:                        key(p)
cut:                        key(c)
mute:                       key(t)
take (nothing | none):      key(ctrl-d)
normalize:                  user.normalize()
# preview one:
#     key(alt:down)
#     mouse_click(button=1, hold=16000)
#     key(alt:up)
# preview:
    # key(alt-RButton:down) mouse_click(0) key(alt-RButton:up)
# resample: user.fl_setResampleMode
# normalize: user.fl_normalize
# (open instrument | instrument | edit instrument): user.fl_openInstrument
automate:
    mouse_move(243, 18)
    mouse_click(0)
    key(l a)
next:                       key(down enter)
# start browsing: user.fl_startBrowsing
# (stop browsing | stop): user.fl_stopBrowsing
play:                       key(space)
mixer:                      key(f9)
playlist:                   key(f5)
channels:                   key(f6)
drag:                       mouse_down(middle)
(stop drag | drag up | drag stop): mouse_up(middle)
