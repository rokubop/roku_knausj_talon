app.exe: FactoryGame-Win64-Shipping.exe
-
settings():
    speech.timeout = 0.05
    key_hold = 64.0
    key_wait = 16.0
    user.game_v2_calibrate_x_360 = 2139
    user.game_v2_calibrate_y_ground_to_center = 542

test x [<number>]:          user.game_v2_calibrate_360(number or 0)
test y [<number>]:          user.game_v2_calibrate_y_ground_to_center(number or 0)
round:                      user.game_v2_snap_180()

# menu stuff
show commands:              user.game_v2_show_commands()
hide commands:              user.game_v2_hide_commands()
game stop:                  user.game_v2_stop_all()

# movement continuous
go:                         user.game_v2_move_dir("w")
go left:                    user.game_v2_move_dir("a")
go right:                   user.game_v2_move_dir("d")
[go] back:                  user.game_v2_move_dir("s")

# movement discrete you can combo with continuous movement
step [<number_small>]:      user.game_v2_move_dir_step("w", number_small or 1)
step left [<number_small>]: user.game_v2_move_dir_step("a", number_small or 1)
step right [<number_small>]: user.game_v2_move_dir_step("d", number_small or 1)
step back [<number_small>]: user.game_v2_move_dir_step("s", number_small or 1)

# turn natural
^[turn] left$:              user.game_v2_turn_left(30)
^[turn] lefter$:            user.game_v2_turn_left(60)
^[turn] right$:             user.game_v2_turn_right(30)
^[turn] righter$:           user.game_v2_turn_right(60)

# turn slowly
(small | soft) up:          user.game_v2_soft_up(10)
(small | soft) left:        user.game_v2_soft_left(10)
(small | soft) right:       user.game_v2_soft_right(10)
(small | soft) down:        user.game_v2_soft_down(10)

[look] up:                  user.game_v2_turn_up(25)
[look] down:                user.game_v2_turn_down(25)

# continuously scan mode
# once the mode is activated, say
# "left", "right", "up", "down", "stop"
scan up:                    user.game_v2_scan_mode_enable("up")
scan left:                  user.game_v2_scan_mode_enable("left")
scan right:                 user.game_v2_scan_mode_enable("right")
scan down:                  user.game_v2_scan_mode_enable("down")

# turn snap to angle
# [snap] up:                  user.game_v2_snap_up(30)
snap left:                  user.game_v2_snap_left(90)
snap right:                 user.game_v2_snap_right(90)

# [snap] down:                user.game_v2_snap_down(30)
# snap pop:                   user.game_v2_snap_last_position()

# similar to snap, but keep your current movement direction
# look up:                    user.game_v2_look_up(30)
look left:                  user.game_v2_look_left(90)
look right:                 user.game_v2_look_right(90)
# look down:                  user.game_v2_look_down(30)
look (back | round):        user.game_v2_look_back(180)
[look] pop:                 user.game_v2_look_reset()

set | reset:                user.game_v2_reset_center_y()

jump:                       key(space)
(stand | crouch):           key(ctrl)
(walk | run | slow | fast | sprint): key(shift)

spam:                       user.game_v2_mouse_hold('left')
spam <user.letter>:         user.game_v2_key_repeat(letter, "500ms")
spam stop:                  user.game_v2_spam_stop()
long <user.letter>:         user.game_v2_key_hold(letter, "2s")

^stop$:                     user.game_v2_stop_layer_by_layer()
^stop all$:                 user.game_v2_stop_all()
