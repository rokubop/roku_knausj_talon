from talon import Module, actions, ctrl, cron
import re
from talon_init import TALON_HOME

mod = Module()

cron_repeat_job = None

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

    def get_last_command_with_exception(exception: str):
        """Get the last command except for the one specified"""
        last_command = actions.user.history_get(0)
        second_last_command = actions.user.history_get(1)

        if not re.search(exception, last_command):
            return last_command
        elif not re.search(exception, second_last_command):
            return second_last_command
        return None

    def repeat_last_command():
        """Continue repeating the last command"""
        if (actions.speech.enabled()):
            last_command = actions.user.get_last_command_with_exception("continue")
            if last_command:
                actions.mimic(last_command)

    def cancel_repeat_repeatedly():
        """Cancel repeating the last command"""
        global cron_repeat_job
        if (actions.speech.enabled() and cron_repeat_job):
            cron.cancel(cron_repeat_job)
            cron_repeat_job = None

    def start_repeat_repeatedly(timeout: int = 1):
        """Continue repeating the last command"""
        global cron_repeat_job
        if (actions.speech.enabled() and not cron_repeat_job):
            time = f'{timeout}000ms'
            cron_repeat_job = cron.interval(time, actions.user.repeat_last_command)
            actions.user.repeat_last_command()