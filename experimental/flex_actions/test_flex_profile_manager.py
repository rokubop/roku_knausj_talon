from .typings import Profile
from .flex_profile_manager import FlexProfileManager
from talon import Module
mod = Module()

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

test_profile2 = {
    "name": "test_profile2",
    "commands": {
        "x": {
            "name": "x2",
            "action": lambda: "x2"
        }
    }
}

test_title = ""

def set_ctx_profile(manager: FlexProfileManager, profile: Profile):
    manager.ctx_profile = lambda: profile

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

    print(f"""*

Test #{i}: {test_title}.
-   {result}
-   Expected: {value1}, Actual: {value2}
""")

def run_test_suite():
    global test_title, i
    init()

    manager = FlexProfileManager("Test")

    test_title = "When I call an action it should execute"
    set_ctx_profile(manager, test_profile)
    assert_equal(manager.execute_flex_action("x"), "x1")
    assert_equal(manager.profile_name_stack, ["test_profile"])
    assert_equal(manager.profiles["test_profile"].name, "test_profile")

    test_title = "A context change should change profiles"
    set_ctx_profile(manager, test_profile2)
    assert_equal(manager.execute_flex_action("x"), "x2")
    assert_equal(manager.profile_name_stack, ["test_profile", "test_profile2"])
    assert_equal(manager.profiles["test_profile"].name, "test_profile")
    assert_equal(manager.profiles["test_profile2"].name, "test_profile2")



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