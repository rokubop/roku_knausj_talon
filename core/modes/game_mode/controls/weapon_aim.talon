tag: user.game_weapon_aim
and mode: user.game
and not mode: sleep
-
aim [toggle]:
	user.game_weapon_aim_toggle()
aim start:
    user.game_weapon_aim_toggle(1)
aim done:
	user.game_weapon_aim_toggle(0)