from talon import Module, Context, actions, ui

mod = Module()
ctx = Context()

# ctx.matches = """
# app: /steam/
# """

# @mod.action_class
@mod.action_class
class Actions:
    def test_one():
        """test"""
        # actions.core.repeat_phrase()
        print(ui.active_window())

    def test_two():
        """test"""
        actions.key('down')

# @ctx.action_class("user")
# class UserActions:
#     def test_one():
#         """test"""
#         actions.insert('helloa')