app: talos_2
mode: user.islandsof_insight_parrot
and mode: user.islandsof_insight_nav_mode
-
parrot(ee):                 user.game_v2_stop_layer_by_layer()
parrot(ah):                 user.event_mouse_nav("left")
parrot(oh):                 user.event_mouse_nav("right")
parrot(hiss):               user.event_mouse_nav("down")
parrot(hiss:stop):          skip()
parrot(shush):              user.event_mouse_nav("up")
parrot(shush:stop):         skip()
parrot(er):                 user.islandsof_insight_nav_mode_disable()
