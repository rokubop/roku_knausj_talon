tag: user.game_sprint_controls
and mode: user.game
-
(sprint | print) [toggle]:
    user.game_switch_sprint()
(sprint | print) start:
    user.game_switch_sprint(1)
(sprint | print) done:
    user.game_switch_sprint(0)
run [toggle]:
    user.game_start_running()
walk [toggle]:
    user.game_start_walking()