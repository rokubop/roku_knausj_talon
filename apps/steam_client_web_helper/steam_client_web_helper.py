from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.steam_client_web_helper = r"""
os: windows
and app.exe: steamwebhelper.exe
"""
ctx.matches = r"""
os: windows
app: steam_client_web_helper
"""
# @mod.action_class
# class Actions:
