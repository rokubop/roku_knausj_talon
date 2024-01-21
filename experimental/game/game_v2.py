from talon import Module, actions, ctrl, settings, cron
import platform
import math
os = platform.system().lower()

mod = Module()
mod.setting("game_v2_calibrate_x_360", type=int, default=2000, desc="Arbitrary number amount that should be equivalent to 360 degrees")
mod.setting("game_v2_calibrate_y_ground_to_center", type=int, default=500, desc="Arbitrary number amount that should be equivalent to 360 degrees")
mouse_job = None
last_calibrate_value = 0
last_calibrate_value_y = 0
move_dir = None
step_dir = None
step_job = None
held_keys = set()

def _mouse_move(dx, dy):
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse_move(x + dx, y + dy, dx=dx, dy=dy)

if os.startswith("windows"):
    import win32api, win32con
    def _mouse_move(dx, dy):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

def _mouse_move_snap(degrees_x, degrees_y):
    dx_360 = settings.get("user.game_v2_calibrate_x_360")
    dy_90 = settings.get("user.game_v2_calibrate_y_ground_to_center")
    dx_angle = dx_360 / 360 * degrees_x
    dy_angle = dy_90 / 90 * degrees_y
    _mouse_move(int(dx_angle), int(dy_angle))

total_x = 0

def _mouse_move_natural(degrees_x, degrees_y, duration_ms, calibrate_x_override = 0, calibrate_y_override = 0):
    global mouse_job, total_x

    _mouse_stop()

    # Initialize variables for the movement
    dx_360 = calibrate_x_override or settings.get("user.game_v2_calibrate_x_360")
    dy_90 = calibrate_y_override or settings.get("user.game_v2_calibrate_y_ground_to_center")
    dx_total = dx_360 / 360 * degrees_x
    dy_total = dy_90 / 90 * degrees_y
    step_count = 0

    update_interval_ms = 16
    steps = duration_ms // update_interval_ms

    # Define the update function
    def update_position():
        nonlocal step_count, dx_total, dy_total

        # Calculate progress
        progress = step_count / steps
        eased_progress = math.sin(progress * math.pi / 2)

        # Calculate deltas
        dx_step = dx_total * eased_progress - dx_total * math.sin((progress - 1 / steps) * math.pi / 2)
        dy_step = dy_total * eased_progress - dy_total * math.sin((progress - 1 / steps) * math.pi / 2)
        total_x = dx_step
        print(total_x)
        _mouse_move(int(dx_step), int(dy_step))

        step_count += 1
        if step_count >= steps:
            _mouse_stop()

    mouse_job = cron.interval("16ms", update_position)

def _mouse_stop():
    global mouse_job, total_x
    total_x = 0
    if mouse_job:
        cron.cancel(mouse_job)
        mouse_job = None

def _move_dir_stop():
    global move_dir
    if move_dir:
        actions.key(f"{move_dir}:up")
        move_dir = None


def _step_start(key: str, duration: str):
    global step_dir, step_job
    _step_stop()
    step_dir = key
    actions.key(f"{step_dir}:down")
    step_job = cron.after(duration, _step_stop)

def _step_stop():
    global step_job, step_dir
    if step_job:
        actions.key(f"{step_dir}:up")
        cron.cancel(step_job)
        step_job = None

@mod.action_class
class Actions:
    def game_v2_move_dir(key: str):
        """Move in direction"""
        global move_dir
        if move_dir:
            actions.key(f"{move_dir}:up")
        move_dir = key
        actions.key(f"{move_dir}:down")

    def game_v2_move_dir_step(key: str, steps: int):
        """Step in direction"""
        duration = f"{steps * 5}00ms"
        _step_start(key, duration)

    def game_v2_stop_layer_by_layer():
        """Perform stop based on a priority"""
        global move_dir
        if mouse_job:
            _mouse_stop()
        elif move_dir:
            _move_dir_stop()
        if step_job:
            _step_stop()

    def game_v2_stop_all():
        """Stop all"""
        global move_dir
        if mouse_job:
            _mouse_stop()
        if step_job:
            _step_stop()
        if move_dir:
            _move_dir_stop()

    def game_v2_calibrate_360(number: int):
        """Calibrate 360"""
        global last_calibrate_value
        last_calibrate_value = number
        _mouse_move_natural(360, 0, 2000, number)

    def game_v2_reset_center_y(value: int = 0):
        """Reset the center"""
        # _mouse_move_natural(0, 180, 50)
        # actions.sleep("50ms")
        # _mouse_move_natural(0, -90, 50)
        _mouse_move_natural(0, 180, 100)
        actions.sleep("100ms")
        _mouse_move_natural(0, -90, 100)

    def game_v2_calibrate_paste():
        """Paste the last attempted calibrate number"""
        actions.insert(last_calibrate_value)

    def game_v2_calibrate_y_ground_to_center(number: int):
        """Calibrate y ground to center"""
        global last_calibrate_value_y
        last_calibrate_value_y = number
        _mouse_move_natural(0, 180, 100, 0, number)
        actions.sleep("100ms")
        _mouse_move_natural(0, -90, 100, 0, number)

    def game_v2_calibrate_y_paste():
        """Paste the last attempted calibrate number"""
        actions.insert(last_calibrate_value_y)

    def game_v2_snap_180():
        """Snap 360"""
        _mouse_move_natural(360, 0, 500)
        # _mouse_move_snap(180, 0)

    def game_v2_snap_left(degrees: int):
        """Snap left to angle in degrees"""
        _mouse_move_snap(-degrees, 0)

    def game_v2_snap_right(degrees: int):
        """Snap right to angle in degrees"""
        _mouse_move_snap(degrees, 0)

    def game_v2_soft_left(degrees: int):
        """Turn left softly"""
        _mouse_move_natural(-degrees, 0, 2500)

    def game_v2_soft_right(degrees: int):
        """Turn right softly"""
        _mouse_move_natural(degrees, 0, 2500)

    def game_v2_turn_left(degrees: int):
        """Turn left"""
        _mouse_move_natural(-degrees, 0, 800)

    def game_v2_turn_right(degrees: int):
        """Turn right"""
        _mouse_move_natural(degrees, 0, 800)



    def game_v2_key_toggle_hold(key: str):
        """Toggle holding a key"""
        global held_keys
        if key in held_keys:
            actions.key(f"{key}:up")
            held_keys.remove(key)
        else:
            actions.key(f"{key}:down")
            held_keys.add(key)

    def game_v2_key_toggle_once(key: str):
        """Toggle holding a key once"""
        actions.key(key)
