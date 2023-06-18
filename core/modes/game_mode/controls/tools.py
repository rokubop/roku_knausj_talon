from talon import Module, actions, Context

mod = Module()
mod.list("game_tool_keyword")
ctx = Context()
ctx.lists["user.game_tool_keyword"] = {"tool", "trap"}


@mod.action_class
class Actions:

    def game_tool_use():
        """Use selected tool or trap, like in a souls-like game.
        As not every game has this mechanic, it's left blank to be overridden if needed."""
        return