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

# @mod.action_class
# class Actions:
