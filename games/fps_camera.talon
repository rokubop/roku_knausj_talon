tag: user.fps_camera
-
hello: key(a)
scan {user.fps_direction}: user.fps_scan(fps_direction)
[scan] stop: user.fps_stop()
(nudge | small) {user.fps_direction}: user.fps_nudge(fps_direction)
soft {user.fps_direction}: user.fps_soft(fps_direction)