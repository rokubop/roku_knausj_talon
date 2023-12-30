from typing import Union
from .typings import Profile, Command, CommandContinuous
from talon import actions

class FlexProfileManager:

    def __init__(self, name):
        self.name: str = name
        self.profile_name_stack: list(str) = []
        self.profiles: dict[str, Profile] = {}

    def get_name(self, profile):
        return profile['name'] if isinstance(profile, dict) else profile.name

    def add_profile(self, profile: Union[Profile, dict]):
        profile_name = self.get_name(profile)
        if profile_name not in self.profiles:
            profile = profile if isinstance(profile, Profile) else Profile(**profile)
            self.profiles[profile_name] = profile

        if profile.activation_type == "auto":
            self.profile_name_stack.append(profile_name)

    def ctx_profile(self):
        return actions.user.flex_profile()

    def current_profile_name(self):
        if self.profile_name_stack:
            return self.profile_name_stack[-1]
        return None

    def profile_activate(self, profile_name: str):
        print(f"self.profiles.keys(): {self.profiles.keys()}")
        if profile_name not in self.profiles:
            print(f"Profile {profile_name} not found")
            return

        if self.profile_name_stack:
            current_profile_name = self.current_profile_name()
            if current_profile_name == profile_name:
                return

            if self.profiles[current_profile_name].on_stop:
                print(f"stopping profile: {current_profile_name}")
                self.profiles[current_profile_name].on_stop()

        if profile_name in self.profile_name_stack:
            self.profile_name_stack.remove(profile_name)

        self.profile_name_stack.append(profile_name)
        print(f"starting profile: {profile_name}")
        if self.profiles[profile_name].on_start:
            self.profiles[profile_name].on_start()

        print(f"self.profile_name_stack: {self.profile_name_stack}")

    def execute_flex_action(self, command_name):
        """Determine which profile to use and execute the action"""
        print("********************")
        print(f"flex_action: {command_name}")
        profile_name = None
        profile = self.ctx_profile()

        if not profile:
            print(f"profile not found for {command_name}")
            return

        if isinstance(profile, list):
            for p in profile:
                profile_name = self.get_name(p)
                if profile_name not in self.profiles:
                    self.add_profile(p)
        else:
            profile_name = self.get_name(profile)
            if profile_name not in self.profiles:
                self.add_profile(profile)

        # we're getting the wrong profile here
        # we should be looking at the stack instead
        print(f"self.profile_name_stack: {self.profile_name_stack}")
        profile = self.profiles[self.current_profile_name()]

        print(f"profile.name: {profile.name}")
        print(f"activation_type: {profile.activation_type}")

        # make sure the profile is on the stack and bring to front if needed
        if profile.name not in self.profiles:
            self.profiles[profile.name] = profile

        if profile.activation_type == "auto":
            self.profile_activate(profile.name)

        current_profile_name = self.profiles[self.current_profile_name()]

        command_name_root = command_name.split("_")[0]

        command = current_profile_name.commands[command_name_root]
        if isinstance(current_profile_name.commands[command_name_root], list):
            command = current_profile_name.commands[command_name_root][0]

        if isinstance(command, Command):
            print("The object is an instance of Command")
            if command.action:
                return command.action()
        elif isinstance(command, CommandContinuous):
            print("The object is an instance of CommandContinuous")
            if "_stop" in command_name:
                return command.action_stop()
                return
            if command.action_start:
                return command.action_start()
        elif isinstance(command, dict):
            print("The object is an instance of dict")
            if command["action"]:
                print("Attempting to run action")
                return command["action"]()
            elif "_stop" in command_name:
                return command["action_stop"]()
                return
            elif command["action_start"]:
                return command["action_start"]()


flex_profile_manager = FlexProfileManager("flex_profile_manager")