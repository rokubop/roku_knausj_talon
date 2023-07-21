from talon import Context, Module, actions, ctrl

mod = Module()
ctx = Context()

mod.apps.audacity = """
os: windows
and app.app: Audacity® Cross-Platform Sound Editor
"""

# @mod.action_class
# class Actions:
