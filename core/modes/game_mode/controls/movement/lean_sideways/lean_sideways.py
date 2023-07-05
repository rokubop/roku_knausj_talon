from talon import Module, Context, actions, ctrl

lean_direction = None
mod = Module()
mod.tag("game_lean_sideways")


@mod.action_class
class Actions:

    def game_lean_sideways(direction: str):
        """Lean left/right if not leaning currently.
        OR stop leaning left/right if leaning in the specified direction already.
        OR start leaning the other direction than leaning currently.

        This action does not handle any key presses by itself. It defaults to calling:
            actions.user.game_lean_left_start() 
            actions.user.game_lean_left_stop()
            actions.user.game_lean_right_start() 
            actions.user.game_lean_right_stop()
        
        This action's main purpose is to track current leaning state
        and being called upon the "lean left/right" voice commands
        (or their respective see/sir shorthand voice commands)
        to simplify and shorten movement voice commands,
        so that both starting and canceling leaning a certain direction can be done with the same voice command
        and changing leaning direction can also be done with the voice command for the opposite direction.

        This action should not be overridden.
        The actual key bindings should be done by overriding the following actions:
            actions.user.game_lean_left_start() 
            actions.user.game_lean_left_stop()
            actions.user.game_lean_right_start() 
            actions.user.game_lean_right_stop()
        """

        global lean_direction
        if not direction in ("left", "right"):
            return

        if direction == "left":
            if lean_direction is None:
                actions.user.game_lean_left_start()
            elif lean_direction == "left":
                actions.user.game_lean_left_stop()
                direction = None
            else:
                actions.user.game_lean_right_stop()
                actions.user.game_lean_left_start()
        else:
            if lean_direction is None:
                actions.user.game_lean_right_start()
            elif lean_direction == "right":
                actions.user.game_lean_right_stop()
                direction = None
            else:
                actions.user.game_lean_left_stop()
                actions.user.game_lean_right_start()

        lean_direction = direction

    def game_lean_sideways_stop():
        """Stop leaning left or right. Tracks leaning state. Should not be overridden.
        This action does not handle any key presses by itself. It defaults to calling:
            actions.user.game_lean_left_stop()
            actions.user.game_lean_right_stop()"""
        global lean_direction
        actions.user.game_lean_right_stop()
        actions.user.game_lean_left_stop()
        lean_direction = None

    def game_lean_left_start():
        """Start leaning left. Defaults to holding down q."""
        actions.key("q:down")

    def game_lean_left_stop():
        """Stop leaning left. Defaults to releasing q."""
        actions.key("q:up")

    def game_lean_right_start():
        """Start leaning right. Defaults to holding down e."""
        actions.key("e:down")

    def game_lean_right_stop():
        """Stop leaning right. Defaults to releasing e."""
        actions.key("e:up")
