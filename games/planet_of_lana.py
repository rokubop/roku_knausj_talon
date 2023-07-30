from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.apps.planet_of_lana = """
win.title: Planet of Lana
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: planet_of_lana
"""