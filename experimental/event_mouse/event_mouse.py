from talon import Module
from .typings import ButtonsBase, EventBusBase, ScrollingBase, MovementBase, Profile
from .buttons import ButtonsDefault
from .scrolling import ScrollingDefault
from .movement import MovementDefault
from .event_bus import EventBus
from .user.profiles import profile_default

class EventMouse:
    def __init__(self, ButtonsClass, ScrollingClass, MovementClass, profile_default):
        self.event_bus: EventBusBase = EventBus()
        self.profile: Profile = profile_default
        self.buttons: ButtonsBase = ButtonsClass(self.event_bus, self.profile)
        self.scrolling: ScrollingBase = ScrollingClass(self.event_bus, self.profile)
        self.movement: MovementBase = MovementClass(self.event_bus, self.profile)

        self.click = self.buttons.click
        self.drag = self.buttons.drag
        self.drag_stop = self.buttons.drag_stop
        self.scroll_start = self.scrolling.scroll_start
        self.scroll_stop_soft = self.scrolling.scroll_stop_soft
        self.scroll_stop_hard = self.scrolling.scroll_stop_hard
        self.move_start = self.movement.move_start
        self.move_start_new = self.movement.move_start_new
        self.move_stop_soft = self.movement.move_stop_soft
        self.move_stop_hard = self.movement.move_stop_hard
        self.is_scrolling = self.scrolling.is_scrolling
        self.is_moving = self.movement.is_moving

    def update_profile(self, new_profile: Profile):
        self.profile = new_profile
        self.movement.update_profile(new_profile)
        self.scrolling.update_profile(new_profile)
        self.buttons.update_profile(new_profile)

event_mouse = EventMouse(ButtonsDefault, ScrollingDefault, MovementDefault, profile_default)