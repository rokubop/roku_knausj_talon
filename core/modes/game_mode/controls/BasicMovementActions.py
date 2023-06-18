from threading import Lock
from talon import actions, Module

game_movement_module = Module()

setting_default_movement_direction = game_movement_module.setting(
    "game_default_movement_key",
    type=str,
    default="w",
    desc="""Default movement key.
    Can be modified so that you don't have to issue the movement direction change command
    by voice after launching the game every time.""")

game_movement_module.list("game_directions")
game_movement_module.tag("game_basic_movement")

# TODO get current user.game_directions list according to the active context
current_game_movement_direction_key: str = None
is_moving: bool = False
lock_is_moving = Lock()


def _nullify_current_movement_direction_key():
    current_game_movement_direction_key = None


def _start_game_movement():
    """Start moving in game direction. Not thread safe."""
    global is_moving, current_game_movement_direction_key
    if current_game_movement_direction_key is None:
        current_game_movement_direction_key = setting_default_movement_direction.get()
    actions.user.hold_game_key(current_game_movement_direction_key)
    is_moving = True


def _stop_game_movement():
    """Stop in-game movement by releasing all movement keys (according to the active context). Not thread safe."""
    global is_moving
    directions = actions.user.get_game_movement_keys()
    for key in directions:
        actions.user.release_game_key(key)
    is_moving = False


def _set_game_movement_direction(new_direction_key: str):
    """Sets the key currently used to move in game. Not thread safe."""
    global current_game_movement_direction_key
    current_game_movement_direction_key = new_direction_key


def _switch_game_movement(do_turn_on: bool = None):
    do_turn_on = not is_moving if do_turn_on is None else do_turn_on
    if do_turn_on:
        _start_game_movement()
    else:
        _stop_game_movement()


def _switch_game_movement_direction(direction_key: str):
    _set_game_movement_direction(direction_key)
    if is_moving:
        _stop_game_movement()
        _start_game_movement()

@game_movement_module.action_class
class GameActions:

    def switch_game_movement(do_turn_on: bool = None):
        """toggle or switch game movement on/off. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            _switch_game_movement(do_turn_on)

    def set_game_movement_direction(new_direction: str):
        """Sets the key currently used to move in game. Thread safe."""
        global lock_is_moving
        with lock_is_moving:
            _set_game_movement_direction(new_direction)

    def switch_game_movement_direction(new_direction: str):
        """Switches the key currently used to move in game. Continues moving in the new direction if movement is active. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            _switch_game_movement_direction(new_direction)

    def game_movement_toggle_direction_switch(direction_key: str):
        """Start movement in the given direction if not moving
        or stop movement if the direction is equal to the current direction and moving
        or change the current direction while continuing movement."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            if direction_key == current_game_movement_direction_key:
                _switch_game_movement()
            else:
                _switch_game_movement_direction(direction_key)


    def get_game_movement_keys():
        """this method must be overridden with game-specific contexts
        unless the game movement is the standard WSAD

        It should return the same list of values
        as the context for the specific game
        stores under context.lists['user.game_directions']
        until talon allows to obtain the list directly
        """
        # TODO get current user.game_directions list according to the active context
        # Or create tags or different types of movement controls: arrows
        # and apply contexts for them specificly, overriding this method too
        return []

    def game_movement_state_reset():
        """Resets is_moving to False
        in case the game overrides movement behavior
        after, for example, a loading screen
        or the user exits the game (or the game mode) without stopping the movement
        which would mess up the execution of 'go' and 'stop' commands
        with the default game_switch_movement()"""
        global is_moving, lock_is_moving
        with lock_is_moving:
            is_moving = False
