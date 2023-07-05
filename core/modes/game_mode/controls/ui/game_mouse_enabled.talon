mode: user.game
and tag: user.game_mouse_enabled
-
touch | click:
	user.game_click(0)
righty:
	user.game_click(1)
curse stay:
    user.mouse_stay_in_place(1)
curse come:
    user.mouse_stay_in_place(0)
(scroll | wheel) up:
    user.mouse_scroll_up()
(scroll | wheel) down:
    user.mouse_scroll_down()
wheel upper:
    user.mouse_scroll_up_continuous()
wheel downer:
    user.mouse_scroll_down_continuous()
drag:
	user.mouse_drag(0)
end drag | drag end:
    user.mouse_drag_end()
