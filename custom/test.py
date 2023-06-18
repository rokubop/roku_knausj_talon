# from talon import Module, actions, noise, scope
import os

from talon import Module, actions, app, clip, cron, ctrl, imgui, noise, ui, Context
from talon_plugins import eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_camera_overlay, toggle_control

mod = Module()

def fibonacci(n: str):
    if n == 'world':
        print('yo')


@mod.action_class

class Actions:
    def test_one(whatever: str):
        """test"""
        if whatever == 'world':
            print('yo')