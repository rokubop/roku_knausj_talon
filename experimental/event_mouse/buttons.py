from talon import ctrl
from .typings import ButtonsBase, Profile

class ButtonsDefault(ButtonsBase):
    def __init__(self, event_bus, profile):
        self.held_buttons: list[int] = []
        self.event_bus = event_bus
        self.profile: Profile = profile

    def update_profile(self, new_profile):
        self.profile = new_profile

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