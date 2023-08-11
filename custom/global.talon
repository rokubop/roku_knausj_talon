-
again:                      user.repeat()
confetti:                   user.vscode('cursorless.toggleDecorations')
mouse (mid | five):         user.mouse_move_center_active_window()
smart paste | show clip:    key(win-v)
copy paste:                 key(ctrl-c ctrl-v)
<user.operator> stack:      ": "
<user.operator> dash:       " - "
screenshot:                 key(f3)
open (in | with) paint:
    user.switcher_launch('C:\Program Files\WindowsApps\Microsoft.Paint_11.2302.19.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe')
    sleep(500ms)
    key(ctrl-v)
    key(ctrl-shift-x)

desktop {user.system_paths}:
    key(win-e)
    sleep(500ms)
    user.file_manager_open_directory(system_paths)

then: skip()
tab yep:
    key(tab)
    key(enter)
south yep:
    key(down)
    key(enter)
north yep:
    key(up)
    key(enter)
continue [<number_small>]:   user.start_repeat_repeatedly(number_small or 1)
