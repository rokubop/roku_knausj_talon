from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.blue_stacks = r"""
os: windows
and app.exe: HD-Player.exe
"""

ctx.matches = r"""
os: windows
app: blue_stacks
"""

# @mod.action_class
# class Actions:
