window (new | open):        app.window_open()
window next:                app.window_next()
window last:                app.window_previous()
window close:               app.window_close()
window hide:                app.window_hide()
(swap | focus) <user.running_applications>: user.switcher_focus(running_applications)
# following only works on windows. Can't figure out how to make it work for mac. No idea what the equivalent for linux would be.
focus$:                     user.switcher_menu()
running list:               user.switcher_toggle_running()
running close:              user.switcher_hide_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)

(snap | window) <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]:         user.move_window_next_screen()
snap last [screen]:         user.move_window_previous_screen()
snap screen <number>:       user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)

# roku additions
window list:                key(win-tab)
window (max | maximize):    user.window_maximize()
maximize [window]:          user.window_maximize()
window (min | minimize):    user.window_minimize()
minimize window:            user.window_minimize()
[window] restore:           user.window_restore()
restore window:             user.window_restore()
[snap] screen left:         user.move_window_to_screen(1)
[snap] screen right:        user.move_window_to_screen(2)
snap <user.running_applications> [screen] left:
    user.move_app_to_screen(running_applications, 1)
snap <user.running_applications> [screen] right:
    user.move_app_to_screen(running_applications, 2)
(folk | focus) voice meter [<phrase>]$:
    user.switcher_focus("VB-AUDIO Virtual Audio Device Mixing Console Application")
    sleep(200ms)
    user.parse_phrase(phrase or "")
swap$:
    key(alt:down)
    key(tab)
    sleep(50ms)
    key(alt:up)
