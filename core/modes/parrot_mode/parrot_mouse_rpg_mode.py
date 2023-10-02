from talon import Module, Context, actions, ctrl, cron, settings

mod = Module()

nav_job = None
direction = (0, 1)

speeds = {"slow": 1, "medium": 5, "fast": 8, "fastest": 11}
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
class ParrotMouseNavModeActions:
    def parrot_mouse_rpg_move_left():
        """Start moving mouse to the left"""
        print("Start moving mouse to the left")
        start_moving(-1, 0)

    def parrot_mouse_rpg_move_right():
        """Start moving mouse to the right"""
        print("Start moving mouse to the right")
        start_moving(1, 0)

    def parrot_mouse_rpg_move_down():
        """Start moving mouse down"""
        print("Start moving mouse down")
        start_moving(0, 1)

    def parrot_mouse_rpg_move_up():
        """Start moving mouse up"""
        print("Start moving mouse up")
        start_moving(0, -1)

    def parrot_mouse_rpg_repeat_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        print('parrot_mouse_rpg_repeat_dir_by_increment')
        x, y = ctrl.mouse_pos()
        # print(settings.get("user.parrot_rpg_increment_x"))
        increment_x = settings.get("user.parrot_rpg_increment_x")
        increment_y = settings.get("user.parrot_rpg_increment_y")
        print(increment_x)
        print(increment_y)

        dx = direction[0] * increment_x
        dy = direction[1] * increment_y

        if direction:
            ctrl.mouse_move(x + dx, y + dy)

    def parrot_mouse_rpg_repeat_reverse_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        x, y = ctrl.mouse_pos()
        increment_x = settings.get("user.parrot_rpg_increment_x")
        increment_y = settings.get("user.parrot_rpg_increment_y")
        dx = direction[0] * increment_x * -1
        dy = direction[1] * increment_y * -1

        if direction:
            ctrl.mouse_move(x + dx, y + dy)

    def parrot_mouse_rpg_move_slow():
        """Move mouse slower"""
        global speed
        update_speed("slow")

    def parrot_mouse_rpg_move_fast():
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

    def parrot_mouse_rpg_stop():
        """Stop moving mouse"""
        print("parrot mouse nav stop")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)

    def parrot_mouse_rpg_mode_enable():
        """Enable parrot mouse nav mode"""
        print("parrot mouse nav mode enabled")
        actions.user.parrot_freeze_mouse()
        actions.user.add_yellow_cursor()
        actions.user.parrot_mouse_rpg_stop()
        update_speed(speed_default)
        actions.user.parrot_mode_enable_tag("user.parrot_mouse_rpg")
        # actions.mode.disable("user.parrot")
        # actions.mode.disable("command")
        # actions.mode.disable("dictation")
        # actions.mode.enable("user.parrot_mouse_rpg")

    def parrot_mouse_rpg_mode_disable_full():
        """Disable parrot mouse nav mode and exit parrot mode"""
        print("parrot mouse nav mode disabled")
        actions.user.parrot_mouse_rpg_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.user.parrot_mode_reset_tags()
        actions.user.parrot_mode_disable()
        # actions.mode.disable("user.parrot_mouse_rpg")
        # actions.mode.enable("command")
        # actions.mode.disable("dictation")

    def parrot_mouse_rpg_mode_disable():
        """Disable parrot mouse nav mode"""
        print("parrot mouse nav mode disabled")
        actions.user.parrot_mouse_rpg_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.user.parrot_mode_reset_tags()
        actions.user.parrot_mode_enable()