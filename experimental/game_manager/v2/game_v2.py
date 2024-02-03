"""
A generic set of game actions
game_v2_move_dir
game_v2_move_dir_step
game_v2_stop_layer_by_layer
game_v2_stop_all
game_v2_calibrate_360
game_v2_reset_center_y
game_v2_calibrate_paste
game_v2_calibrate_y_ground_to_center
game_v2_calibrate_y_paste
game_v2_snap_180
game_v2_snap_left
game_v2_snap_right
game_v2_soft_left
game_v2_soft_right
game_v2_soft_up
game_v2_soft_down
game_v2_turn_left
game_v2_turn_right
game_v2_turn_up
game_v2_turn_down
game_v2_key_toggle_hold
game_v2_key_toggle_once
"""
from talon import Module, Context, actions, ctrl, settings, cron
import platform
import math
os = platform.system().lower()

mod = Module()
mod.setting("game_v2_calibrate_x_360", type=int, default=2000, desc="Arbitrary number amount that should be equivalent to 360 degrees")
mod.setting("game_v2_calibrate_y_ground_to_center", type=int, default=500, desc="Arbitrary number amount that should be equivalent to 360 degrees")
mod.tag("game_v2", 'Game tag v2')
mod.tag("parrot_game_temp", 'Game tag v2 parrot')
ctx = Context()
mouse_job = None
last_calibrate_value = 0
last_calibrate_value_y = 0
move_dir = None
step_dir = None
step_job = None
held_keys = set()

def _mouse_move(dx: int, dy: int):
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse_move(x + dx, y + dy)

if os.startswith("windows"):
    import win32api, win32con
    def _mouse_move(dx: int, dy: int):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)

def _mouse_move_snap(degrees_x: int, degrees_y: int):
    dx_360 = settings.get("user.game_v2_calibrate_x_360")
    dy_90 = settings.get("user.game_v2_calibrate_y_ground_to_center")
    dx_angle = dx_360 / 360 * degrees_x
    dy_angle = dy_90 / 90 * degrees_y
    _mouse_move(int(dx_angle), int(dy_angle))

def _mouse_move_natural_hold_start(degrees: int = 0, speed: int = 100, acceleration: int = 5, min_speed: int = 100, max_speed: int = 200):
    global mouse_job

    _mouse_stop()

    dx_360 = settings.get("user.game_v2_calibrate_x_360")
    dy_90 = settings.get("user.game_v2_calibrate_y_ground_to_center")
    dx_normalized = dx_360 / 360
    dy_normalized = dy_90 / 90
    update_interval_ms = 16
    print("dx_normalized", dx_normalized)

    def update_position():
        _mouse_move(int(dx_normalized), 0)

    mouse_job = cron.interval("16ms", update_position)


def _mouse_move_natural_hold_release(duration_decay_ms: int = 300):
    global mouse_job

    _mouse_stop()

    dx_360 = settings.get("user.game_v2_calibrate_x_360")
    dy_90 = settings.get("user.game_v2_calibrate_y_ground_to_center")
    dx_normalized = dx_360 / 360
    dy_normalized = dy_90 / 90
    update_interval_ms = 16
    steps = max(1, duration_decay_ms // update_interval_ms)
    step_count = 0
    last_x, last_y = 0, 0
    accumulated_dx, accumulated_dy = 0.0, 0.0
    rad_90 = math.pi / 2

    def update_position():
        nonlocal step_count, last_x, last_y, accumulated_dx, accumulated_dy

        step_count += 1
        if step_count > steps:
            _mouse_stop()
            return

        linear_progress_0_to_1 = step_count / steps
        curved_progress_1_to_0 = math.sin(linear_progress_0_to_1 * rad_90 + rad_90)

        current_dx = dx_normalized * curved_progress_1_to_0

        _mouse_move(int(current_dx), 0)

    mouse_job = cron.interval("16ms", update_position)

# Examples:
# _mouse_move_natural(30, 0, 2000) # 30 degrees right over 2 seconds
# _mouse_move_natural(-30, 0, 500) # 30 degrees left over 500ms
def _mouse_move_natural(degrees_x: int, degrees_y: int, duration_ms: int, calibrate_x_override=0, calibrate_y_override=0):
    global mouse_job

    _mouse_stop()

    dx_360 = calibrate_x_override or settings.get("user.game_v2_calibrate_x_360")
    dy_90 = calibrate_y_override or settings.get("user.game_v2_calibrate_y_ground_to_center")
    dx_total = dx_360 / 360 * degrees_x
    dy_total = dy_90 / 90 * degrees_y
    update_interval_ms = 16
    steps = max(1, duration_ms // update_interval_ms)
    step_count = 0
    last_x, last_y = 0, 0
    accumulated_dx, accumulated_dy = 0.0, 0.0

    def update_position():
        nonlocal step_count, last_x, last_y, accumulated_dx, accumulated_dy

        step_count += 1
        if step_count > steps:
            _mouse_stop()
            # actions.user.game_v2_canvas_hide()
            return

        progress = step_count / steps
        eased_progress = math.sin(progress * math.pi / 2)

        current_x = dx_total * eased_progress
        current_y = dy_total * eased_progress

        dx_step = current_x - last_x
        dy_step = current_y - last_y

        accumulated_dx += dx_step - int(dx_step)
        accumulated_dy += dy_step - int(dy_step)

        if abs(accumulated_dx) >= 1:
            dx_step += int(accumulated_dx)
            accumulated_dx -= int(accumulated_dx)

        if abs(accumulated_dy) >= 1:
            dy_step += int(accumulated_dy)
            accumulated_dy -= int(accumulated_dy)
        print("dx_step", dx_step)
        print("dy_step", dy_step)


        _mouse_move(int(dx_step), int(dy_step))
        last_x, last_y = current_x, current_y
        if calibrate_x_override:
            actions.user.game_v2_canvas_refresh(f"Calibrate x: {int(current_x)}")


    mouse_job = cron.interval("16ms", update_position)

def _mouse_stop():
    global mouse_job
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

    def game_v2_move_dir_toggle(key: str):
        """Move in direction toggle"""
        global move_dir
        if move_dir:
            actions.key(f"{move_dir}:up")
            if move_dir == key:
                move_dir = None
                return
        move_dir = key
        actions.key(f"{move_dir}:down")

    def game_v2_move_dir_step(key: str, steps: int):
        """Step in direction"""
        duration = f"{steps * 2}00ms"
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
        actions.user.game_v2_canvas_calibrate_x()
        _mouse_move_natural(360, 0, 2000, number)

    def game_v2_reset_center_y(value: int = 0):
        """Reset the center"""
        time_ms = 100
        _mouse_move_natural(0, 180, time_ms)
        actions.sleep(f"{time_ms}ms")
        _mouse_move_natural(0, -90, time_ms)

    def game_v2_calibrate_paste():
        """Paste the last attempted calibrate number"""
        actions.insert(last_calibrate_value)

    def game_v2_calibrate_y_ground_to_center(number: int):
        """Calibrate y ground to center"""
        time_ms = 100
        _mouse_move_natural(0, 180, time_ms, 0, number)
        actions.sleep(f"{time_ms}ms")
        _mouse_move_natural(0, -90, time_ms, 0, number)

    def game_v2_calibrate_y_paste():
        """Paste the last attempted calibrate number"""
        actions.insert(last_calibrate_value_y)

    def game_v2_snap_180():
        """Snap 360"""
        _mouse_move_natural(180, 0, 100)

    def game_v2_snap_left(degrees: int):
        """Snap left to angle in degrees"""
        _mouse_move_natural(-degrees, 0, 100)
        # _mouse_move_snap(-degrees, 0)

    def game_v2_snap_right(degrees: int):
        """Snap right to angle in degrees"""
        _mouse_move_natural(degrees, 0, 100)
        # _mouse_move_snap(degrees, 0)

    def game_v2_soft_left(degrees: int):
        """Turn left softly"""
        _mouse_move_natural(-degrees, 0, 1500)

    def game_v2_soft_right(degrees: int):
        """Turn right softly"""
        _mouse_move_natural(degrees, 0, 1500)

    def game_v2_soft_up(degrees: int):
        """Turn up softly"""
        _mouse_move_natural(0, -degrees, 1500)

    def game_v2_soft_down(degrees: int):
        """Turn right softly"""
        _mouse_move_natural(0, degrees, 1500)

    def game_v2_turn_left(degrees: int, speed_ms: int = 600):
        """Turn left"""
        _mouse_move_natural(-degrees, 0, speed_ms)

    def game_v2_turn_right(degrees: int, speed_ms: int = 600):
        """Turn right"""
        _mouse_move_natural(degrees, 0, speed_ms)

    def game_v2_turn_left_hold_start():
        """Turn left hold"""
        _mouse_move_natural_hold_start()

    def game_v2_turn_left_hold_release():
        """Turn left hold release"""
        _mouse_move_natural_hold_release()

    def game_v2_turn_right_hold_start():
        """Turn right hold"""
        _mouse_move_natural_hold_start()

    def game_v2_turn_right_hold_release():
        """Turn right hold release"""
        _mouse_move_natural_hold_release()

    def game_v2_turn_up(degrees: int):
        """Turn up"""
        _mouse_move_natural(0, -degrees, 300)

    def game_v2_turn_down(degrees: int):
        """Turn down"""
        _mouse_move_natural(0, degrees, 300)

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

    def game_v2_enable_parrot():
        """Enable parrot game mode"""
        tags = set(ctx.tags)
        if 'user.parrot_game_temp' in tags:
            actions.user.game_v2_disable_parrot()
        else:
            actions.user.add_blue_cursor()
            ctx.tags = ['user.parrot_game_temp']

    def game_v2_disable_parrot():
        """disabled parrot game mode"""
        ctx.tags = []
