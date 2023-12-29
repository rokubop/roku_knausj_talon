from talon import Module, actions
from .typings import Profile, Command, CommandContinuous
from dataclasses import dataclass

class FlexProfileManager:

    def __init__(self, name):
        self.name: str = name
        self.profile_stack: list(str) = []
        self.profiles: dict[str, Profile] = {}

    def profile_activate(self, profile_name: str):
        print(f"self.profiles.keys(): {self.profiles.keys()}")
        if profile_name not in self.profiles:
            print(f"Profile {profile_name} not found")
            return

        if self.profile_stack:
            current_profile = self.profile_stack[0]
            if current_profile == profile_name:
                return

            print(f"stopping profile: {current_profile}")
            self.profiles[current_profile].on_stop()

        if profile_name in self.profile_stack:
            self.profile_stack.remove(profile_name)

        self.profile_stack.insert(0, profile_name)
        print(f"starting profile: {profile_name}")
        self.profiles[profile_name].on_start()
        print(f"self.profile_stack: {self.profile_stack}")

    def execute_flex_action(self, command_name):
        """Determine which profile to use and execute the action"""
        print("********************")
        print(f"flex_action: {command_name}")
        profile = actions.user.flex_profile()

        if not profile:
            print(f"profile not found for {command_name}")
            return

        if isinstance(profile, list):
            for p in profile:
                if p.name not in self.profiles:
                    self.profiles[p.name] = p
                    self.profile_stack.append(p.name)

            # we're getting the wrong profile here
            # we should be looking at the stack instead
            print(f"self.profile_stack: {self.profile_stack}")
            current = self.profile_stack[0]
            profile = self.profiles[current]


        print(f"profile.name: {profile.name}")
        print(f"activation_type: {profile.activation_type}")

        # make sure the profile is on the stack and bring to front if needed
        if profile.name not in self.profiles:
            self.profiles[profile.name] = profile

        if profile.activation_type == "auto":
            self.profile_activate(profile.name)

        current_profile = self.profiles[self.profile_stack[0]]

        command_name_root = command_name.split("_")[0]

        command = current_profile.commands[command_name_root]
        if isinstance(current_profile.commands[command_name_root], list):
            command = current_profile.commands[command_name_root][0]

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

flex_profile_manager = FlexProfileManager("flex_profile_manager")