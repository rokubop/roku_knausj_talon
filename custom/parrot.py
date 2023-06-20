
from talon import Module, actions, speech_system
import threading

mod = Module()

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
}

last_tut = ""

@mod.action_class
class Actions:
    def on_tut():
        """Reverse the last command"""
        global last_tut

        if (actions.speech.enabled()):
            last_command = actions.user.history_get(0)
            print("last_command", last_command)
            second_last_command = actions.user.history_get(1)
            print("second_last_command", second_last_command)
            print("last_tut", last_tut)
            for word in opposites:
                if word in last_command:
                    if last_tut and last_tut in last_command:
                        print("run direct")
                        actions.mimic(last_command)
                    else:
                        print("run opposite")
                        oppositePhrase = last_command.replace(word, opposites[word])
                        last_tut = oppositePhrase
                        actions.mimic(oppositePhrase)
                        print(oppositePhrase)
                    return
            last_tut = ""
