from talon import Module, Context, actions, settings, ctrl

mod = Module()
ctx = Context()

ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_default
"""

class EventMouse:
    def __init__(self):
        self.event_names = [
            "mouse_down",
            "mouse_up",
            "click",
            "scroll_start",
            "scroll_stop",
            "drag_start",
            "drag_stop"
        ]
        self.events: dict[str, list[callable]] = {}
        self.held_buttons = []

    def click(self, button: int = 0):
        if self.held_buttons:
            self.drag_stop()
        else:
            self._on("mouse_down")
            ctrl.mouse_click(button=button, hold=16000)
            self._on("mouse_up")
            self._on("click")

    def drag(self, button: int = 0):
        if button not in self.held_buttons:
            self.held_buttons.append(button)
            self._on("mouse_down")
            self._on("drag_start")
            ctrl.mouse_click(button=button, down=True)

    def drag_stop(self):
        if self.held_buttons:
            for button in self.held_buttons:
                ctrl.mouse_click(button=button, up=True)
            self.held_buttons.clear()
            self._on("mouse_up")
            self._on("drag_stop")

    def register(self, event: str, callback: callable):
        """
        Register events such as mouse_down, mouse_up, click,
        drag_start, drag_stop, scroll_start, scroll_stop
        """
        if event not in self.event_names:
            error_message = (
                f"Cannot register event {event} because it is not a valid event."
                f"Valid events are {', '.join(self.event_names)}"
            )
            raise ValueError(error_message)

        if event not in self.events:
            self.events[event] = []

        self.events[event].append(callback)

    def unregister(self, event: str, callback: callable):
        if event in self.events:
            self.events[event] = list(filter(lambda c: c != callback, self.events[event]))

    def _on(self, event: str):
        if event in self.events:
            for callback in self.events[event]:
                callback()

event_mouse = EventMouse()
def on_mouse_down():
    print("Received the mouse down event")

event_mouse.register("mouse_down", on_mouse_down)

@ctx.action_class("user")
class Actions:
    def parrot_v5_on_mode_enable():
        print("On parrot default enable")
        actions.user.add_red_cursor()

    def parrot_v5_on_mode_disable():
        print("On parrot default disable")
        actions.user.clear_screen_regions()

@mod.action_class
class Actions:
    def parrot_v5_click_primary():
        """Click the primary mouse button"""
        event_mouse.click(0)

    def parrot_v5_click_alternate():
        """Click the alternate mouse button"""
        event_mouse.click(1)

    def parrot_v5_drag_primary():
        """Click the alternate mouse button"""
        event_mouse.drag(0)
