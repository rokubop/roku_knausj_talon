from dataclasses import dataclass

class Config:
    def __init__(self, name, activation_type, on_start, on_stop, commands):
        self.name = name
        self.commands = commands
        self.activation_type = activation_type
        self.on_start = on_start
        self.on_stop = on_stop
        self.active_tags = set()
        self.active_commands = set()
        self.context = None
        self.state = {}

@dataclass
class Command:
    name: str
    action: callable = None
    action_start: callable = None
    action_stop: callable = None
    debounce_start: str | int = None
    debounce_stop: str | int = None

@dataclass
class Tag:
    name: str
    on_start: callable
    on_stop: callable
    commands: dict