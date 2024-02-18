from talon import Module, Context, actions, settings

mod = Module()
mod.mode("parrot_v5", "base parrot mode v5 common to every parrot mode")
mod.mode("parrot_v5_default", "default parrot mode v5")
# mod.mode("parrot_v5_rpg_mouse", "rpg mouse parrot mode v5")
ctx = Context()

current_parrot_mode = None

def no_op():
    return

@mod.action_class
class Actions:
    def parrot_v5_mode_enable(parrot_mode: str = "user.parrot_v5_default"):
        """Enable parrot mode"""
        global current_parrot_mode
        if current_parrot_mode:
            actions.user.on_parrot_v5_mode_disable()
            actions.mode.disable(current_parrot_mode)
        current_parrot_mode = parrot_mode
        actions.mode.disable("command")
        actions.mode.enable("user.parrot_v5")
        actions.mode.enable(current_parrot_mode)
        actions.user.on_parrot_v5_mode_enable()

    def parrot_v5_mode_switch(parrot_mode: str):
        """Switch parrot mode"""
        global current_parrot_mode
        if current_parrot_mode:
            actions.user.on_parrot_v5_mode_disable_soft()
            actions.mode.disable(current_parrot_mode)
        current_parrot_mode = parrot_mode
        actions.mode.enable(current_parrot_mode)
        actions.user.on_parrot_v5_mode_enable()

    def parrot_v5_mode_disable():
        """Disable parrot mode"""
        global current_parrot_mode
        if current_parrot_mode:
            actions.user.on_parrot_v5_mode_disable()
            actions.mode.disable(current_parrot_mode)
            print(f"Disabled {current_parrot_mode}")
            current_parrot_mode = None
        actions.mode.disable("user.parrot_v5")
        actions.mode.enable("command")

    def on_parrot_v5_mode_enable():
        """Callback when parrot mode is enabled"""
        no_op()

    def on_parrot_v5_mode_disable():
        """Callback when parrot mode is disabled"""
        no_op()

    def on_parrot_v5_mode_disable_soft():
        """Callback when parrot mode is switched"""
        no_op()
