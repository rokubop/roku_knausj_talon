from threading import Lock
from talon import actions, Module
from ....GameModeHelper import GameModeHelper

game_sprint_module = Module()

setting_hold_to_walk = game_sprint_module.setting(
    "game_sprint_hold_to_walk",
    type=bool,
    default=False,
    desc=
    """If true then the default sprint key will be held to walk instead of held to run."""
)
setting_default_sprint_state = game_sprint_module.setting(
    "game_sprint_state_default",
    type=bool,
    default=False,
    desc="""Helps in tracking the in-game sprint/walk state.
        See the comment on GameActions.game_sprint_state_reset() for more information.
        Sho5uld be set to true when the default in-game behavior is running instead of walking (e.g. in Antichamber).
        By default false.""")

game_sprint_module.tag("game_sprint_controls")

is_sprinting: bool = False


@game_sprint_module.action_class
class SprintActions:

    def game_switch_sprint(do_turn_on: bool = None):
        """If do_turn_on is True, start sprinting.
        If do_turn_on is is False, stop sprinting.
        If do_turn_on is None, the action toggles between sprinting/not sprinting, based on tracked sprint state.

        This action should be called instead of actions.user.game_sprint_start
        and actions.user.game_sprint_stop if any of those 2 get overridden.
        This action shouldn't be overridden. Doing so may desynchronize the tracked sprint state.

        This function does not handle any sprinting logic. It defaults to calling
        actions.user.game_sprint_start() or actions.user.game_sprint_stop().
        Its main purpose is to be called upon the shorthand "sprint"/"print" voice command
        instead of "sprint start" and "sprint done" to shorten the voice commands
        necessary for such a basic game interaction.

        Tracks sprint state independently of underlying action calls
        in case the main logic needs to be overridden."""
        global is_sprinting
        do_turn_on = not is_sprinting if do_turn_on is None else do_turn_on

        if do_turn_on:
            actions.user.game_sprint_start()
        else:
            actions.user.game_sprint_stop()

        is_sprinting = do_turn_on
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_sprint_start():
        """Start sprinting.
        Defaults to pressing down the shift key.
        May be overridden to implement custom sprint start game mechanic.
        Tracks sprint state if not overridden."""
        global is_sprinting
        if setting_hold_to_walk.get():
            actions.key("shift:up")
        else:
            actions.key("shift:down")
        is_sprinting = True  # in case game_switch_sprintgets overridden
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_sprint_stop():
        """Stop sprinting.
        Defaults to releasing the shift key.
        May be overridden to implement custom sprint stop game mechanic.
        Tracks sprint state if not overidden."""
        global is_sprinting
        if setting_hold_to_walk.get():
            actions.key("shift:down")
        else:
            actions.key("shift:up")
        is_sprinting = False  # in case game_switch_sprintgets overridden
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_start_running():
        """Start running. Defaults to calling actions.user.game_switch_sprint(True)
        as in most games running means the same as sprinting.
        May be overridden to implement custom running game mechanic."""
        actions.user.game_switch_sprint(True)

    def game_start_walking():
        """Stop running. Defaults to calling actions.user.game_switch_sprint(False)
        as in most games walking means not sprinting.
        May be overridden to implement custom walking game mechanic."""
        actions.user.game_switch_sprint(False)

    def game_sprint_state_reset():
        """Resets is_sprinting to default"""
        global is_sprinting
        is_sprinting = setting_default_sprint_state.get()
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)
