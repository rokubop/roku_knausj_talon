from talon import actions, Module

mod = Module()


@mod.action_class
class Interactions:

    def game_take():
        """Take an object. Defaults to user.game_use if not overridden."""
        actions.user.game_use()

    def game_take_number(digits: int):
        """Take a specified number of objects.
        Defaults to calling user.game_take() the specified number of times."""
        for i in range(digits):
            actions.user.game_take()

    def game_take_all():
        """Take all selected objects. Defaults to user.game_take() if not overridden."""
        actions.user.game_take()
   
    def game_loot():
        """Loot an object. Defaults to user.game_use if not overridden."""
        actions.user.game_use()

    def game_talk():
        """Talk to an NPC.
        Defaults to user.game_use if not overridden."""
        actions.user.game_use()    

    def game_interactable_objects_highlight_start():
        """Highlight interactable objects, defaults to pressing tab."""
        actions.key("tab")

    def game_interactable_objects_highlight_stop():
        """Stop highlighting interactable objects.
        Defaults to calling actions.user.game_interactable_objects_highlight_start()."""
        actions.user.game_interactable_objects_highlight_start()

    def game_use():
        """Basic use/interact with an object (e by default)"""
        actions.key("e")

    def game_long_use():
        """Hold use/interact key (e by default) for approximately half a second"""
        actions.user.game_hold_key_native("e", 650000)

    def game_hold_use():
        """hold use/interact key indefinitely (e by default)"""
        actions.key("e:down")

    def game_release_use():
        """release use/interact key (e by default)"""
        actions.key("e:up")