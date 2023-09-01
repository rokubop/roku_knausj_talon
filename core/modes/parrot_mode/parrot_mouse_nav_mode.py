from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.mode("parrot_mouse_nav", "Parrot Mode for controlling mouse, modifiers, and scrolling")
ctx = Context()

nav_job = None
direction = None
default_speed = 3
slow_speed = 1
fast_speed = 6
speed = default_speed

def set_slow_speed():
    global speed
    speed = slow_speed

def set_default_speed():
    global speed
    speed = default_speed

def set_fast_speed():
    global speed
    speed = fast_speed

def nav_tick():
    global direction
    x, y = ctrl.mouse_pos()
    if direction == "left":
        ctrl.mouse_move(x - speed, y)
    elif direction == "right":
        ctrl.mouse_move(x + speed, y)
    elif direction == "up":
        ctrl.mouse_move(x, y - speed)
    elif direction == "down":
        ctrl.mouse_move(x, y + speed)

@mod.action_class
class ParrotMouseNavModeActions:
    def parrot_mouse_nav_move_left():
        """Start moving mouse to the left"""
        print("Start moving mouse to the left")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)
        direction = "left"
        nav_job = cron.interval("16ms", nav_tick)

    def parrot_mouse_nav_move_right():
        """Start moving mouse to the right"""
        print("Start moving mouse to the right")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)
        direction = "right"
        nav_job = cron.interval("16ms", nav_tick)

    def parrot_mouse_nav_move_down():
        """Start moving mouse down"""
        print("Start moving mouse to the down")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)
        direction = "down"
        nav_job = cron.interval("16ms", nav_tick)

    def parrot_mouse_nav_move_up():
        """Start moving mouse up"""
        print("Start moving mouse to the up")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)
        direction = "up"
        nav_job = cron.interval("16ms", nav_tick)

    def parrot_mouse_nav_move_slow():
        """Move the mouse slowly"""
        global speed, fast_speed
        if speed == fast_speed:
            set_default_speed()
        else:
            set_slow_speed()

    def parrot_mouse_nav_move_fast():
        """Move the mouse fast"""
        global speed, slow_speed
        if speed == slow_speed:
            set_default_speed()
        else:
            set_fast_speed()

    def parrot_mouse_nav_stop():
        """Stop moving the mouse"""
        print("parrot mouse nav stop")
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)
        direction = None

mod = Module()
@mod.action_class
class UserActions:
    def parrot_mouse_nav_mode_enable():
        """Enable parrot mouse nav mode"""
        print("parrot mouse nav mode enabled")
        actions.user.add_yellow_cursor()
        actions.user.parrot_mouse_nav_stop()
        set_default_speed()
        actions.mode.disable("user.parrot")
        actions.mode.disable("command")
        actions.mode.disable("dictation")
        actions.mode.enable("user.parrot_mouse_nav")

    def parrot_mouse_nav_mode_disable():
        """Disable parrot nav mode"""
        print('parrot mouse nav mode disabled')
        actions.user.parrot_mouse_nav_stop()
        actions.user.clear_screen_regions()
        set_default_speed()
        actions.mode.disable("user.parrot_mouse_nav")
        actions.mode.disable("command")
        actions.mode.disable("dictation")

@ctx.action_class("user")
class UserActions:
    def virtual_region_one():
        print('got it')