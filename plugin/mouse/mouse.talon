track (on | off | yes | no | dog): tracking.control_toggle()
zoom mouse:                 tracking.control_zoom_toggle()
track debug:                tracking.control_debug_toggle()
calibrate:                  tracking.calibrate()
touch | click it | ticket:
    mouse_click(0)
    user.grid_close()
    user.mouse_drag_end()

^right click | rick it:
    mouse_click(1)
    user.grid_close()

^mid click | mick it:
    mouse_click(2)
    user.grid_close()

^ship it:                   user.mouse_click("shift")
^dub it:                    user.mouse_click("double")
^troll it:                  user.mouse_click("ctrl")
^trip it:                   user.mouse_click("triple")
^alt it:                    user.mouse_click("alt")

^ship right:                user.mouse_click("shift", 1)
^dub right:                 user.mouse_click("double", 1)
^troll right:               user.mouse_click("ctrl", 1)
^trip right:                user.mouse_click("triple", 1)
^alt right:                 user.mouse_click("alt", 1)

<user.modifiers> touch:
    key("{modifiers}:down")
    mouse_click(0)
    key("{modifiers}:}")
    # close the mouse grid"
    user.grid_close()
<user.modifiers> righty:
    key("{modifiers}:down")
    mouse_click(1)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
    user.grid_close()

<user.modifiers> drag:
    key("{modifiers}:down")
    user.mouse_drag(0)
    key("{modifiers}:up")

<user.modifiers> drag right:
    key("{modifiers}:down")
    user.mouse_drag(1)
    key("{modifiers}:up")

<user.modifiers> drag mid:
    key("{modifiers}:down")
    user.mouse_drag(2)
    key("{modifiers}:up")

^drag [it]:
    user.mouse_drag(0)
    user.grid_close()
^drag right | right drag | risk drag | drag risk:
    user.mouse_drag(1)
    user.grid_close()

^drag mid | mid drag:
    user.mouse_drag(2)
    user.grid_close()
end drag | drag (end | stop): user.mouse_drag_end()
wheel down | downer:        user.mouse_scroll_down(6)
wheel down here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down()
wheel tiny [down]:          user.mouse_scrollnl_down(0.2)
wheel tiny [down] here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down(0.2)
wheel downer | downer start: user.mouse_scroll_down_continuous()
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
wheel upper | upper start:  user.mouse_scroll_up_continuous()
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
