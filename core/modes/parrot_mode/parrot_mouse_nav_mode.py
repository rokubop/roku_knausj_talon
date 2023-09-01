from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.mode("parrot_mouse_nav", "Parrot Mode for controlling mouse, modifiers, and scrolling")
ctx = Context()

nav_job = None
direction = None

speeds = {"slow": 1, "default": 4, "fast": 10}
speed = speeds["fast"]

def update_speed(new_speed):
    global speed
    speed = speeds.get(new_speed, speeds["default"])

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
    def parrot_mouse_nav_move_left():
        """Start moving mouse to the left"""
        print("Start moving mouse to the left")
        start_moving(-1, 0)

    def parrot_mouse_nav_move_right():
        """Start moving mouse to the right"""
        print("Start moving mouse to the right")
        start_moving(1, 0)

    def parrot_mouse_nav_move_down():
        """Start moving mouse down"""
        print("Start moving mouse down")
        start_moving(0, 1)

    def parrot_mouse_nav_move_up():
        """Start moving mouse up"""
        print("Start moving mouse up")
        start_moving(0, -1)

    def parrot_mouse_nav_move_slow():
        """Move mouse slowly"""
        update_speed("slow" if speed != speeds["fast"] else "default")

    def parrot_mouse_nav_move_fast():
        """Move mouse quickly"""
        update_speed("fast" if speed != speeds["slow"] else "default")

    def parrot_mouse_nav_stop():
        """Stop moving mouse"""
        print("parrot mouse nav stop")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)
        direction = None

@mod.action_class
class UserActions:
    def parrot_mouse_nav_mode_enable():
        """Enable parrot mouse nav mode"""
        print("parrot mouse nav mode enabled")
        actions.user.add_yellow_cursor()
        actions.user.parrot_mouse_nav_stop()
        update_speed("fast")
        actions.mode.disable("user.parrot")
        actions.mode.disable("command")
        actions.mode.disable("dictation")
        actions.mode.enable("user.parrot_mouse_nav")

    def parrot_mouse_nav_mode_disable():
        """Disable parrot mouse nav mode"""
        print("parrot mouse nav mode disabled")
        actions.user.parrot_mouse_nav_stop()
        actions.user.clear_screen_regions()
        update_speed("fast")
        actions.mode.disable("user.parrot_mouse_nav")
        actions.mode.disable("command")
        actions.mode.disable("dictation")