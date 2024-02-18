from talon import Module, actions, ctrl, settings, cron
from collections import defaultdict
import time

mod = Module()
mod.setting("event_mouse_scroll_speed", float, 1, "Setting for event mouse scroll speed")

class EventBus:
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


class Buttons:
    def __init__(self, event_bus):
        self.held_buttons = []
        self.event_bus = event_bus

    def click(self, button: int = 0):
        if self.held_buttons:
            self.drag_stop()
        else:
            self.event_bus.notify("button_down")
            ctrl.mouse_click(button=button, hold=16000)
            self.event_bus.notify("button_up")
            self.event_bus.notify("click")

    def drag(self, button: int = 0):
        if button not in self.held_buttons:
            self.held_buttons.append(button)
            self.event_bus.notify("button_down")
            self.event_bus.notify("drag_start")
            ctrl.mouse_click(button=button, down=True)

    def drag_stop(self):
        if self.held_buttons:
            for button in self.held_buttons:
                ctrl.mouse_click(button=button, up=True)
            self.held_buttons.clear()
            self.event_bus.notify("button_up")
            self.event_bus.notify("drag_stop")

class Scrolling:
    def __init__(self, event_bus):
        self.scroll_job = None
        self.scroll_dir = 1
        self.scroll_start_ts = None
        self.scroll_stop_soft_ts = None
        self.debounce_start_duration = 0.0
        self.debounce_stop_duration = 0.170
        self.event_bus = event_bus

    def scroll_start(self, direction: str):
        """Start scrolling until stop is called"""
        new_scroll_dir = -1 if direction == "up" else 1
        self.scroll_stop_soft_ts = None

        if self.scroll_job:
            if new_scroll_dir != self.scroll_dir:
                self.scroll_dir = new_scroll_dir
                self.scroll_start_ts = time.perf_counter()
            # scroll_job already exists
            return

        self.scroll_dir = new_scroll_dir
        self.scroll_start_ts = time.perf_counter()
        self.event_bus.notify("scroll_start")
        self.scroll_tick()
        self.scroll_job = cron.interval("16ms", self.scroll_tick)

    def scroll_tick(self):
        ts = time.perf_counter()
        if ts - self.scroll_start_ts < self.debounce_start_duration:
            return

        if self.scroll_stop_soft_ts and ts - self.scroll_stop_soft_ts > self.debounce_stop_duration:
            self.scroll_stop_hard()
            return

        acceleration_speed = 1 + min((ts - self.scroll_start_ts) / 0.5, 4)
        y = (
            settings.get("user.event_mouse_scroll_speed")
            * acceleration_speed
            * self.scroll_dir
        )
        actions.mouse_scroll(y, by_lines=True)

    def scroll_stop_soft(self):
        self.scroll_stop_soft_ts = time.perf_counter()

    def scroll_stop_hard(self):
        if self.scroll_job:
            cron.cancel(self.scroll_job)
            self.scroll_start_ts = None
            self.scroll_stop_soft_ts = None
            self.scroll_job = None
            self.event_bus.notify("scroll_stop")

    def is_scrolling(self):
        return self.scroll_job is not None

class Movement:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def move_start(self):
        pass

class EventMouse:
    def __init__(self, Buttons, Scrolling, Movement):
        self.event_bus = EventBus()
        self.buttons = Buttons(self.event_bus)
        self.scrolling = Scrolling(self.event_bus)
        self.movement = Movement(self.event_bus)

        # self.event_bus.register("button_down", self.on_button_down)
        # self.event_bus.register("scroll_start", self.on_scroll_start)

        self.click = self.buttons.click
        self.drag = self.buttons.drag
        self.drag_stop = self.buttons.drag_stop
        self.scroll_start = self.scrolling.scroll_start
        self.scroll_stop_soft = self.scrolling.scroll_stop_soft
        self.scroll_stop_hard = self.scrolling.scroll_stop_hard
        self.move_start = self.movement.move_start
        self.is_scrolling = self.scrolling.is_scrolling

    # def on_button_down(self):
    #     self.scrolling.scroll_stop_hard()
    #     actions.user.tracking_control_freeze()

    # def on_scroll_start(self):
    #     actions.user.tracking_control_freeze()

event_mouse = EventMouse(Buttons, Scrolling, Movement)

def no_op():
    pass

@mod.action_class
class Actions:
    def event_mouse_click(button: str = 0):
        """Event mouse click""";
        event_mouse.click(button)

    def event_mouse_drag(button: int = 0):
        """Event mouse drag"""
        event_mouse.drag(button)

    def event_mouse_drag_stop():
        """Event mouse drag stop"""
        event_mouse.drag_stop()

    def event_mouse_scroll_start(direction: str = "down"):
        """Event mouse scroll start"""
        event_mouse.scroll_start(direction)

    def event_mouse_scroll_stop_soft():
        """Event mouse scroll stop soft"""
        event_mouse.scroll_stop_soft()

    def event_mouse_scroll_stop_hard():
        """Event mouse scroll stop hard"""
        event_mouse.scroll_stop_hard()

    def event_mouse_is_scrolling():
        """Event mouse scroll stop hard"""
        event_mouse.is_scrolling()

    def on_event_mouse_click():
        """On mouse click"""
        no_op()

    def on_event_mouse_button_down():
        """On mouse down"""
        no_op()

    def on_event_mouse_button_up():
        """On mouse up"""
        no_op()

    def on_event_mouse_drag_start():
        """On drag start"""
        no_op()

    def on_event_mouse_drag_stop():
        """On drag stop"""
        no_op()

    def on_event_mouse_scroll_start():
        """On scroll start"""
        no_op()

    def on_event_mouse_scroll_stop():
        """On scroll stop"""
        no_op()
