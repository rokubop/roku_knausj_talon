track [on | off]:           tracking.control_toggle()
zoom mouse:                 tracking.control_zoom_toggle()
track debug:                tracking.control_debug_toggle()
calibrate:                  tracking.calibrate()
touch:
    mouse_click(0)
    user.grid_close()
    user.mouse_drag_end()

righty | right click:
    mouse_click(1)
    user.grid_close()

mid click:
    mouse_click(2)
    user.grid_close()

<user.modifiers> touch:
    key("{modifiers}:down")
    mouse_click(0)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
<user.modifiers> righty:
    key("{modifiers}:down")
    mouse_click(1)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
(dub click | duke):
    mouse_click()
    mouse_click()
    # close the mouse grid
    user.grid_close()
(trip click | trip lick):
    mouse_click()
    mouse_click()
    mouse_click()
    user.grid_close()
drag:
    user.mouse_drag(0)
    user.grid_close()
drag right:
    user.mouse_drag(1)
    user.grid_close()
drag mid:
    user.mouse_drag(2)
    user.grid_close()
end drag | drag (end | stop): user.mouse_drag_end()
wheel down | downer:        user.mouse_scroll_down(6)
wheel down here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down()
wheel tiny [down]:          user.mouse_scroll_down(0.2)
wheel tiny [down] here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down(0.2)
wheel downer:               user.mouse_scroll_down_continuous()
wheel downer here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down_continuous()
wheel up | upper:           user.mouse_scroll_up(6)
wheel up here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up()
wheel tiny up:              user.mouse_scroll_up(0.2)
wheel tiny up here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up(0.2)
wheel upper:                user.mouse_scroll_up_continuous()
wheel upper here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up_continuous()
mouse gaze:                 user.mouse_gaze_scroll()
mouse gaze here:
    user.mouse_move_center_active_window()
    user.mouse_gaze_scroll()
mouse stop:                 user.mouse_scroll_stop()
mouse stop here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_stop()
wheel left:                 user.mouse_scroll_left()
wheel left here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left()
wheel tiny left:            user.mouse_scroll_left(0.5)
wheel tiny left here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left(0.5)
wheel right:                user.mouse_scroll_right()
wheel right here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right()
wheel tiny right:           user.mouse_scroll_right(0.5)
wheel tiny right here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right(0.5)
copy mouse position:        user.copy_mouse_position()

curse no:
    # Command added 2021-12-13, can remove after 2022-06-01
    app.notify("Please activate the user.mouse_cursor_commands_enable tag to enable this command")
curse stay:
    user.mouse_stay_in_place(1)
curse come:
    user.mouse_stay_in_place(0)
