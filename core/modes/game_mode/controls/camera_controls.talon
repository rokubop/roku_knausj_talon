tag: user.game_camera_controls
and mode: user.game
-
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