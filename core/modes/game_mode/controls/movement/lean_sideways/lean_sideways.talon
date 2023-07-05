mode: user.game
and tag: user.game_lean_sideways
-
#start/stop leaning left or change leaning direction from right to left
peek left | leek:
	user.game_lean_sideways("left")
#start/stop leaning right or change leaning direction from left to right
peek right | reek:
	user.game_lean_sideways("right")
#start/stop leaning right or left
upright:
	user.game_lean_sideways_stop()