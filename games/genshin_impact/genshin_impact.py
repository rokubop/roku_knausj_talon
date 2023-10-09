from talon import Module, Context, actions, cron, ctrl
import win32api, win32con

mod = Module()
ctx = Context()
mod.apps.genshin_impact = r"""
os: windows
and app.exe: GenshinImpact.exe
"""
ctx.matches = r"""
os: windows
app: genshin_impact
"""

mod.tag("genshin_melee", desc="Tag for melee mode")
mod.tag("genshin_orbit", desc="Tag for orbitting")

setting_mouse_move_increment_x = mod.setting(
    "mouse_move_increment_x",
    desc="X increment for mouse move",
    type=int,
    default=26
)

setting_mouse_move_increment_y = mod.setting(
    "mouse_move_increment_y",
    desc="Y increment for mouse move",
    type=int,
    default=26
)


cam_job = None
direction = None

speeds = {"slow": 5, "medium": 10, "fast": 20, "fastest": 30}
speed_default = "slow"
speed = speeds[speed_default]

def update_speed(new_speed):
    global speed
    speed = speeds.get(new_speed, speed_default)

def nav_tick():
    global direction
    if direction:
        dx, dy = direction
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx * speed), int(dy * speed))

def start_moving(dx, dy):
    global cam_job, direction
    if cam_job:
        cron.cancel(cam_job)
    direction = (dx, dy)
    cam_job = cron.interval("16ms", nav_tick)

    tags = set(ctx.tags)
    tags.add("user.genshin_orbit")
    ctx.tags = tags

is_dragging_mouse = False
is_holding_alt = False

def fight_tick():
    actions.mouse_click()

fight_job = None

@mod.action_class
class Actions:
    def genshin_toggle_fight():
        """Toggle fight mode"""
        global fight_job
        if fight_job:
            cron.cancel(fight_job)
            fight_job = None
        else:
            fight_job = cron.interval("100ms", fight_tick)

    def genshin_stop_fight():
        """Toggle fight mode"""
        global fight_job
        if fight_job:
            cron.cancel(fight_job)
            fight_job = None

    def genshin_repeater():
        """Repeat previous direction"""
        print("hello")
        print(ctx.tags)
        if "user.genshin_orbit" in ctx.tags:
            print("got it")
            actions.user.mouse_move_repeat_dir_by_increment()
        else:
            actions.core.repeat_phrase()

    def genshin_scan_toggle():
        """Toggle scan mode"""
        global is_dragging_mouse
        if is_dragging_mouse:
            actions.mouse_release(2)
            is_dragging_mouse = False
        else:
            actions.mouse_drag(2)
            is_dragging_mouse = True

    def genshin_curse_toggle():
        """Toggle cursor mode"""
        global is_holding_alt
        if is_holding_alt:
            actions.key("alt:up")
            is_holding_alt = False
        else:
            actions.key("alt:down")
            is_holding_alt = True

    def mouse_move_native_left():
        """Moves the mouse cursor to the left"""
        start_moving(-1, 0)

    def mouse_move_native_right():
        """Moves the mouse cursor to the right"""
        start_moving(1, 0)

    def mouse_move_native_up():
        """Moves the mouse cursor up"""
        start_moving(0, -1)

    def mouse_move_native_down():
        """Moves the mouse cursor down"""
        start_moving(0, 1)

    def mouse_move_native_stop():
        """Stop moving mouse"""
        print("parrot mouse nav stop")
        global cam_job, direction
        if cam_job:
            cron.cancel(cam_job)
            cam_job = None
        tags = set(ctx.tags)
        tags.discard("user.genshin_orbit")
        ctx.tags = tags

    def mouse_move_repeat_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        global direction
        x, y = ctrl.mouse_pos()
        increment_x = setting_mouse_move_increment_x.get()
        increment_y = setting_mouse_move_increment_y.get()
        dx = direction[0] * increment_x
        dy = direction[1] * increment_y

        print("increment disc")
        print("direction", direction)
        if direction:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx * speed), int(dy * speed))

    def mouse_move_repeat_reverse_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        global direction
        x, y = ctrl.mouse_pos()
        increment_x = setting_mouse_move_increment_x.get()
        increment_y = setting_mouse_move_increment_y.get()
        dx = direction[0] * increment_x * -1
        dy = direction[1] * increment_y * -1

        if direction:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx * speed), int(dy * speed))

    def genshin_stop_layer():
        """Stop moving mouse or direction"""
        if cam_job:
            actions.user.mouse_move_native_stop()
        else:
            actions.key("shift:up")
            actions.user.release_dir_keys_all()

    def genshin_parrot_mode_enable():
        """Enable parrot mode"""
        actions.user.parrot_mode_enable()
        if "user.genshin_melee" in ctx.tags:
            actions.user.add_color_cursor('97245a')

    def genshin_fight_mode_toggle():
        """Toggle fight mode"""
        global fight_job
        if "user.genshin_melee" in ctx.tags:
            actions.user.genshin_fight_mode_disable()
        else:
            tags = set(ctx.tags)
            tags.add("user.genshin_melee")
            ctx.tags = tags
            actions.user.add_color_cursor('97245a')

    def genshin_fight_mode_disable():
        """Disable fight mode"""
        global fight_job
        tags = set(ctx.tags)
        tags.discard("user.genshin_melee")
        ctx.tags = tags
        if fight_job:
            cron.cancel(fight_job)
            fight_job = None
