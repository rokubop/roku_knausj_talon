mode: command
-
test paste:                 user.game_v2_calibrate_paste()
game create [(files | talon)]: user.game_v2_create_talon_files()
game (setup | help):        user.game_v2_help_show()
game help close:            user.game_v2_help_close()
game calibrate [x] [<number>]: user.game_v2_calibrate_360(number or 0)
game calibrate y [<number>]: user.game_v2_calibrate_y_ground_to_center(number or 0)
calibrate x [<number>]:     user.game_v2_calibrate_360(number or 0)
calibrate y [<number>]:     user.game_v2_calibrate_y_ground_to_center(number or 0)
canvas (stop | hide):       user.game_v2_canvas_hide()
calibrate (stop | hide):    user.game_v2_canvas_hide()
calibrate save:             user.game_v2_calibrate_save()
