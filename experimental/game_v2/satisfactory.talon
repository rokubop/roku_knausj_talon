app.exe: FactoryGame-Win64-Shipping.exe
-
settings():
    user.game_v2_calibrate_x_360 = 2139
    user.game_v2_calibrate_y_ground_to_center = 542

tag(): user.game_v2

please <user.text>:
    key(n)
    edit.delete_line()
    user.paste(text)
