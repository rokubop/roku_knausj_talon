mode: user.game
and not mode: sleep
-
^manual save$:
				user.game_manual_save()
^quick save$:
				user.game_quick_save()
^quick load$:
				user.game_quick_load()
^(menu [pause] | escape | go back)$:
				user.game_menu()
^enter$:
				key(enter)
^backspace$:
				key(backspace)
^game console show$:
				key(`)
^track$:
				tracking.control_toggle()
