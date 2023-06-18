tag: user.game_mount
and mode: user.game
and not mode: sleep
-
mount:
	user.game_mount()
dismount:
	user.game_dismount()
[mount] [ride] fast:
	user.game_mount_ride_faster()
[mount] [ride] slow:
	user.game_mount_ride_slower()
[mount] halt:
	user.game_mount_stop()