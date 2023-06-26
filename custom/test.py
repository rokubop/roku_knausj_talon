from talon import Module, Context, actions

mod = Module()
ctx = Context()

ctx.matches = """
app: chrome
"""

# @mod.action_class
@mod.action_class
class Actidsfosdffefewwefefws:
    def test_one():
        """test"""
        actions.insert('yo')

@ctx.action_class("user")
class Totorsfwefewfewfewfewo:
    def test_one():
        """test"""
        actions.insert('helloa')