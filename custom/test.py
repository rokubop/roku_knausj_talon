import inspect
from dataclasses import dataclass
from typing import List, Optional
from talon import Module, Context, actions, ui, cron, ctrl
# from talon_plugins import eye_zoom_mouse, eye_mouse
# from talon.track import tobii

mod = Module()
ctx = Context()

# ctx.matches = """
# app: /steam/
# """

# @mod.scope
# def scope():
#     return { "flex_mode": True }
# cron.interval("5s", scope.update)

# @mod.action_class
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

# @ctx.action_class("user")
# class UserActions:
#     def test_one():
#         """test"""

#         actions.insert('helloa')
