from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.manifold_garden = r"""
os: windows
and app.exe: ManifoldGarden.exe
"""
ctx.matches = r"""
os: windows
app: manifold_garden
"""
# @mod.action_class
# class Actions:
