from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.v_l_c_media_player = r"""
os: windows
and app.exe: vlc.exe
"""
ctx.matches = r"""
os: windows
app: v_l_c_media_player
"""
# @mod.action_class
# class Actions:
