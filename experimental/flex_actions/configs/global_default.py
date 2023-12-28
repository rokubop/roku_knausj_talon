from talon import actions, Context
from ..typings import Config, Command, CommandContinuous

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

position_mode = Command(
    name="position mode",
    action=lambda: print("changing to position mode")
)

global_config = Config(
    name="global default",
    activation_type="auto",
    on_start=on_start,
    on_stop=on_stop,
    commands={
        "nn": click,
        "hiss": [scroll_down],
        "shush": [scroll_up],
        "eh": position_mode
    }
)

@ctx.action_class("user")
class GlobalActions:
    def flex_config():
        return global_config