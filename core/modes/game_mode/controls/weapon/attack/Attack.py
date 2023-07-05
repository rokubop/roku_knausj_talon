from talon import actions, Module

mod = Module()


@mod.action_class
class Attack:
#weapon?
    def game_attack(is_held: bool = None):
        """Perform a primary attack. Defaults to LMB.
        If is_held is None, defaults to a single click.
        If is_held is True, holds down LMB.
        If is_held is False, releases LMB."""
        if is_held is None:
            actions.user.game_click(0)
        else:
            actions.user.game_press_mouse(is_held)

    def game_stealth_kill():
        """Perform a stealth kill.
        No binding by default, needs to be overridden if needed.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_stealth_choke():
        """Perform a non-lethal elimination.
        No binding by default, needs to be overridden if needed.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0