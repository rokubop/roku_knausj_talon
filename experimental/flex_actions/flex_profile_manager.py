from .typings import Profile, Command, CommandContinuous
from talon import actions

class FlexProfileManager:

    def __init__(self, name):
        self.name: str = name
        self.profile_name_stack: list[str] = []
        self.profiles: dict[str, Profile] = {}

    def use_profile(self, profile_name: str):
        """Alias for profile_activate"""
        self.profile_activate(profile_name)

    def ctx_profile(self) -> Profile | list[Profile]:
        return actions.user.flex_profile()

    def current_profile_name(self):
        if self.profile_name_stack:
            return self.profile_name_stack[-1]
        return None

    def get_active_profile(self):
        if self.profile_name_stack:
            profile_name = self.profile_name_stack[-1]
            return self.profiles[profile_name]
        return None


    def _add_new_profiles(self, profile: Profile | list[Profile]):
        if isinstance(profile, list):
            for p in profile:
                profile_name = p["name"]
                if profile_name not in self.profiles:
                    self.profiles[profile_name] = p
        else:
            profile_name = profile["name"]
            if profile_name not in self.profiles:
                self.profiles[profile_name] = profile


    def profile_activate(self, profile_name: str):
        # print(f"self.profiles.keys(): {self.profiles.keys()}")
        print(f"profile_named: ", profile_name)
        if profile_name not in self.profiles:
            print(f"Profile {profile_name} not found")
            return

        active_profile = self.get_active_profile()
        if active_profile:
            if active_profile.get('name') == profile_name:
                return

            if active_profile.get('on_stop'):
                print(f"stopping profile: {active_profile.get('name')}")
                active_profile["on_stop"]()

        if profile_name in self.profile_name_stack:
            self.profile_name_stack.remove(profile_name)

        self.profile_name_stack.append(profile_name)
        profile = self.profiles[profile_name]
        if profile.get('on_start'):
            print(f"starting profile: {profile_name}")
            profile["on_start"]()

        print(f"self.profile_name_stack: {self.profile_name_stack}")

    def execute_flex_action(self, command_name):
        """Determine which profile to use and execute the action"""
        print("********************")
        print(f"flex_action: {command_name}")
        profile = self.ctx_profile()

        if not profile:
            print(f"profile not found for {command_name}")
            return

        # First, we need to check if we should add the profile.
        self._add_new_profiles(profile)

        # Next we need to determine if we should add it to the stack
        #  Basically, we just check for auto-activate.
        relevant_profile = profile[0] if isinstance(profile, list) else profile
        if relevant_profile.get('auto_activate') is not False:
            self.use_profile(relevant_profile.get('name'))

        active_profile = self.get_active_profile()

        #  Once the stack is all set up, we just execute the action


        # print(f"self.profile_name_stack: {self.profile_name_stack}")
        # profile = self.profiles[self.current_profile_name()]

        # print(f"profile.name: {profile['name']}")
        # print(f"auto_activate: {profile['auto_activate']}")

        # current_profile_name = self.profiles[self.current_profile_name()]

        command_name_root = command_name.split("_")[0]

        command = active_profile['commands'][command_name_root]
        if isinstance(command, list):
            command = command[0]

        if command.get('action'):
            return command["action"]()
        elif "_stop" in command_name:
            return command["action_stop"]()
            return
        elif command.get('action_start'):
            return command["action_start"]()


flex_profile_manager = FlexProfileManager("flex_profile_manager")