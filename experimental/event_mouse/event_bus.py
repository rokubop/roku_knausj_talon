from talon import actions
from .typings import EventBusBase
from typing import defaultdict

class EventBus(EventBusBase):
    def __init__(self):
        self.events = defaultdict(list)

    def register(self, event_name, callback):
        self.events[event_name].append(callback)

    def unregister(self, event_name, callback):
        if event_name in self.events:
            self.events[event_name] = list(filter(lambda c: c != callback, self.events[event_name]))

    def notify(self, event_name):
        for callback in self.events[event_name]:
            callback()

        method = getattr(actions.user, f"on_event_mouse_{event_name}", None)
        if method:
            method()