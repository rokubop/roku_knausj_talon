app: Red Dead Redemption 2
and mode: user.game
-
settings():
    key_hold = 64.0
    key_wait = 16.0
    user.game_turn_around_mouse_delta = 2850
    user.game_turn_horizontally_mouse_delta = 600
    user.game_turn_vertically_mouse_delta = 600
    # user.game_sprint_hold_to_walk = False
    # user.game_sprint_state_default = False


# tag(): user.game_action_rpg
# tag(): user.first_person_game_controls
# tag(): user.game_mouse_enabled
# tag(): user.game_map
# tag(): user.game_trade
# tag(): user.game_arrow_keys_toggle_wsad_movement
# tag(): user.game_quick_access_menu
# tag(): user.game_mount
# tag(): user.game_skills
# tag(): user.game_weapons
# tag(): user.game_tools<>
# tag(): user.game_weapon_aim
# tag(): user.game_basic_movement
tag(): user.game_camera_controls
# tag(): user.game_sprint_controls

<user.letter>:              key("{letter}")

swap():                     key(alt-tab)

hold <user.letter>:         key("{letter}:down")
stop <user.letter>:         key("{letter}:up")

crouch | stand:             key(ctrl)
skip:
    key("space:down")
    sleep(500ms)
    key("space:up")

short <user.letter>:
    key("{letter}:down")
    sleep(500ms)
    key("{letter}:up")

long <user.letter>:
    key("{letter}:down")
    sleep(1000ms)
    key("{letter}:up")

go | north:
    key("w:down")

stop:
    key("w:up")
    key("s:up")
    key("a:up")
    key("d:up")
    key("space:up")

# jump:
#     user.game_jump()
# crouch | duck:
#     user.game_crouch()
# roll | dodge | doo:
#     user.game_dodge()
# long roll | long dodge | [sausage] dog:
#     user.game_long_dodge()
# dive:
#     user.game_dive_start()
# dive done:
#     user.game_dive_stop()

# basic user interface
map show:
    user.game_map_show()
# (inventory | equipment | bag) [show]:
#     user.game_inventory_show()
# (character sheet | car sheet) [show]:
#     user.game_character_sheet_show()
(journal | quest log) [show]:
    user.game_quest_log_show()

[camera] [turn] {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}')
[camera] [turn] (tiny | tea) {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}', 0.25)
[camera] [turn] (little | lil | lee | small) {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}', 0.5)
[camera] [turn] (big | be) {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}', 1.25)
[camera] [turn] (around | round) | turn:
    user.game_turn_camera_around()

[camera] first person [switch | toggle]:
    user.game_camera_first_person()
[camera] third person [switch | toggle]:
    user.game_camera_third_person()
