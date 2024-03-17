from talon import Module, actions, cron

mod = Module()

combo_chain = ""
combo_job = None

def no_op():
    pass

def parrot_combo_stop():
    global combo_chain, combo_job
    if combo_job:
        cron.cancel(combo_job)
        combo_job = None
    actions.user.on_parrot_combo_stop({"combo": combo_chain})
    combo_chain = ""

def categorize_commands(commands):
    def is_prefix_of_other(cmd):
        return any(other_cmd.startswith(f"{cmd} ") and other_cmd != cmd for other_cmd in commands)

    immediate_commands = {}
    delayed_commands = {}

    for command, action in commands.items():
        if is_prefix_of_other(command):
            delayed_commands[command] = action
        else:
            immediate_commands[command] = action

    return immediate_commands, delayed_commands

class ParrotConfig():
    def __init__(self):
        self.mode = ""
        self.immediate_commands = {}
        self.delayed_commands = {}
        self.combo_chain = ""
        self.combo_job = None

    def setup(self, parrot_config):
        if self.combo_job:
            cron.cancel(self.combo_job)
            self.combo_job = None
        self.mode = parrot_config.get("mode", "")
        self.immediate_commands, self.delayed_commands = categorize_commands(parrot_config.get("commands", {}))

    def _delayed_combo_execute(self):
        if self.combo_job:
            cron.cancel(self.combo_job)
            self.combo_job = None
        self.delayed_commands[self.combo_chain][1]()
        self.combo_chain = ""

    def execute(self, sound):
        if self.combo_job:
            cron.cancel(self.combo_job)
            self.combo_job = None

        self.combo_chain = self.combo_chain + f" {sound}" if self.combo_chain else sound

        if self.combo_chain in self.delayed_commands:
            self.combo_job = cron.after("300ms", self._delayed_combo_execute)
        elif self.combo_chain in self.immediate_commands:
            self.immediate_commands[self.combo_chain][1]()
            self.combo_chain = ""
        elif sound in self.immediate_commands:
            self.immediate_commands[sound][1]()
            self.combo_chain = ""

parrot_config_saved = ParrotConfig()

@mod.action_class
class Actions:
    def use_parrot_config(sound: str):
        """Enable or disable the parrot mode"""
        config = actions.user.parrot_config()
        if parrot_config_saved.mode != config.get("mode", ""):
            parrot_config_saved.setup(config)

        parrot_config_saved.execute(sound)

    def parrot_config():
        """Return the parrot configuration for the current context"""
        return {}

    def parrot_combo(name: str):
        """Helper for combos. Define `ctx` callbacks `on_parrot_combo(ev: dict)` and/or `on_parrot_combo_stop(ev: dict)`"""
        global combo_chain, combo_job
        if combo_job:
            cron.cancel(combo_job)

        combo_chain = combo_chain + f" {name}" if combo_chain else name
        actions.user.on_parrot_combo({"combo": combo_chain})
        # parrot_combo_stop()
        combo_job = cron.after("300ms", parrot_combo_stop)

    def on_parrot_combo(ev: dict):
        """Called on each individual combo action"""
        no_op()

    def on_parrot_combo_stop(ev: dict):
        """Called when a complete combo is finished"""
        no_op()
