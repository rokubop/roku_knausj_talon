from talon import Module, actions, ctrl

mod = Module()

@mod.action_class
class Actions:
    def repeat():
        """Repeat the last command."""
        if (actions.speech.enabled()):
            actions.core.repeat_command()

    def click():
        """Click the mouse."""
        if (actions.speech.enabled()):
            ctrl.mouse_click(button=0, hold=16000)
