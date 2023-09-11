from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.mode("parrot_mouse_rpg", "Parrot Mode for controlling mouse, modifiers, and scrolling")
ctx = Context()

nav_job = None
direction = None

speeds = {"slow": 1, "medium": 5, "fast": 8, "fastest": 11}
speed_default = "slow"
speed = speed_default

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
        direction = None

@mod.action_class
class UserActions:
    def parrot_mouse_rpg_mode_enable():
        """Enable parrot mouse nav mode"""
        print("parrot mouse nav mode enabled")
        actions.user.add_yellow_cursor()
        actions.user.parrot_mouse_rpg_stop()
        update_speed(speed_default)
        actions.mode.disable("user.parrot")
        actions.mode.disable("command")
        actions.mode.disable("dictation")
        actions.mode.enable("user.parrot_mouse_rpg")

    def parrot_mouse_rpg_mode_disable():
        """Disable parrot mouse nav mode"""
        print("parrot mouse nav mode disabled")
        actions.user.parrot_mouse_rpg_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.mode.disable("user.parrot_mouse_rpg")
        actions.mode.enable("command")
        actions.mode.disable("dictation")