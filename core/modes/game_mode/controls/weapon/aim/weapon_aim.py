from talon import Module, Context, actions, ctrl

is_weapon_aim: bool = False
mod = Module()
mod.tag("game_weapon_aim")


@mod.action_class
class Actions:

    def game_weapon_aim_toggle(is_aim: bool = None):
        """If is_aim is True, start aiming.
        If is_aim is is False, stop aiming.
        If is_aim is None, the action toggles between aimed/not aimed, based on tracked aiming state.

        This function does not handle any aiming logic. It defaults to calling
        actions.user.game_weapon_aim_start() or actions.user.game_weapon_aim_stop().
        Its main purpose is to be called upon the shorthand "aim" voice command
        to simplify and shorten voice commands during a fight.

        Tracks aiming state independently of underlying action calls
        in case the main logic needs to be overridden."""
        global is_weapon_aim
        if is_aim is None:
            is_aim = not is_weapon_aim

        if is_aim:
            actions.user.game_weapon_aim_start()
        else:
            actions.user.game_weapon_aim_stop()

        is_weapon_aim = is_aim

    def game_weapon_aim_start():
        """Start aiming.
        It defaults to pressing down the right mouse button.
        Tracks aiming state."""
        global is_weapon_aim
        actions.user.game_press_mouse(1, True)
        is_weapon_aim = True  #in case game_weapon_aim_toggle is overridden

    def game_weapon_aim_stop():
        """Stops aiming (releases RMB). Releases firing button (LMB).
        Tracks aiming state."""
        global is_weapon_aim
        actions.user.game_press_mouse(1, False)
        actions.user.game_press_mouse(0, False)
        is_weapon_aim = False  #in case game_weapon_aim_toggle is overridden

    def game_is_weapon_aim():
        """"""
        return is_weapon_aim