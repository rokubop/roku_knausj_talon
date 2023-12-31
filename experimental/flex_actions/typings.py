from typing import Optional, Callable, TypedDict

class Profile(TypedDict):
    name: str
    commands: list["Command"]
    auto_activate: Optional[bool]
    on_start: Optional[Callable]
    on_stop: Optional[Callable]

class Command(TypedDict):
    name: str
    action: Callable
    group_name: Optional[str]

class CommandContinuous(TypedDict):
    name: str
    action_start: Callable
    action_stop: Callable
    debounce_start: Optional[str | int]
    debounce_stop: Optional[str | int]
    group_name: Optional[str]

class Tag(TypedDict):
    name: str
    on_start: Callable
    on_stop: Callable
    commands: dict