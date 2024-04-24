from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def parrot_config_get_commands_text():
        """Get text of commands formatted in a list"""
        config = actions.user.parrot_config()
        commands = config.get("commands", {}) if "commands" in config else {k: v for k, v in config.items() if k != "options"}
        return [f"{command}: {action[0]}" for command, action in commands.items()]

    def parrot_config_show_commands():
        """Show the commands for the current parrot mode"""
        config = actions.user.parrot_config()
        actions.user.ui_textarea_show({
            "title": f"mode: {config.get('mode', '')}",
            "bg_color": config.get("color", "222666"),
            "align": "right",
            "text_lines": actions.user.parrot_config_get_commands_text()
        })

    def parrot_config_hide_commands():
        """Hide the commands for the current parrot mode"""
        actions.user.ui_textarea_hide()