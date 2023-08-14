again:                      user.repeat()
confetti:                   user.vscode('cursorless.toggleDecorations')
mouse (mid | five):         user.mouse_move_center_active_window()
smart paste | show clip:    key(win-v)
screenshot:                 key(f3)

fast mode:                  mode.enable("user.fast")

open (in | with) paint:
    user.switcher_launch('C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2302.19.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe')
    sleep(500ms)
    key(ctrl-v)
    key(ctrl-shift-x)

desktop {user.system_paths}:
    key(win-e)
    sleep(500ms)
    user.file_manager_open_directory(system_paths)

then:                       skip()

continue [<number_small>]:  user.start_repeat_repeatedly(number_small or 1)

flow <user.find> [<user.text>]:
    key(ctrl-shift-alt-f)
    sleep(100ms)
    insert(user.text or "")

windows <user.find> [<user.text>]:
    key(win)
    sleep(100ms)
    insert(user.text or "")
