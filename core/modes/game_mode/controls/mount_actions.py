from talon import actions, Module

mod = Module()
mod.tag("game_mount")


@mod.action_class
class Actions:

    def game_mount():
        """Begin mounted ride.
        Defaults to user.game_use if not overridden"""
        actions.user.game_use()

    def game_dismount():
        """Get off your high horse.
        Defaults to user.game_mount if not overridden."""
        actions.user.game_mount()

    def game_mount_ride_faster():
        """Defaults to user.game_switch_sprint(True) if not overridden."""
        actions.user.game_switch_sprint(True)

    def game_mount_ride_slower():
        """Defaults to user.game_switch_sprint(False) if not overridden."""
        actions.user.game_switch_sprint(False)

    def game_mount_stop():
        """Defaults to user.switch_game_movement(False) if not overridden."""
        actions.user.switch_game_movement(False)