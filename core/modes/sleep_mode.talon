mode: sleep
-
settings():
    #stop continuous scroll/gaze scroll with a pop
    user.mouse_enable_pop_stops_scroll = 0
    #enable pop click with 'control mouse' mode
    user.mouse_enable_pop_click = 0

parrot(cluck):
    user.wake_if_not_hard_sleep()
