from talon import Module

mod = Module()


@mod.action_class
class Crafting:

    def game_craft():
        """Craft an object.
        Not every game has crafting mechanics
        so this action is only there to be overridden if needed
        without having to declare a new voice command"""
        return