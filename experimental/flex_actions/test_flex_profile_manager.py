from .typings import Profile
from unittest.mock import Mock
from .flex_profile_manager import FlexProfileManager
from talon import Module
mod = Module()

class MockEventHistory:
    def __init__(self):
        self.events = []

    def append_event(self, event_name: str):
        self.events.append(event_name)

    def was_called(self, event_name: str):
        return event_name in self.events

    def was_not_called(self, event_name: str):
        return event_name not in self.events

    def a_was_called_before_b(self, event_name_1: str, event_name_2: str):
        return self.events.index(event_name_1) < self.events.index(event_name_2)

    def reset(self):
        self.events = []

    def debug_events(self):
        print("debug events:")
        print(self.events)

mock_event_history = MockEventHistory()

EVENT_ON_START_PROFILE2 = "on_start test_profile2"
EVENT_ON_STOP_PROFILE2 = "on_stop test_profile2"
EVENT_ON_START_PROFILE3 = "on_start test_profile3"
EVENT_ON_STOP_PROFILE3 = "on_stop test_profile3"

test_profile = Profile(
    name="test_profile",
    auto_activate=True,
    commands={
        "x": {
            "name": "x1",
            "action": lambda: "x1"
        }
    }
)

test_profile2: Profile = {
    "name": "test_profile2",
    "on_start": lambda : (
        mock_event_history.append_event(EVENT_ON_START_PROFILE2)
    ),
    "on_stop": lambda : mock_event_history.append_event(EVENT_ON_STOP_PROFILE2),
    "commands": {
        "x": {
            "name": "x2",
            "action": lambda: "x2"
        }
    }
}

test_profile3 = Profile(
    name="test_profile3",
    auto_activate=False,
    on_start=lambda : mock_event_history.append_event(EVENT_ON_START_PROFILE3),
    on_stop=lambda : mock_event_history.append_event(EVENT_ON_STOP_PROFILE3),
    commands={
        "x": {
            "name": "x3",
            "action": lambda: "x3"
        },
        "y":{
            "name": "y3",
            "action": lambda: "y3"
        }
    }
)



test_title = ""

def set_mock_ctx_profile(manager: FlexProfileManager, profile: Profile):
    manager._ctx_profile = lambda: profile

i = 0
success_count = 0
failure_count = 0

def init():
    global i, success_count, failure_count
    i = 0
    success_count = 0
    failure_count = 0


def assert_equal(value1, value2):
    global i, success_count, failure_count
    i += 1
    result = None

    if value1 == value2:
        success_count += 1
        result = "Success"
    else:
        failure_count += 1
        result = "Error"

    if result == "Error":
        print(f"""*

Test #{i}: {test_title}.
-   {result}
-   Actual: {value1}, Expected: {value2}
""")

def run_test_suite():
    global test_title, i
    init()

    manager = FlexProfileManager("Test")

    test_title = "When I call an action it should execute"
    mock_event_history.reset()
    set_mock_ctx_profile(manager, test_profile)
    assert_equal(manager.execute_flex_action("x"), "x1")
    assert_equal(manager.profile_name_stack, ["test_profile"])
    assert_equal(manager.profiles["test_profile"].get('name'), "test_profile")

    test_title = "A context change should change profiles if auto_activate is true"
    mock_event_history.reset()
    set_mock_ctx_profile(manager, test_profile2)
    assert_equal(manager.execute_flex_action("x"), "x2")
    mock_event_history.debug_events()
    assert_equal(mock_event_history.was_called(EVENT_ON_START_PROFILE2), True)
    assert_equal(manager.profile_name_stack, ["test_profile", "test_profile2"])
    assert_equal(manager.profiles["test_profile"].get('name'), "test_profile")
    assert_equal(manager.profiles["test_profile2"].get('name'), "test_profile2")

    test_title = "A context change should not change profiles if auto_activate is false"
    mock_event_history.reset()
    set_mock_ctx_profile(manager, test_profile3)
    # Is still using the previous profile
    assert_equal(manager.execute_flex_action("x"), "x2")
    assert_equal(mock_event_history.was_called(EVENT_ON_START_PROFILE2), False)
    assert_equal(mock_event_history.was_called(EVENT_ON_STOP_PROFILE2), False)
    assert_equal(mock_event_history.was_called(EVENT_ON_START_PROFILE3), False)
    assert_equal(manager.profile_name_stack, ["test_profile", "test_profile2"])
    assert_equal(manager.profiles["test_profile3"].get('name'), "test_profile3")

    test_title = "We can manually set the profile we want to use"
    mock_event_history.reset()
    manager.use_profile("test_profile3")
    assert_equal(mock_event_history.was_called(EVENT_ON_STOP_PROFILE2), True)
    assert_equal(mock_event_history.was_called(EVENT_ON_START_PROFILE3), True)
    assert_equal(mock_event_history.a_was_called_before_b(EVENT_ON_STOP_PROFILE2, EVENT_ON_START_PROFILE3), True)
    assert_equal(manager.profile_name_stack, ["test_profile", "test_profile2", "test_profile3"])
    assert_equal(manager.execute_flex_action("x"), "x3")

    test_title = "We can use a previous profile manually"
    mock_event_history.reset()
    manager.use_profile("test_profile2")
    assert_equal(mock_event_history.was_called(EVENT_ON_STOP_PROFILE3), True)
    assert_equal(mock_event_history.was_called(EVENT_ON_START_PROFILE2), True)
    assert_equal(manager.profile_name_stack, ["test_profile", "test_profile3", "test_profile2"])
    assert_equal(manager.execute_flex_action("x"), "x2")

    test_title = "We can use a previous profile by switching context"
    mock_event_history.reset()
    set_mock_ctx_profile(manager, test_profile)
    assert_equal(manager.execute_flex_action("x"), "x1")
    assert_equal(mock_event_history.was_called(EVENT_ON_STOP_PROFILE2), True)
    assert_equal(manager.profile_name_stack, ["test_profile3", "test_profile2", "test_profile"])
    assert_equal(manager.profiles["test_profile"].get('name'), "test_profile")




@mod.action_class
class Actions:
    def flex_run_tests():
        """Run tests for flex actions"""
        global success_count, failure_count
        print("""-




********************

Start flex action tests

********************""")
        run_test_suite()
        print(f"""-

********************

Tests complete

Success: {success_count}
Failure: {failure_count}

********************




-
""")