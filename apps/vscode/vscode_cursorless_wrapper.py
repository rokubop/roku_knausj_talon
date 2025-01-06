from talon import Module, Context, actions
from typing import Any

mod = Module()
ctx = Context()
ctx.matches = r"""
app: vscode
tag: user.cursorless
"""

last_action_name = None

@ctx.action_class("user")
class Actions:
    def cursorless_command(action_name, target):
        global last_action_name
        last_action_name = action_name
        actions.next(action_name, target)

@mod.action_class
class Actions:
    def cursorless_command_again(target: Any):
        """Repeat the last cursorless command on a new target"""
        global last_action_name
        actions.user.cursorless_command(last_action_name, target)
