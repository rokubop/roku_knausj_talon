from talon import Context, Module

module = Module()
module.tag("game_basic_movement_arrows")
context = Context()
context.matches = """
tag: user.game_basic_movement_arrows
"""
context.lists["user.game_directions"] = {
    "north": "up",
    "nor": "up",
    "no": "up",
    "south": "down",
    "so": "down",
    "west": "left",
    "wet": "left",
    "we": "left",
    "east": "right",
    "ease": "right",
    "aye": "right",
}


@context.action_class("user")
class Actions:

    def get_game_movement_keys():
        return ["up", "down", "left", "right"]
