# from talon import Module, actions, noise, scope
import os

from talon import Module, actions, app, clip, cron, ctrl, imgui, noise, ui, Context
from talon_plugins import eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_camera_overlay, toggle_control

mod = Module()

@mod.action_class
class Actions:
    def palate_click():
        """Repeat or wake up."""
        # if (actions.speech.enabled()):
        actions.core.repeat_command()
        # else:
        #     actions.user.wake_all()

    def repeat(): 
        """Repeat the last command."""
        if (actions.speech.enabled()):
            actions.core.repeat_command()

    def click():
        """Click the mouse."""
        if (actions.speech.enabled()):
            ctrl.mouse_click(button=0, hold=16000)