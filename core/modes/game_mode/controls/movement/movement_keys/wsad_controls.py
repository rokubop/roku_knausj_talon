from talon import Context, Module

module = Module()
module.tag("wsad_game_controls")
context = Context()
context.matches = """
tag: user.wsad_game_controls
"""
context.lists["user.game_directions"] = {
    "north": "w",
    "nor": "w",
    "no": "w",
    "south": "s",
    "so": "s",
    "west": "a",
    "wet": "a",
    "we": "a",
    "east": "d",
    "ease": "d",
    "aye": "d",
}


@context.action_class("user")
class Actions:

    def get_game_movement_keys():
        return ["w", "s", "a", "d"]
