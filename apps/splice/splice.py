from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.splice = r"""
os: windows
and app.exe: /Splice.exe/i
"""

ctx.matches = r"""
os: windows
app: splice
"""

# @mod.action_class
# class Actions:
