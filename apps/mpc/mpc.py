from talon import Context, Module, actions, ctrl

mod = Module()
ctx = Context()

mod.apps.mpc = """
os: windows
and app.app: MPC-BE x64
"""

# @mod.action_class
# class Actions:
