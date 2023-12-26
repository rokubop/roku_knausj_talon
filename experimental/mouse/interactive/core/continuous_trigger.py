from talon import cron

class ContinuousTrigger:
    """
    Performs a single start and stop callback, provided a debounce_stop time
    (defaults to 150ms). Useful for continuous parrot sounds.

    Usage:
    ```
    def on_start():
        print("I trigger once per lifecycle, immediately")

    def on_stop():
        print("I'm called after 150ms of inactivity")

    hiss = ContinuousTrigger(on_start)
    hiss = ContinuousTrigger(on_start, on_stop)
    hiss = ContinuousTrigger(on_start, on_stop, "150ms")

    @ctx.action_class("user")
    class Actions:
        def on_hiss_start():
            hiss.start()

        def on_hiss_stop()
            hiss.stop()

    # If you want to force stop the debouncer, immediately:
    hiss.force_stop()
    ```
    """
    def __init__(self, start_action=None, stop_action=None, debounce_stop="150ms"):
        self.debounce_time = debounce_stop
        self.started = False
        self.start_action = start_action
        self.stop_action = stop_action
        self.stop_debouncer = None

    def _actual_stop(self):
        if self.started:
            self.started = False
            if self.stop_action:
                self.stop_action()
        if self.stop_debouncer:
            cron.cancel(self.stop_debouncer)
            self.stop_debouncer = None

    def start(self):
        if not self.started:
            self.started = True
            if self.start_action:
                self.start_action()
            if self.stop_debouncer:
                cron.cancel(self.stop_debouncer)
                self.stop_debouncer = None

    def stop(self):
        if self.started:
            if self.stop_debouncer:
                cron.cancel(self.stop_debouncer)
            self.stop_debouncer = cron.after(self.debounce_time, self._actual_stop)

    def force_stop(self):
        self._actual_stop()
