from talon import Module, actions
from .typings import Config, Command, CommandContinuous
from dataclasses import dataclass

mod = Module()

class FlexActionManager:
    configs = set()

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
        config = actions.user.flex_config()
        if not config:
            print(f"config not found for {command_name}")
            return
        print(f"config.name: {config.name}")
        print(f"activation_type: {config.activation_type}")
        if config.activation_type == "auto":
            command_name_root = command_name.split("_")[0]

            command = config.commands[command_name_root]
            if isinstance(config.commands[command_name_root], list):
                command = config.commands[command_name_root][0]

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
        elif config.activation_type == "manual":
            return

    def flex_config():
        """Flex config"""
        print("flex_config not implemented")
