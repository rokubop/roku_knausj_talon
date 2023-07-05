from talon import actions, Module, ctrl

mod = Module()


@mod.action_class
class MiscellaneousMovement():
    def game_jump(is_hold: bool = None):
        """if is_hold is not provided or None, perform a basic jump.
        If is_hold is True, press the jump key down indefinitely
        If is_hold is False, release the jump key.
        Key defaults to space."""
        if is_hold is None:
            actions.key("space")
        else:
            ctrl.key_press("space", down=is_hold, up=not is_hold)

    def game_crouch():
        """Duck or crouch"""
        actions.key("c")

    def game_dodge():
        """Dodge roll. Defaults to pressing ctrl."""
        actions.key("ctrl")

    def game_long_dodge():
        """Long dodge roll. Defaults to pressing the ctrl key for 650 milliseconds."""
        actions.user.press_game_key("ctrl", 1, 650000)

    def game_dive_start():
        """Start diving"""
        actions.key("ctrl:down")

    def game_dive_stop():
        """Stop diving"""
        actions.key("ctrl:up")