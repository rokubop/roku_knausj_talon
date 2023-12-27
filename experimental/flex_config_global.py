from talon import actions, Context
from .typings import Config, Command

ctx = Context()

def on_start():
    print("on start")

def on_stop():
    print("on stop")

global_config = Config(
    name="default",
    activation_type="auto",
    on_start=on_start,
    on_stop=on_stop,
    commands={
        "nn": Command(
            name="click",
            action=lambda: print("executing: click")
        ),
        "hiss": Command(
            name="scroll down",
            action_start=lambda: print("executing: scroll down"),
            action_stop=lambda: print("executing: scroll down stop")
        ),
        "shush": Command(
            name="scroll up",
            action_start=lambda: print("executing: scroll up"),
            action_stop=lambda: print("executing: scroll up stop")
        )
    }
)

@ctx.action_class("user")
class GlobalActions:
    def flex_config():
        print("returning the global config")
        return global_config