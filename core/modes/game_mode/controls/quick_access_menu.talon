tag: user.game_quick_access_menu
and mode: user.game
and not mode: sleep
-
(wheel | quick access) [menu] [toggle]:
	user.game_quick_access_menu_toggle()
(wheel | quick access) [menu] show:
	user.game_quick_access_menu_toggle(1)
(wheel | quick access) [menu] (hide | done):
	user.game_quick_access_menu_toggle(0)