from talon import Module, Context, actions, ctrl, ui

mod = Module()
ctx = Context()

mod.apps.factory_game = r"""
os: windows
and app.exe: FactoryGame-Win64-Shipping.exe
"""

ctx.matches = r"""
os: windows
app: factory_game
"""

@mod.action_class
class Actions:
    def virtual_keys_3x3(grid: dict):
        """Virtual keys"""
        x, y = ctrl.mouse_pos()
        screens = ui.screens()
        tile_width = screens[0].rect.width // 3
        tile_height = screens[0].rect.height // 3
        tile_index_x = x // tile_width + 1
        tile_index_y = y // tile_height + 1
        tile_key = str(int(tile_index_y * 3 - (3 - tile_index_x)))
        if grid.get(tile_key):
            grid[tile_key]()

# @ctx.action_class("user")
# class Actions:
    # def parrot_nn():
    #     print("'to execute parrot command'")
    #     if actions.user.mouse_move_curve_is_moving():
    #         actions.user.mouse_move_curve_stop()
    #     else:
    #         actions.user.virtual_keys_3x3({
    #             '1': lambda: actions.user.mouse_move_curve(180, 2, 700),
    #             '2': lambda: actions.user.mouse_move_curve(270, 1, 500),
    #             '3': lambda: actions.user.mouse_move_curve(0, 2, 700),
    #             '4': lambda: actions.user.mouse_move_curve(180, 2, 300),
    #             '5': lambda: actions.user.fps_move_forward_toggle(),
    #             '6': lambda: actions.user.mouse_move_curve(0, 2, 300),
    #             '7': lambda: actions.user.mouse_move_curve(180, 4, 200),
    #             '8': lambda: actions.user.mouse_move_curve(90, 1, 500),
    #             '9': lambda: actions.user.mouse_move_curve(0, 4, 200),
    #         })

# def turn_left_soft():
#     return {
#         "name": "turn left",
#         "action": actions.user.fps_turn_left
#     }

# def turn_right_soft():
#     return {
#         "name": "turn right",
#         "action": actions.user.fps_turn_right
#     }

# def stopper():
#     return {
#         "name": "stop",
#         "action": actions.user.fps_stop_layer
#     }

# def go():
#     return {
#         "name": "go",
#         "action": actions.user.fps_move_forward
#     }


# game_profile = {
#     "name": "game",
#     "auto_activate": False,
#     "commands": {
#         "nn": {
#             "region_3x3": {
#                 "4": turn_left_soft,
#                 "5": go,
#                 "6": turn_right_soft ,
#             }
#         },
#         'hiss': turn_left_soft,
#         'shush': turn_right_soft,
#         'ee': stopper
#     },
# }

# game_profile_b = {
#     "name": "game side b",
#     "commands": {
#         'hiss': turn_left_hard,
#         'shush': turn_right_hard
#     },
# }

# # here's what I think about the tags:
# # if I want to create global tags that any place can use, likely there would only be one level of context
# # when I'm in a context like a game or an interactive application, I will often be two levels of context deep
# #
# game_profile_c = {
#     "name": "game side c",
#     "group": "parrot",
#     "commands": {
#         'hiss': turn_left_continuous,
#         'shush': turn_right_continuous
#     },
# }

# actions.user.flex_pick([])
# actions.user.flex_use_profile(game_profile_b, use_once=True, timeout="1s")
# actions.user.flex_use_profile(game_profile_b, while_combo=True, timeout="1s")
# actions.user.flex_use_profile(game_profile_c, use_once=True)


# ctx.matches = r"""
# app: factory_game
# tag: user.flex_context
# tag: user.side_b
# """
# @ctx.action_class("user")
# class ParrotActions:
#     def parrot_ah():


# # I should be able to activate all modes with a manual command
# # flex none
# # flex global
# # flex contextp

# @mod.action_class
# class Actions:_
#     def flex_profile_game_satisfactory():
#         """Game profile for Satisfactory"""
#         return game_profile

# @ctx.action_class("user")
# class Actions:
#     def flex_profile():
#         return actions.user.flex_profile_game_satisfactory()Bluetooth