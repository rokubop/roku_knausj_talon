from talon import Module, Context, actions, ctrl

is_weapon_block: bool = False
mod = Module()
mod.tag("game_weapon_block")


@mod.action_class
class Actions:

    def game_weapon_block_toggle(is_block: bool = None):
        """If is_block is True, start blocking.
        If is_block is is False, stop blocking.
        If is_block is None, the action toggles between blocked/not blocked, based on tracked blocking state.

        This action does not handle any presses by itself. It defaults to calling
        actions.user.game_weapon_block_start() or actions.user.game_weapon_block_stop().
        Its main purpose is to be called upon the shorthand "block" voice command
        to simplify and shorten voice commands during a fight
        by being able to use the same voice command for toggling blocking on and off.

        Tracks blocking state independently of underlying action calls
        in case the main logic needs to be overridden."""
        if is_block is None:
            is_block = not is_weapon_block

        if is_block:
            actions.user.game_weapon_block_start()
        else:
            actions.user.game_weapon_block_stop()

        actions.user.game_weapon_block_state_set(is_block)

    def game_weapon_block_start():
        """Start blocking. Doesn't track blocking state.
        Needs to be overwritten with the game-specific binding.
        Doesn't do anything by default, as there is no universal blocking binding in games
        and this is not a mechanic all games have.
        Return value does not matter. Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_weapon_block_stop():
        """Stops blocking. Doesn't track blocking state.
        Needs to be overwritten with the game-specific binding.
        Doesn't do anything by default, as there is no universal blocking binding in games
        and this is not a mechanic all games have.
        Return value does not matter. Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_weapon_block_state_set(is_block: bool):
        """Used to track the state of blocking.
        Helps at toggling block on and off with the same voice command.
        Shouldn't be overridden. May be used when overriding blocking logic."""
        global is_weapon_block
        is_weapon_block = is_block

    def game_get_is_block():
        """Returns current blocking state.
        May be used when overriding blocking logic or noise&blocking logic, e.g.
        when additional actions need to be called inside
        game_before_on_hiss() or game_after_on_hiss()."""
        return is_weapon_block


ctx = Context()
ctx.matches = """
tag: user.game_weapon_block
and mode: user.game
"""


@ctx.action_class("user")
class UserActions:

    def game_before_on_hiss():
        if is_weapon_block:
            actions.user.game_weapon_block_stop()  # let your guard down to attack
            # but do not change the block state as game_weapon_block_toggle would do
            # this will tell game_after_on_hiss to return to blocking
        return (True, True)

    def game_after_on_hiss():
        if is_weapon_block:
            #if blocking previously, return to blocking after the attack
            actions.user.game_weapon_block_start()