from talon import Context, actions
from ..typings import Profile, Command, CommandContinuous

ctx = Context()

def on_start():
    print("on start")

def on_stop():
    print("on stop")

scroll_down = CommandContinuous(
    name="scroll down",
    group_name="scroll",
    action_start=lambda: print("executing: scroll down"),
    action_stop=lambda: print("executing: scroll down stop")
)

scroll_up = CommandContinuous(
    name="scroll up",
    group_name="scroll",
    action_start=lambda: print("executing: scroll up"),
    action_stop=lambda: print("executing: scroll up stop")
)

click = Command(
    name="click",
    action=lambda: print("executing: click")
)

default_mode = Command(
    name="default mode",
    action=lambda: (
    print("changing to default mode"),
    actions.user.flex_profile_activate("default")
)
)

profile_position = Profile(
    name="position",
    activation_type="auto",
    on_start=on_start,
    on_stop=on_stop,
    commands={
        "nn": click,
        "hiss": [scroll_down],
        "shush": [scroll_up],
        "eh": default_mode
    }
)