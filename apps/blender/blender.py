from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.blender = r"""
os: windows
and app.exe: blender.exe
"""
ctx.matches = r"""
os: windows
app: blender
"""

# @mod.action_class
# class Actions:
