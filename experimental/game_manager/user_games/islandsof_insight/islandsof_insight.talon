app: islandsof_insight
-
settings():
    user.game_v2_calibrate_x_360 = 4790
    user.game_v2_calibrate_y_ground_to_center = 1180

tag(): user.game_v2

game:                       user.game_v2_islandsof_insight_parrot_mode_enable()
menu:                       user.parrot_v5_mode_enable("user.parrot_v5_default")
