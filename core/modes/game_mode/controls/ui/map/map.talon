tag: user.game_map
and mode: user.game
-
map show:
	user.game_map_show()
map hide:
    user.game_map_hide()
map (marker | waypoint) [place | here]:
    user.game_map_marker_place()
map (marker | waypoint) clear:
    user.game_map_marker_clear()
map center:
    user.game_map_center()
map rotate:
    user.game_map_rotate()
map (floor | level) up:
    user.game_map_floor_up()
map (floor | level) down:
    user.game_map_floor_down()
map filter [list] [show]:
    user.game_map_filters_show()
map filter [list] hide:
    user.game_map_filters_hide()
map [filter] toggle:
    user.game_map_filter_toggle()
map [filter] toggle all:
    user.game_map_filters_toggle_all()
map zoom [in]:
    user.game_map_zoom_in()
map zoom out:
    user.game_map_zoom_out()
map zoom inner | map closer:
    user.game_map_zoom_in_continuous()
map zoom outer | map farther:
    user.game_map_zoom_out_continuous()
map zoom (stop | done):
    user.game_map_zoom_continuous_stop()