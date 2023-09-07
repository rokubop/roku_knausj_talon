again:                      core.repeat_phrase()

confetti:                   user.vscode('cursorless.toggleDecorations')

mouse (mid | five):         user.mouse_move_center_active_window()
mouse (bar | leaf):         mouse_move(190, 338)
mouse ledge:                mouse_move(28, 478)
mouse ridge:                mouse_move(1911, 487)
mouse (term | base):        mouse_move(924, 939)
mouse (left | one):         mouse_move(709, 419)
mouse (right | two):        mouse_move(1293, 468)
mouse (rack | reef):        mouse_move(1717, 459)

smart paste | show clip:    key(win-v)
screenshot:                 key(win-shift-s)

fast mode:                  mode.enable("user.fast")

open (in | with) paint:
    user.switcher_launch('C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2302.19.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe')
    sleep(500ms)
    key(ctrl-v)
    key(ctrl-shift-x)

then:                       skip()

continue [<number_small>]:  user.start_repeat_repeatedly(number_small or 1)
stop:                       user.cancel_repeat_repeatedly()

windows <user.find> [<user.text>]:
    key(win)
    sleep(100ms)
    insert(user.text or "")

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

zoom [in]:                  key(ctrl-plus)
zoom out:                   key(ctrl-minus)

open log:                   user.open_powershell_and_tail_log()
