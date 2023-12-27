from dataclasses import dataclass

def mouse_hold():
    pass

def mouse_click():
    pass

def scroll_down():
    pass

def scroll_up():
    pass

def scroll_down_stop():
    pass

def scroll_up_stop():
    pass

# mock data
actions = {
    "user": {
        "mouse_hold": mouse_hold,
        "mouse_click": mouse_click,
        "scroll_down": scroll_down,
        "scroll_up": scroll_up,
        "scroll_down_stop": scroll_down_stop,
        "scroll_up_stop": scroll_up_stop,
    },
}


config = {
    "ah": mouse_hold,
    "hiss": scroll_down,
    "nn": mouse_click
}

config.register("ah", mouse_hold)
config.register_continuous("hiss", scroll_down, scroll_down_stop)
config.register("nn", mouse_click)
config.register_combo(["nn", "ah"], mouse_click)

config = {
    'ah': {
        "type": "discrete",
        "action": mouse_hold
    },
    "hiss": {
        "type": "continuous",
        "action": scroll_down
    },
}

config.cmd("ah", actions.user.mouse_hold)
config.cmd("hiss", actions.user.scroll_down, actions.user.scroll_down_stop),
config.cmd("hiss", actions.user.scroll_down, actions.user.scroll_down_stop),
config.cmd("shush", actions.user.scroll_up, actions.user.scroll_up_stop,),
config.cmd("nn nh", actions.user.mouse_click, timeout=0.5),
config.cmd("t cluck", actions.user.mode_switch),

def on_start():
    print("hello world start")

def on_stop():
    print("hello world stop")

config = {
    "on_start": on_start,
    "on_stop": on_stop,
    "commands": {
        "ah": actions.user.mouse_hold,
        "hiss": {
            "start": actions.user.scroll_down,
            "stop": actions.user.scroll_down_stop,
            "debounce_start": '300ms',
        },
        "hiss2": {
            "start": actions.user.scroll_down,
            "stop": actions.user.scroll_down_stop,
            "debounce_end": '150ms',
        },
        "nn nh": {
            "action": actions.user.mouse_click,
            "timeout": '0.5s',
        }
    }
}

class Config:
    def __init__(self, name, on_start, on_stop, commands):
        self.name = name
        self.commands = commands
        self.on_start = on_start
        self.on_stop = on_stop
        self.active_tags = set()
        self.active_commands = set()
        self.context = None
        self.state = {}





@dataclass
class Tag:
    name: str
    on_start: callable
    on_stop: callable
    commands: dict

@dataclass
class Command:
    name: str
    action: callable
    action_start: callable = None
    action_stop: callable = None
    debounce_start: str | int = None
    debounce_stop: str | int = None

command_scroll_down = Command(
    name="scroll down",
    action_start=actions.user.scroll_down,
    action_stop=actions.user.scroll_down_stop,
    debounce_start='300ms',
)

command_scroll_up = Command(
    name="scroll up",
    action_start=actions.user.scroll_up,
    action_stop=actions.user.scroll_up_stop,
    debounce_start='300ms',
)

command_shift_scroll_down = Command(
    name="shift scroll down",
    action_start=lambda: actions.user.scroll_down("shift"),
    action_stop=lambda: actions.user.scroll_down_stop("shift"),
    debounce_start='300ms',
)

command_shift_scroll_up = Command(
    name="shift scroll up",
    action_start=lambda: actions.user.scroll_up("shift"),
    action_stop=lambda: actions.user.scroll_up_stop("shift"),
    debounce_start='300ms',
)

command_drag_down = Command(
    name="drag down",
    action_start=actions.user.drag_down,
    action_stop=actions.user.drag_down_stop,
    debounce_end='150ms',
)

command_drag_up = Command(
    name="drag up",
    action_start=actions.user.drag_up,
    action_stop=actions.user.drag_up_stop,
    debounce_end='150ms',
)


scroller = Tag(
    name="scroller",
    on_start=on_start,
    on_stop=on_stop,
    commands={
        "hiss": command_scroll_down,
        "shush": command_scroll_up
    }
)

shift_scroller = Tag(
    name="shift_scroller",
    on_start=on_start,
    on_stop=on_stop,
    commands={
        "hiss": command_shift_scroll_down,
        "shush": command_shift_scroll_up
    }
)

dragger = Tag(
    name="dragger",
    on_start=on_start,
    on_stop=on_stop,
    commands={
        "hiss": command_drag_down,
        "shush": command_drag_up
    }
)

config = {
    "name": "default",
    "on_start": on_start,
    "on_stop": on_stop,
    "tags": [scroller, dragger],
    "commands": {
        "ah":{
            "name": "click",
            "action": actions.user.mouse_hold
        },
        "hiss": {
            "tags": [scroller, shift_scroller, dragger]
        },
        "shush": [command_scroll_up, command_shift_scroll_up, command_drag_up],
        "nn cluck": {
            "name": "mode_switch",
            "action": actions.user.mode_switch,
            "timeout": '0.5s',
        },
        "eh": {
            "name": "position mode",
            "action": actions.user.mode_switch,
        },
    }
}

@dataclass
class Command:
    name: str
    action: callable
    type: str = "discrete"
    stop_action: callable = None
