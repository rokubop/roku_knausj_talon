from talon import Module, actions, cron
mod = Module()

def get_base_noise(noise):
    """The part before colon or @ e.g.'pop' in 'pop:debounce-170' or 'pop@top'"""
    base_noise = noise.split(':')[0].split('@')[0]
    return base_noise.strip()

def is_prefix_of_other(cmd):
    return any(other_cmd.startswith(f"{cmd} ") and other_cmd != cmd for other_cmd in commands)

def categorize_commands(commands):
    """Determine immediate vs delayed commands"""
    immediate_commands = {}
    delayed_commands = {}
    base_noise_set = set()
    base_noise_map = {}

    for noise in commands.keys():
        base_noise = get_base_noise(noise)
        base_noise_set.add(base_noise)
        base_noise_map[noise] = base_noise

    for noise, action in commands.items():
        base = base_noise_map[noise]
        if any(other_noise.startswith(f"{base} ") and other_noise != base for other_noise in base_noise_set):
            delayed_commands[noise] = action
        else:
            immediate_commands[noise] = action

    return immediate_commands, delayed_commands

def parse_modifiers(sound: str):
    noise, rest = sound.split(':', 1) if ':' in sound else (sound, None)
    modifiers, locations = None, None
    if rest:
        modifiers, locations = rest.split('@', 1) if '@' in rest else (rest, None)
    return noise, modifiers, locations

class ParrotConfig():
    def __init__(self):
        self.parrot_config_ref = None
        self.immediate_commands = {}
        self.delayed_commands = {}
        self.combo_chain = ""
        self.combo_job = None
        self.pending_combo = None

    def setup(self, parrot_config):
        if self.combo_job:
            cron.cancel(self.combo_job)
            self.combo_job = None
        self.combo_chain = ""
        self.pending_combo = None
        self.parrot_config_ref = parrot_config
        self.immediate_commands, self.delayed_commands = categorize_commands(parrot_config.get("commands", {}))

    def _delayed_combo_execute(self):
        if self.combo_job:
            cron.cancel(self.combo_job)
            self.combo_job = None
        self.delayed_commands[self.pending_combo][1]()
        self.combo_chain = ""
        self.pending_combo = None

    def execute(self, sound):
        (noise, modifiers, locations) = parse_modifiers(sound)
        if self.combo_job:
            cron.cancel(self.combo_job)
            self.combo_job = None

        self.combo_chain = self.combo_chain + f" {noise}" if self.combo_chain else noise

        if self.combo_chain in self.delayed_commands:
            self.pending_combo = self.combo_chain
            self.combo_job = cron.after("300ms", self._delayed_combo_execute)
        elif self.combo_chain in self.immediate_commands:
            self.immediate_commands[self.combo_chain][1]()
            self.combo_chain = ""
            self.pending_combo = None
        elif noise in self.immediate_commands:
            if self.pending_combo:
                self._delayed_combo_execute()
                actions.sleep("20ms")
            self.immediate_commands[noise][1]()

# todo: try using the user's direct reference instead
parrot_config_saved = ParrotConfig()

parrot_throttle_busy = {}

def parrot_throttle_disable(id):
    global parrot_throttle_busy
    parrot_throttle_busy[id] = False

@mod.action_class
class Actions:
    def use_parrot_config(sound: str):
        """Enable or disable the parrot mode"""
        config = actions.user.parrot_config()
        if parrot_config_saved.parrot_config_ref != config:
            parrot_config_saved.setup(config)

        parrot_config_saved.execute(sound)

    def parrot_config():
        """Return the parrot configuration for the current context"""
        return {}

    def parrot_config_get_commands_text():
        """Get text of commands formatted in a list"""
        config = actions.user.parrot_config()
        commands = config.get("commands", {})
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

    def parrot_throttle(time_ms: int, id: str, command: callable):
        """Throttle the command once every time_ms"""
        global parrot_throttle_busy
        if parrot_throttle_busy.get(id):
            return
        parrot_throttle_busy[id] = True
        command()
        cron.after(f"{time_ms}ms", lambda: parrot_throttle_disable(id))
