from talon import Module, Context, actions

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

# game_profile = {
#     "name": "game",
#     "auto_activate": False,
#     "commands": {
#         'hiss': {
#             "name": "turn left",
#             "action": actions.user.fps_turn_left
#         },
#         'shush': {
#             "name": "turn right",
#             "action": actions.user.fps_turn_right
#         },
#         'ee': {
#             "name": "stop",
#             "action": actions.user.fps_stop_layer
#         }
#     },
# }

@ctx.action_class("user")
class Actions:
    # def flex_profile():
    #     return game_profile