again:                      core.repeat_phrase()

confetti:                   user.vscode('cursorless.toggleDecorations')

spot (mid | five):        user.mouse_move_center_active_window()
spot bar:                 user.mouse_move_relative_window(190, 338)
spot ledge:               user.mouse_move_relative_window(28, 478)
spot ridge:               user.mouse_move_relative_window(1911, 487)
spot (term | base):       user.mouse_move_relative_window(924, 939)
spot (left | one):        user.mouse_move_relative_window(709, 419)
spot (right | two):       user.mouse_move_relative_window(1293, 468)
spot rack:                user.mouse_move_relative_window(1717, 459)

^screen <number> (mid | five): user.mouse_move_relative_screen(number, 960, 540)
^screen <number> bar:       user.mouse_move_relative_screen(number, 190, 338)
^screen <number> ledge:     user.mouse_move_relative_screen(number, 28, 478)
^screen <number> ridge:     user.mouse_move_relative_screen(number, 1911, 487)
^screen <number> (term | base): user.mouse_move_relative_screen(number, 924, 939)
^screen <number> (left | one): user.mouse_move_relative_screen(number, 709, 419)
^screen <number> (right | two): user.mouse_move_relative_screen(number, 1293, 468)
^screen <number> rack:      user.mouse_move_relative_screen(number, 1717, 459)

smart paste | show clip:    key(win-v)
screenshot:                 key(win-shift-s)

^fast mode:                 mode.enable("user.fast")

open (in | with) paint:
    user.switcher_launch('C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2302.19.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe')
    sleep(500ms)
    key(ctrl-v)
    key(ctrl-shift-x)

then:                       skip()

^continue [<number_small>]: user.start_repeat_repeatedly(number_small or 1)
^stop:                      user.cancel_repeat_repeatedly()

reload it:
    sleep(100ms)
    key(f5)
    sleep(300ms)

explore:                    key(win-e)
explore {user.system_paths}:
    key(win-e)
    sleep(500ms)
    user.file_manager_open_directory(system_paths)
explore this:               key(shift-alt-r)

desktop new:                key(win-ctrl-d)
desktop (right | next):     key(win-ctrl-right)
desktop (left | last):      key(win-ctrl-left)
desktop close:              key(win-ctrl-f4)
desktop (show | revert | hide): key(win-d)
show desktop:               key(win-d)

tracker:                    user.parrot_use_default_tracking()

(reader | speech) (yes | no):
    key(capslock:down)
    key(s)
    key(capslock:up)

coder: 