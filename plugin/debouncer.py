from talon import cron
import time

class Debouncer:
    def __init__(self, debounce_duration, start_action, stop_action):
        self.debounce_duration = debounce_duration
        self.started = False
        self.start_action = start_action
        self.stop_action = stop_action
        self.timer_handle = None

    def _actual_stop(self):
        if self.started:
            self.started = False
            self.stop_action()
        if self.timer_handle:  # Clear timer handle after executing.
            self.timer_handle = None

    def start(self):
        if not self.started:
            self.started = True
            self.start_action()
            if self.timer_handle:
                cron.cancel(self.timer_handle)
                self.timer_handle = None

    def stop(self):
        if self.started:
            if self.timer_handle:
                cron.cancel(self.timer_handle)
            self.timer_handle = cron.after(f"{self.debounce_duration}ms", self._actual_stop)
