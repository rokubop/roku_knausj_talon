from talon import Module, Context, actions, ctrl, cron, settings

mod = Module()
ctx = Context()

mod.setting(
    "parrot_rpg_increment_x",
    desc="X increment for parrot mouse rpg mode",
    type=int,
    default=26
)
mod.setting(
    "parrot_rpg_increment_y",
    desc="Y increment for parrot mouse rpg mode",
    type=int,
    default=26
)
mod.setting(
    "parrot_rpg_interaction_axis_y_pos",
    desc="Y position of an interaction bar in the application",
    type=int,
    default=140
)

nav_job = None
direction = (0, 1)

speeds = {"slow": 1, "medium": 5, "fast": 8, "fastest": 15}
speed_default = "slow"
speed = speeds[speed_default]

def update_speed(new_speed):
    global speed
    speed = speeds.get(new_speed, speed_default)

def nav_tick():
    global direction
    if direction:
        x, y = ctrl.mouse_pos()
        dx, dy = direction
        ctrl.mouse_move(x + dx * speed, y + dy * speed)

def start_moving(dx, dy):
    global nav_job, direction
    if nav_job:
        cron.cancel(nav_job)
    direction = (dx, dy)
    nav_job = cron.interval("16ms", nav_tick)

@mod.action_class
class RpgMouseActions:
    def rpg_mouse_move_left():
        """Start moving mouse to the left"""
        print("Start moving mouse to the left")
        start_moving(-1, 0)

    def rpg_mouse_move_right():
        """Start moving mouse to the right"""
        print("Start moving mouse to the right")
        start_moving(1, 0)

    def rpg_mouse_move_down():
        """Start moving mouse down"""
        print("Start moving mouse down")
        start_moving(0, 1)

    def rpg_mouse_move_up():
        """Start moving mouse up"""
        print("Start moving mouse up")
        start_moving(0, -1)

    def rpg_mouse_repeat_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        x, y = ctrl.mouse_pos()
        increment_x = settings.get("user.parrot_rpg_increment_x")
        increment_y = settings.get("user.parrot_rpg_increment_y")
        print(increment_x)
        print(increment_y)

        dx = direction[0] * increment_x
        dy = direction[1] * increment_y

        if direction:
            ctrl.mouse_move(x + dx, y + dy)

    def rpg_mouse_repeat_reverse_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        x, y = ctrl.mouse_pos()
        increment_x = settings.get("user.parrot_rpg_increment_x")
        increment_y = settings.get("user.parrot_rpg_increment_y")
        dx = direction[0] * increment_x * -1
        dy = direction[1] * increment_y * -1

        if direction:
            ctrl.mouse_move(x + dx, y + dy)

    def rpg_mouse_move_slow():
        """Move mouse slower"""
        global speed
        update_speed("slow")

    def rpg_mouse_move_fast():
        """Move mouse faster"""
        global speed
        if speed == speeds["slow"]:
            update_speed("medium")
        elif speed == speeds["medium"]:
            update_speed("fast")
        elif speed == speeds["fast"]:
            update_speed("fastest")
        elif speed == speeds["fastest"]:
            return

    def rpg_mouse_move_to_interaction_axis():
        """Mouse move to interaction axis"""
        pos = ctrl.mouse_pos()
        y = settings.get("user.parrot_rpg_interaction_axis_y_pos")
        print(f"the value of y is {y}")
        ctrl.mouse_move(pos[0], y)
        actions.user.rpg_mouse_stop()

    def rpg_mouse_stop():
        """Stop moving mouse"""
        print("parrot mouse nav stop")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)

    def rpg_mouse_mode_enable():
        """Enable parrot mouse nav mode"""
        print("parrot mouse nav mode enabled")
        actions.user.parrot_freeze_mouse()
        actions.user.add_yellow_cursor()
        actions.user.rpg_mouse_stop()
        update_speed(speed_default)
        actions.user.parrot_mode_enable_tag("user.rpg_mouse")

    def rpg_mouse_mode_disable_full():
        """Disable parrot mouse nav mode and exit parrot mode"""
        print("parrot mouse nav mode disabled")
        actions.user.rpg_mouse_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.user.parrot_mode_reset_tags()
        actions.user.parrot_mode_disable()

    def rpg_mouse_mode_disable():
        """Disable parrot mouse nav mode"""
        print("parrot mouse nav mode disabled")
        actions.user.rpg_mouse_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.user.parrot_mode_reset_tags()
        actions.user.parrot_mode_enable()