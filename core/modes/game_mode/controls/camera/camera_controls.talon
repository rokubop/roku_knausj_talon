tag: user.game_camera_controls
and mode: user.game
-
[cam] [turn] {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}')
[cam] [turn] (tiny | tea) {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}', 0.25)
[cam] [turn] (little | lil | lee | small) {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}', 0.5)
[cam] [turn] (big | be) {user.game_camera_direction}:
    user.game_turn_camera('{game_camera_direction}', 1.25)
[cam] [turn] (around | round) | turn:
    user.game_turn_camera_around()

[cam] first person [switch | toggle]:
    user.game_camera_first_person()
[cam] third person [switch | toggle]:
    user.game_camera_third_person()
