app: blue_stacks
-

swipe down:
    mouse_drag()
    user.mouse_move_native_down()
    sleep(0.5)
    mouse_release()
    user.mouse_move_native_stop()

swipe up:
    mouse_drag()
    user.mouse_move_native_up()
    sleep(0.5)
    mouse_release()
    user.mouse_move_native_stop()
