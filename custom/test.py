import inspect
from dataclasses import dataclass
from typing import List, Optional
from talon import Module, Context, actions, ui, cron, ctrl
# from talon_plugins import eye_zoom_mouse, eye_mouse
# from talon.track import tobii
import time

mod = Module()
mod.mode("test_mode", "test mode")
ctx = Context()
ctx_test_mode = Context()
ctx_test_mode.matches = """
mode: user.test_mode
"""


@mod.action_class
class Actions:
    def test_one():
        """test"""
        # actions.core.repeat_phrase()
        # print(dir(eye_mouse.tracker))
        # print(ui.active_window())

    # def test_two(power: float, f0: float, f1: float, f2: float):
    def test_two(ts: float, power: float, f0: float, f1: float, f2: float):
        """test"""
        if f0 > 145:
            print("high sound")
        else:
            print("low sound")
        print(f"f0:{f0} f1:{f1} f2:{f2}")
        # print(f"{ts} {power} {f0} {f1} {f2}")
        # actions.key('down')

    def test_context():
        """test context"""
        # actions.insert("module context")
        pass

    def test_mode_enable():
        """test mode enable"""
        actions.mode.enable("user.test_mode")

    def test_mode_disable():
        """test mode disable"""
        actions.mode.disable("user.test_mode")

job_1 = None
job_2 = None
queue = []

def stop_do_something(name: str):
    global job_2
    print(f"stop_do_something {name} time start", time.perf_counter())
    if job_2:
        cron.cancel(job_2)
        job_2 = None

def do_something(name: str):
    global job_2
    print(f"****** do_something time {name} start", time.perf_counter())
    count = 0

    # stop_do_something(name)
    if job_2:
        print(f"job_2 already in progress {name}", time.perf_counter())
        return

    def update():
        nonlocal count
        count += 1
        print(f'> tick > doing something {name} {time.perf_counter()}', count)
        if count > 10:
            stop_do_something(name)
            return

    print(f"job_2 created {name}", time.perf_counter())
    update()
    job_2 = cron.interval("16ms", update)
    print(f"job_2 actually created {name}", time.perf_counter())

def timing_action():
    global job_1
    if job_1:
        cron.cancel(job_1)
        job_1 = None
    print("first do_something time start", time.perf_counter())
    do_something('AAA')
    sleep_start =  time.perf_counter()
    actions.sleep("1s")
    sleep_end =  time.perf_counter()
    print('sleep total', sleep_end - sleep_start)
    print("second do_something time start", time.perf_counter())
    do_something('BBB')



@mod.action_class
class Actions:
    def test_timing():
        """Test timing"""
        global job_1
        # timing_action()
        job_1 = cron.after("100ms", timing_action)

    def zoom_custom():
        """Custom action"""
        if not actions.tracking.control_zoom_enabled():
            actions.tracking.control_zoom_toggle(True)
            actions.sleep("50ms")
        actions.tracking.zoom()


@ctx.action_class("user")
class UserActions:
    def test_context():
        actions.insert("ctx context")
        actions.next()

@ctx_test_mode.action_class("user")
class UserActions:
    def test_context():
        actions.insert("ctx test mode")
        actions.next()
