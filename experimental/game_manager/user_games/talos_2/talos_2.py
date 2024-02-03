from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.talos_2 = r"""
os: windows
and app.exe: Talos2-Win64-Shipping.exe
"""

ctx.matches = r"""
os: windows
app: talos_2
"""

# @mod.action_class
# class Actions:
