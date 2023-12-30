from typing import Optional, Callable
from dataclasses import dataclass

class Profile:
    def __init__(self,
            name: str,
            commands,
            auto_activate: Optional[bool] = True,
            on_start: Optional[Callable] = None,
            on_stop: Optional[Callable] = None
        ):
        self.name = name
        self.commands = commands
        self.auto_activate = auto_activate
        self.on_start = on_start
        self.on_stop = on_stop
        self.active_tags = set()
        self.active_commands = set()
        self.context = None
        self.state = {}

@dataclass
class Command:
    name: str
    action: Callable = None
    group_name: Optional[str] = None

@dataclass
class CommandContinuous:
    name: str
    action_start: Callable
    action_stop: Callable
    debounce_start: Optional[str | int] = None
    debounce_stop: Optional[str | int] = None
    group_name: Optional[str] = None

@dataclass
class Tag:
    name: str
    on_start: Callable
    on_stop: Callable
    commands: dict