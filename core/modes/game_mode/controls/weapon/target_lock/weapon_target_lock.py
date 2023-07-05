from talon import Module, Context, actions, ctrl

is_weapon_target_lock: bool = False
mod = Module()
mod.tag("game_weapon_target_lock")


@mod.action_class
class Actions:

    def game_weapon_target_lock_toggle(is_target_lock: bool = None):
        """If is_target_lock is True, lock the target.
        If is_target_lock is is False, release target lock.
        If is_target_lock is None, the action toggles between target locked/not locked, based on tracked target locking state.

        This function does not handle any target locking logic. It defaults to calling
        actions.user.game_weapon_target_lock_start() or actions.user.game_weapon_target_lock_stop().
        Its main purpose is to be called upon the shorthand "tar" voice command
        to simplify and shorten voice commands during a fight.

        Tracks target locking state."""
        global is_weapon_target_lock
        if is_target_lock is None:
            is_target_lock = not is_weapon_target_lock

        if is_target_lock:
            actions.user.game_weapon_target_lock_start()
        else:
            actions.user.game_weapon_target_lock_stop()

        is_weapon_target_lock = is_target_lock

    def game_weapon_target_lock_start():
        """Start target locking.
        Doesn't default to any key, needs overwriting to suit a specific game control scheme.
        The returned value does not matter, it is only there to stop talon from outputting errors to log."""
        return 0

    def game_weapon_target_lock_stop():
        """Stops target locking (releases RMB).
        Defaults to calling game_weapon_target_lock_start()."""
        actions.user.game_weapon_target_lock_start()

    def game_is_weapon_target_lock():
        """"""
        return is_weapon_target_lock