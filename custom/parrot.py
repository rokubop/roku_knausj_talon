
from talon import Module, actions, cron
from datetime import datetime

mod = Module()

opp = [
    ("north", "south"),
    ("up", "down"),
    ("left", "right"),
    ("push", "tug"),
    ("drain", "step"),
    ("undo", "redo"),
    ("last", "next"),
    ("forward", "back"),
]

opposites = {
    "north": "south",
    "south": "north",
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left",
    "push": "tug",
    "tug": "push",
    "undo": "redo",
    "redo": "undo",
    "drain": "step",
    "step": "drain",
    "last": "next",
    "next": "last",
    "forward": "back",
    "back": "forward",
}

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

def write_it(text: str):
    with open('parrot.log', 'a') as file:
        file.write(f'{datetime.now()}{text}\n')

@mod.action_class
class Actions:
    def on_palate():
        """Repeat or wake up."""
        global last_palete, last_tut

        write_it('palate')

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

        write_it('tut')
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
        write_it('pop')
