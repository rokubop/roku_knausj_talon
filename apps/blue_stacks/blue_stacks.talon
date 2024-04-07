app: blue_stacks
-

swipe down:
    mouse_drag()
    user.game_look_up_45()
    sleep(0.5)
    mouse_release()
    # user.mouse_move_native_stop()

swipe up:
    mouse_drag()
    user.game_look_down_45()
    sleep(0.5)
    mouse_release()
    # user.mouse_move_native_stop()
