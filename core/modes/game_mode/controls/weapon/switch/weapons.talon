tag: user.game_weapons
and mode: user.game
-
weapon [switch] {user.game_previous_keyword} | nick:
	user.game_weapon_switch_previous()
weapon [switch] {user.game_next_keyword} | nack:
	user.game_weapon_switch_next()

weapon draw:
	user.game_weapon_draw()
weapon (hide | sheath) | holster:
    user.game_weapon_hide()
^weapon drop$:
    user.game_weapon_drop()

[weapon] (melee | white) [show]:
    user.game_weapon_melee_show()
[weapon] (ranged | range) [show]:
    user.game_weapon_ranged_show()
[weapon] (thrown | threw) [show]:
    user.game_weapon_thrown_show()