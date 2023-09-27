from talon import Module, Context, actions, ctrl, settings, cron
from ....plugin.debouncer import Debouncer
import win32api, win32con

mod = Module()

track_job = None
interval = 2000

anchor_position = None
programmatic_offset_x = 0
programmatic_offset_y = 0
sensitivity_x = 10
sensitivity_y = 10
speed_x = 5
speed_y = 5

def tick():
    global anchor_position, programmatic_offset_x, programmatic_offset_y, sensitivity_x, sensitivity_y, speed_x, speed_y
    if anchor_position:
        current_position = ctrl.mouse_pos()

        # Adjust the effective position based on how much we've moved the mouse programmatically
        effective_position_x = current_position[0] - programmatic_offset_x
        effective_position_y = current_position[1] - programmatic_offset_y

        dx = effective_position_x - anchor_position[0]
        dy = effective_position_y - anchor_position[1]

        print(f"dx: {dx}, dy: {dy}")
        print(f"effective_position_x: {effective_position_x}, effective_position_y: {effective_position_y}")
        print(f"anchor_position[0]: {anchor_position[0]}, anchor_position[1]: {anchor_position[1]}")
        print(f"programmatic_offset_x: {programmatic_offset_x}, programmatic_offset_y: {programmatic_offset_y}")
        print(f"current_position[0]: {current_position[0]}, current_position[1]: {current_position[1]}")

        # Determine direction of movement for X
        if dx > sensitivity_x:
            direction_x = 1  # Moving right
        elif dx < -sensitivity_x:
            direction_x = -1  # Moving left
        else:
            direction_x = 0  # No significant movement in X

        # Determine direction of movement for Y
        if dy > sensitivity_y:
            direction_y = 1  # Moving down
        elif dy < -sensitivity_y:
            direction_y = -1  # Moving up
        else:
            direction_y = 0  # No significant movement in Y

        # Move the mouse based on directions and adjust our programmatic offsets
        ctrl.mouse_move(current_position[0] + direction_x * speed_x, current_position[1] + direction_y * speed_y)
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_head_toggle(True)
        # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, current_position[0] + direction_x * speed_x, current_position[1] + direction_y * speed_y)

        programmatic_offset_x += direction_x * speed_x
        programmatic_offset_y += direction_y * speed_y

def start_tracking():
    global track_job, interval
    if track_job:
        cron.cancel(track_job)
    track_job = cron.interval(f"{interval}ms", tick)

@mod.action_class
class LeanActions:
    def lean_left(amt: int = 1):
        """lean left"""
        print("lean left")
        x, y = ctrl.mouse_pos()
        ctrl.mouse_move(x - amt, y)

    def lean_right(amt: int = 1):
        """lean right"""
        print("lean right")
        x, y = ctrl.mouse_pos()
        ctrl.mouse_move(x + amt, y)

    def lean_forward(amt: int = 1):
        """lean forward"""
        print("lean forward")
        x, y = ctrl.mouse_pos()
        ctrl.mouse_move(x, y + amt)

    def lean_back(amt: int = 1):
        """lean back"""
        print("lean back")
        x, y = ctrl.mouse_pos()
        ctrl.mouse_move(x, y - amt)

    def lean_mode_start():
        """start lean mode"""
        # bring cursor to my active gaze
        # turn off gaze and turn on head
        # trigger the right lin command based on which way I go
        # depending how far away I am from the center it should be more
        global anchor_position
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(True)
        anchor_position = ctrl.mouse_pos()
        start_tracking()

    def lean_mode_stop():
        """stop lean mode"""
        global track_job, anchor_position, programmatic_offset_x, programmatic_offset_y
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(False)
        if track_job:
            cron.cancel(track_job)
            track_job = None
        anchor_position = None
        programmatic_offset_x = 0
        programmatic_offset_y = 0
