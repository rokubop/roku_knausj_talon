from talon import Module, Context, actions
import win32api, win32con

mod = Module()
ctx = Context()
mod.apps.viewfinder = r"""
os: windows
and app.exe: Viewfinder.exe
"""
ctx.matches = r"""
os: windows
app: viewfinder
"""
ctx.settings = {
    "key_hold": 64.0,
    "key_wait": 16.0,
}

rewind = False

@ctx.action_class('user')
class Actions:
    def pedal_left_down():
        actions.key("w:down")

    def pedal_left_up():
        actions.key("w:up")

    def pedal_center_down():
        actions.key("e")

    def parrot_guh():
        global rewind
        print( "******* guh from viewfinder" )
        if actions.user.parrot_mode_has_tag("user.parrot_side_b"):
            rewind = False
            actions.key("r")
            actions.sleep("50ms")
            actions.key("r")
        else:
            if rewind:
                actions.key("r:up")
            else:
                actions.key("r:down")
            rewind = not rewind
