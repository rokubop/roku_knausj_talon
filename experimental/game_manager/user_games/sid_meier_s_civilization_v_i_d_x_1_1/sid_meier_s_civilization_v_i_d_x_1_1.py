from talon import Module, Context, actions, ctrl, cron
import platform
os = platform.system().lower()

if os.startswith("windows"):
    import win32api, win32con

def mouse_move_windows(dx: int, dy: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

mod = Module()
ctx = Context()

mod.apps.sid_meier_s_civilization_v_i_d_x_1_1 = r"""
os: windows
and app.exe: /CivilizationVI.exe/i
"""

ctx.matches = r"""
os: windows
app: sid_meier_s_civilization_v_i_d_x_1_1
"""

mouse_movement_flag = False

@mod.action_class
class Actions:
    def civilization_vi_mouse_movement_toggle():
        """Start or stop eye tracking - useful for hovering"""
        global mouse_movement_flag

        if mouse_movement_flag:
            actions.tracking.control_toggle(False)
            actions.tracking.control_gaze_toggle(False)
            actions.tracking.control_head_toggle(False)
            mouse_move_windows(2, 0)
        else:
            actions.tracking.control_toggle(True)
            actions.tracking.control_gaze_toggle(True)
            actions.tracking.control_head_toggle(True)

        mouse_movement_flag = not mouse_movement_flag

@ctx.action_class('user')
class Actions:
    def on_pop():
        actions.tracking.control_toggle(False)
        mouse_move_windows(2, 0)
        ctrl.mouse_click(button=0, hold=16000)
        actions.tracking.control_toggle(True)
        # if you want your other on_pop logic to fire too
        # actions.next()
