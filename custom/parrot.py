
from talon import Module, actions, cron, Context
from datetime import datetime
import time

mod = Module()
ctx = Context()

two_way_opposites = [
    ("north", "south"),
    ("upper", "downer"),
    ("up", "down"),
    ("left", "right"),
    ("push", "tug"),
    ("drain", "step"),
    ("undo", "redo"),
    ("last", "next"),
    ("forward", "back"),
    ("out", "in"),
]

state = {}
cron_jobs = {}
callbacks = {}
shush_start: float = 0
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

@mod.action_class
class Actions:
    def on_palate():
        """Repeat or wake up."""
        global last_palete, last_tut

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


    def on_tut():
        """Reverse the last command"""
        global last_tut, last_palete

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
        if actions.user.mouse_is_dragging():
            print("pop as drag end")
            actions.user.mouse_drag_end()
        else:
            print("pop as click")
            actions.user.click()

    def noise_debounce(name: str, active: bool):
        """Start or stop continuous noise using debounce"""
        if name not in state:
            state[name] = active
            cron_jobs[name] = cron.after("80ms", lambda: callback(name))
        elif state[name] != active:
            cron.cancel(cron_jobs[name])
            state.pop(name)

    def noise_shush_start():
        """Noise shush started"""
        print("shush:start")

    def noise_shush_stop():
        """Noise shush stopped"""
        print("shush:stop")

    def noise_hiss_start():
        """Noise hiss started"""
        print("hiss:start")

    def noise_hiss_stop():
        """Noise hiss stopped"""
        print("hiss:stop")

def callback(name: str):
    active = state.pop(name)
    callbacks[name](active)

def on_shush(active: bool):
    if active:
        actions.user.noise_shush_start()
    else:
        actions.user.noise_shush_stop()


def on_hiss(active: bool):
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()

callbacks["shush"] = on_shush
callbacks["hiss"] = on_hiss

chrome_ctx = Context()
ctx.matches = """
app: Chrome
"""

@ctx.action_class("user")
class ChromeActions:
    def noise_shush_start():
        global shush_start
        shush_start = time.perf_counter()
        actions.user.mouse_scrolling("up")

    def noise_shush_stop():
        actions.user.abort_specific_phrases(
            ["hash", "ssh"], shush_start, time.perf_counter()
        )
        actions.user.mouse_scroll_stop()

    def noise_hiss_start():
        actions.user.mouse_scrolling("down")

    def noise_hiss_stop():
        actions.user.mouse_scroll_stop()