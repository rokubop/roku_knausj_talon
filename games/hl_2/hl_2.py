from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.hl_2 = r"""
os: windows
and app.exe: hl2.exe
"""

ctx.matches = r"""
os: windows
app: hl_2
"""

# @mod.action_class
# class Actions:
