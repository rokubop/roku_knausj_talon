from talon import Module, actions
from .typings import Profile, Command, CommandContinuous
from dataclasses import dataclass

mod = Module()

class FlexProfileManager:

    def __init__(self, name):
        self.name: str = name
        self.profile_stack: list(str) = []
        self.profiles: dict[str, Profile] = {}

    def profile_push(self, profile_name: str):
        if profile_name not in self.profiles:
            print(f"Profile {profile_name} not found")
            return

        if self.profile_stack:
            current_profile = self.profile_stack[0]
            self.profiles[current_profile].on_stop()

        if profile_name in self.profile_stack:
            self.profile_stack.remove(profile_name)

        self.profile_stack.insert(0, profile_name)
        self.profiles[profile_name].on_start()


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
        print("********************")
        print(f"flex_action: {command_name}")
        profile = actions.user.flex_profile()
        if not profile:
            print(f"profile not found for {command_name}")
            return
        print(f"profile.name: {profile.name}")
        print(f"activation_type: {profile.activation_type}")
        if profile.activation_type == "auto":
            command_name_root = command_name.split("_")[0]

            command = profile.commands[command_name_root]
            if isinstance(profile.commands[command_name_root], list):
                command = profile.commands[command_name_root][0]

            elif isinstance(command, Command):
                print("The object is an instance of Command")
                if command.action:
                    command.action()
            elif isinstance(command, CommandContinuous):
                print("The object is an instance of CommandContinuous")
                if "_stop" in command_name:
                    command.action_stop()
                    return
                if command.action_start:
                    command.action_start()
            return
        elif profile.activation_type == "manual":
            return

    def flex_profile():
        """Flex profile"""
        print("flex_profile not implemented")

    def flex_profile_push(profile_name: str):
        """
        Push a profile to the top of the stack

        AKA make it the active profile
        """
        # I need a profile manager
        # every time command is run,
        # it checks with the manager to see if it
        # already has the profile
        # otherwise it will add it
        print("do flex_profile_push")

    def flex_profile_pop():
        """ Pop a profile off the stack """
        print("do flex_profile_pop")