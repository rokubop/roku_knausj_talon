from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.octopath_traveler_2 = r"""
os: windows
and app.exe: /Octopath_Traveler2-Win64-Shipping.exe/i
"""
ctx.matches = r"""
os: windows
app: octopath_traveler_2
"""

@ctx.action_class
class Actions:
    def on_tut():
        actions.key("c")