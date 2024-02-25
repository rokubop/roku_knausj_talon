from abc import abstractmethod, ABC
from typing import Literal, TypedDict

class Profile(TypedDict):
    name: str
    acceleration_curve: callable
    deceleration_curve: callable
    base_speed: int
    max_speed: int

class EventBusBase(ABC):
    @abstractmethod
    def register(self, event_name: str, callback: callable) -> None:
        """Register a callback for an event."""
        pass

    @abstractmethod
    def unregister(self, event_name: str, callback: callable) -> None:
        """Unregister a callback for an event."""
        pass

    @abstractmethod
    def notify(self, event_name: str) -> None:
        """Notify all registered callbacks of an event."""
        pass

class ButtonsBase(ABC):
    @abstractmethod
    def __init__(self, event_bus: EventBusBase, profile: Profile):
        """Initialize with an event bus and a profile."""
        pass

    @abstractmethod
    def update_profile(self, new_profile: Profile) -> None:
        """Update the controller's profile."""
        pass

    @abstractmethod
    def click(self, button: int = 0) -> None:
        """Trigger a click action."""
        pass

    @abstractmethod
    def drag(self, button: int = 0) -> None:
        """Start a drag action."""
        pass

    @abstractmethod
    def drag_stop(self) -> None:
        """Stop any ongoing drag action."""
        pass

class ScrollingBase(ABC):
    @abstractmethod
    def __init__(self, event_bus: EventBusBase, profile: Profile):
        """Initialize with an event bus and a profile."""
        pass

    @abstractmethod
    def update_profile(self, new_profile: Profile) -> None:
        """Update the controller's profile."""
        pass

    @abstractmethod
    def scroll_start(self, direction: str) -> None:
        """Start scrolling in a specified direction."""
        pass

    @abstractmethod
    def scroll_stop_soft(self) -> None:
        """Softly stop scrolling."""
        pass

    @abstractmethod
    def scroll_stop_hard(self) -> None:
        """Immediately stop scrolling."""
        pass

    @abstractmethod
    def is_scrolling(self) -> bool:
        """Check if currently scrolling."""
        pass

class MovementBase(ABC):
    @abstractmethod
    def __init__(self, event_bus: EventBusBase, profile: Profile):
        """Initialize with an event bus and a profile."""
        pass

    @abstractmethod
    def update_profile(self, new_profile: Profile) -> None:
        """Update the movement profile to a new one."""
        pass

    @abstractmethod
    def move_start_new(self, direction: Literal["up", "down", "left", "right"]) -> None:
        """Start moving in a new direction until stopped."""
        pass

    @abstractmethod
    def move_start(self, direction: Literal["up", "down", "left", "right"]) -> None:
        """Start moving in a new direction until stopped."""
        pass

    @abstractmethod
    def move_stop_soft(self) -> None:
        """Softly stop the movement."""
        pass

    @abstractmethod
    def move_stop_hard(self) -> None:
        """Immediately stop the movement."""
        pass

    @abstractmethod
    def stop_hard(self) -> None:
        """Immediately stop the movement."""
        pass

    @abstractmethod
    def stop_transition(self) -> None:
        """Immediately stop the movement."""
        pass

    @abstractmethod
    def stop_soft(self) -> None:
        """Immediately stop the movement."""
        pass

    @abstractmethod
    def is_moving(self) -> bool:
        """Check if there is an ongoing movement."""
        pass

    @abstractmethod
    def move_to_pos_relative(self) -> bool:
        """Check if there is an ongoing movement."""
        pass

    @abstractmethod
    def move_to_pos_relative_linear(self) -> bool:
        """Check if there is an ongoing movement."""
        pass