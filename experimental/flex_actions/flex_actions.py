from talon import Module, actions
from .typings import Profile, Command, CommandContinuous
from dataclasses import dataclass
from .flex_profile_manager import flex_profile_manager

mod = Module()

@mod.action_class
class Actions:
    def flex_action(command_name: str, group_name: str = None):
        """
        Manage a command through FlexActions. Only define this once per command.

        Suitable for parrot/noises, foot pedals,
        gamepads, and anything with a fixed amount of inputs

        ```
        parrot(pop): user.flex_action("pop")
        parrot(hiss): user.flex_action("hiss")
        parrot(hiss:stop): user.flex_action("hiss_stop")

        pedal(left): user.flex_action("left_pedal")

        gamepad(a): user.flex_action("gamepad_a")
        ```
        """
        flex_profile_manager.execute_flex_action(command_name)


    def flex_profile():
        """Flex profile"""
        print("flex_profile not implemented")

    def flex_use_profile(profile_name: str):
        """
        Push a profile to the top of the stack

        AKA make it the active profile
        """
        print("do flex_profile_push")
        flex_profile_manager.use_profile(profile_name)

    def flex_profile_pop():
        """ Pop a profile off the stack """
        print("do flex_profile_pop")