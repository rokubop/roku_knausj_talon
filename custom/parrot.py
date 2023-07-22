
from talon import Module, actions, cron
from datetime import datetime

mod = Module()

two_way_opposites = [
    ("north", "south"),
    ("up", "down"),
    ("left", "right"),
    ("push", "tug"),
    ("drain", "step"),
    ("undo", "redo"),
    ("last", "next"),
    ("forward", "back"),
    ("out", "in"),
]

opposites = {}

for key, value in two_way_opposites:
    opposites[key] = value
    opposites[value] = key

last_tut = ""
last_palete = ""

class StateReverse:
    def __init__(self):
        self.is_reverse_active = False
        self.timer_handle = None

    def activate_reverse(self):
        self.is_reverse_active = True
        if self.timer_handle:
            cron.cancel(self.timer_handle)
        self.timer_handle = cron.after("2s", self.deactivate_reverse)

    def deactivate_reverse(self):
        self.is_reverse_active = False
        self.timer_handle = None

    def is_active(self):
        return self.is_reverse_active

stateReverse = StateReverse()

def log_parrot(text: str):
    """Log parrot for stream with Serenade"""
    with open('parrot.log', 'a') as file:
        file.write(f'{datetime.now()}{text}\n')

@mod.action_class
class Actions:
    def on_palate():
        """Repeat or wake up."""
        global last_palete, last_tut

        # log_parrot('palate')

        if (actions.speech.enabled()):
            if (stateReverse.is_active() and last_tut):
                last_command = actions.user.history_get(0)
                for word in opposites:
                    if word in last_command:
                        if last_palete and last_palete in last_command:
                            actions.mimic(last_command)
                            last_tut = ""
                        else:
                            oppositePhrase = last_command.replace(word, opposites[word])
                            last_palete = oppositePhrase
                            actions.mimic(oppositePhrase)
                            last_tut = ""
                        return
                last_palete = ""
            else:
                actions.core.repeat_command()

            stateReverse.activate_reverse()
        # else:
        #     actions.speech.enable()



    def on_tut():
        """Reverse the last command"""
        global last_tut, last_palete

        # log_parrot('tut')
        if (actions.speech.enabled() and stateReverse.is_active()):
            last_command = actions.user.history_get(0)
            stateReverse.activate_reverse()
            for word in opposites:
                if word in last_command:
                    if last_tut and last_tut in last_command:
                        actions.mimic(last_command)
                        last_palete = ""
                    else:
                        oppositePhrase = last_command.replace(word, opposites[word])
                        last_tut = oppositePhrase
                        actions.mimic(oppositePhrase)
                        last_palete = ""
                    return
            last_tut = ""

    def on_pop():
        """Do pop"""
        # log_parrot('pop')
        if actions.user.mouse_is_dragging():
            print("case one")
            actions.user.mouse_drag_end()
        else:
            print("case two")
            actions.user.click()
