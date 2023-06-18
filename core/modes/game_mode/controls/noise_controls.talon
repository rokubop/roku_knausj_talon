mode: user.game
and not mode: sleep
-
^[controls | noise] {user.game_noises} {user.game_noise_controls}$:
    user.game_noise_control_switch(game_noises, game_noise_controls)
^[controls] noise reset$:
    user.game_noise_control_reset() 