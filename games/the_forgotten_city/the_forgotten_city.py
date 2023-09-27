from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.apps.the_forgotten_city = """
app.name: The Forgotten City
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: the_forgotten_city
"""
