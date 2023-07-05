from talon import actions, Module

mod = Module()


@mod.action_class
class QuickAccess:

    def game_number_shortcut(game_number_shortcuts: str):
        """Fast equip or fast use with shortcuts, usually number keys but will handle any keys by default."""
        actions.key(game_number_shortcuts)
        
    def game_heal():
        """Shortcut for healing.
        Not every game has healing or quick potion use shortcut
        so this action is only there to be overridden if needed
        without having to declare a new voice command.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_potion_drink():
        """Shortcut for potion drinking.
        Not every game has quick potion use shortcut
        so this action is only there to be overridden if needed
        without having to declare a new voice command.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0