tag: user.game_side_scroller
and mode: user.game
and not mode: sleep
-
game | menu:                user.game_side_scroller_toggle_menu_mode()
# settings():
#     user.game_noise_pop_binding_default = "move"
#     user.game_noise_hiss_binding_default = "long click"

# tag(): user.game_basic_movement
# tag(): user.game_camera_controls
# tag(): user.game_sprint_controls

# parrot(palate):             key(space)
# tag(): user.game_mouse_enabled
# tag(): user.game_map
# tag(): user.game_trade
# tag(): user.game_arrow_keys_toggle_wsad_movement
# tag(): user.game_quick_access_menu
# tag(): user.game_skills
# tag(): user.game_weapons
# tag(): user.game_tools
# tag(): user.game_weapon_aim

# noise binding exploration mode | noise explore | exploring:
#     user.game_noise_control_switch("pop","move")
#     user.game_noise_control_switch("hiss","long click")

# noise binding fight mode | noise fight | fighting:
#     user.game_noise_control_switch("pop","dodge")
#     user.game_noise_control_switch("hiss","long click")
