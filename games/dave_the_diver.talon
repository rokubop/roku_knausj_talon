app: dave_the_diver
and mode: user.game
and not mode: sleep
-
settings():
    key_hold = 64.0
    key_wait = 16.0
    user.mouse_hold = 64000
    user.mouse_wait = 0
    # user.mouse_enable_pop_click = 0
    # user.mouse_hide_mouse_gui = 1
    # user.game_noise_pop_binding_default = "move"
    # user.game_noise_hiss_binding_default = "long click"
    # user.game_turn_around_mouse_delta = 2850
    # user.game_turn_horizontally_mouse_delta = 600
    # user.game_turn_vertically_mouse_delta = 600
    # user.game_noise_pop_binding_default = "mouse_click_1"
    # user.game_noise_pop_binding_default = "click"
    # user.game_noise_hiss_binding_default = "right long click"
    # user.game_noise_hiss_binding_default = "jump"
    # user.game_sprint_hold_to_walk = False
    # user.game_sprint_state_default = False

# tag(): user.game_action_rpg

# go/stop/direction
tag(): user.game_basic_movement

# north, south, east, west
tag(): user.game_basic_movement_arrows

# toggles hold for arrow keys
tag(): user.game_arrow_keys_toggle_wsad_movement

#  walk/run/sprint
tag(): user.game_sprint_controls

#  walk/run/sprint
tag(): user.wsad_game_controls


tag(): user.game_mouse_enabled

# noise binding exploration mode | noise explore | exploring:
# 	user.("pop","move")
# 	user.game_noise_control_switch("hiss","long click")

# for move I want to say go.
# while going in a certain direction I want to be shift up or down or right or left a little bit
# I want to be able to toggle a shift or not
# I need a command for left attack
# I need a command for harpoon
#

# noise set:
#     user.game_noise_control_switch("pop","click")
#     user.game_noise_control_switch("hiss","right long click")

# parrot.pop():               mouse_click(0)

# parrot(pop):                user.game_click(0)
# hello:                      user.game_click(0)
parrot(pop):                user.dave_mouse_click(0)
parrot(palete_click):       user.dave_mouse_click(0)
hello:                      user.dave_mouse_click(0)
# test:                       mouse_click(0)
test:                       user.dave_mouse_click(0)
# test:                       user.dave_test()

<user.key>:                 key(key)
harp:
    user.mouse_drag(1)

swim | slow | slower:       user.game_start_walking()
fast | faster | phelps:
    user.game_start_running()

shot:
    user.dave_mouse_click(0)
    user.mouse_drag_end()

swap$:
    print("command mode")
    mode.disable("sleep")
    mode.disable("dictation")
    mode.disable("user.game")
    mode.enable("command")
    key(alt:down)
    key(tab)
    sleep(50ms)
    key(alt:up)

# [go] (fast | faster) | run:
#     user.switch_game_movement(0)
#     key(w)
#     user.switch_game_movement(1)
# [go] (slow | slower) | walk:
#     user.switch_game_movement(0)
#     user.switch_game_movement(1)
(small | short) {user.game_directions}: user.hold_game_key(game_directions, "700ms")
long {user.game_directions}: user.hold_game_key(game_directions, "1300ms")
longer {user.game_directions}: user.hold_game_key(game_directions, "2000ms")
small (<user.key>):         user.hold_game_key(key, "700ms")
long (<user.key>):          user.hold_game_key(key, "1300ms")
longer (<user.key>):        user.hold_game_key(key, "2000ms")
hold (<user.key>):          user.hold_game_key(key)
# horse go:                   user.rdr_horse_run()
# horse stop:                 user.rdr_horse_stop()
# ^retry$:                    user.hold_game_key("enter", "2000ms")
# ^restart$:                  user.hold_game_key("space", "2000ms")
# (release | real | don't) (<user.key>): user.release_game_key(key)
# (release | real | don't) all: user.release_held_game_keys()
# loot:                       user.hold_game_key("r", "700ms")
# skip scene:                 user.hold_game_key("space", "2s")
# cancel:                     user.release_held_game_keys()
# whistle:                    key(h)
# path:                       mouse_click(2)
