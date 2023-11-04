from talon import Context, Module, actions, cron, ctrl, settings
import win32api, win32con

mod = Module()
ctx = Context()
ctx_parrot_side_b = Context()
ctx_parrot_pan = Context()

mod.tag("parrot_fps", desc="Tag for fps parrot mode")
ctx.matches = """
tag: user.parrot_fps
and mode: user.parrot
"""
ctx_parrot_side_b.matches = """
tag: user.parrot_side_b
and tag: user.parrot_fps
and mode: user.parrot
"""
ctx_parrot_pan.matches = """
tag: user.parrot_pan
and tag: user.parrot_fps
and mode: user.parrot
"""
ctx.settings = {
    "key_hold": 64.0,
    "key_wait": 16.0,
}

@ctx.action_class("user")
class Actions:
    def parrot_cluck():
        actions.user.parrot_mode_disable()
        actions.user.fps_stop_layer()
        actions.user.fps_stop_layer()
    def parrot_pop():
        actions.key('e')
        actions.user.parrot_mouse_click(0)
        actions.user.fps_stop_layer()
    # def parrot_t(): actions.skip()
    # def parrot_guh(): actions.skip()
    def parrot_tut(): actions.user.parrot_mouse_click(1)

    def parrot_hiss():
        actions.user.hold_dir_key_mutually_exclusive('w')
    def parrot_hiss_stop(): actions.skip()
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    def parrot_eh(): actions.user.hold_dir_key_mutually_exclusive('a')
    def parrot_er(): actions.user.hold_dir_key_mutually_exclusive('d')
    def parrot_shush(): actions.user.hold_dir_key_mutually_exclusive('s')
    def parrot_shush_stop(): actions.skip()
    def parrot_nn(): actions.user.parrot_activate_side_b_briefly()
    def parrot_ee(): actions.user.fps_stop_layer()
    def parrot_palate():actions.user.fps_grid()
    # def parrot_palate():actions.user.fps_repeater()
    def parrot_t():actions.key("q")
    # def parrot_guh(): actions.user.fps_grid()


@ctx_parrot_side_b.action_class("user")
class Actions:
    def parrot_cluck():
        if (actions.user.parrot_side_b_source_tag() == "user.parrot_fps"):
            actions.user.parrot_mode_append_tag("user.parrot_default")
            actions.user.parrot_mode_remove_tag("user.parrot_fps")
        else:
            actions.user.parrot_mode_reset_tags()
    def parrot_hiss():
        if (actions.user.parrot_side_b_source_tag() == "user.parrot_pan"):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('w')
        else:
            actions.user.parrot_mode_append_tag("user.parrot_pan")
            actions.user.add_color_cursor("FFA500")
            actions.user.mouse_move_native_down()
        actions.user.parrot_side_b_disable()
    def parrot_hiss_stop(): pass
    def parrot_shush():
        if (actions.user.parrot_side_b_source_tag() == "user.parrot_pan"):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('s')
        else:
            actions.user.parrot_mode_append_tag("user.parrot_pan")
            actions.user.add_color_cursor("FFA500")
            actions.user.mouse_move_native_up()
        actions.user.parrot_side_b_disable()
    def parrot_shush_stop(): pass
    def parrot_eh(): actions.user.parrot_position_mode_enable()
    def parrot_ee(): win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1200, 0)

@ctx_parrot_pan.action_class("user")
class Actions:
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    def parrot_hiss():
        if (actions.user.parrot_mode_has_tag("user.parrot_side_b")):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('w')
        else:
            actions.user.mouse_move_native_down()
    def parrot_hiss_stop(): pass
    def parrot_shush():
        print("shush from pan")
        if (actions.user.parrot_mode_has_tag("user.parrot_side_b")):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('s')
        else:
            actions.user.mouse_move_native_up()
    def parrot_shush_stop(): pass
    def parrot_eh(): actions.user.hold_dir_key_mutually_exclusive('a')
    def parrot_er(): actions.user.hold_dir_key_mutually_exclusive('d')
    def parrot_nn(): actions.user.parrot_activate_side_b_briefly()

####################################################################################################
# Mouse actions

cam_job = None
direction = None

mod.setting(
    "fps_mouse_x_speed_continuous",
    desc="x continuous speed",
    type=int,
    default=10
)
mod.setting(
    "fps_mouse_y_speed_continuous",
    desc="y continuous speed",
    type=int,
    default=10
)
mod.setting(
    "fps_mouse_x_speed_increment",
    desc="x incremental speed",
    type=int,
    default=100
)
mod.setting(
    "fps_mouse_y_speed_increment",
    desc="y incremental speed",
    type=int,
    default=100
)
mod.tag("fps_orbit", desc="Tag for orbitting")
x_speed_continuous = settings.get("user.fps_mouse_x_speed_continuous")
y_speed_continuous = settings.get("user.fps_mouse_y_speed_continuous")
x_speed_increment = settings.get("user.fps_mouse_x_speed_increment")
y_speed_increment = settings.get("user.fps_mouse_y_speed_increment")

def nav_tick():
    global direction, x_speed_continuous, y_speed_continuous
    if direction:
        dx, dy = direction
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx * x_speed_continuous), int(dy * y_speed_continuous))

def start_moving(dx, dy):
    global cam_job, direction, x_speed_continuous, y_speed_continuous
    x_speed_continuous = settings.get("user.fps_mouse_x_speed_continuous")
    y_speed_continuous = settings.get("user.fps_mouse_y_speed_continuous")
    if cam_job:
        cron.cancel(cam_job)
    direction = (dx, dy)
    cam_job = cron.interval("16ms", nav_tick)

    tags = set(ctx.tags)
    tags.add("user.fps_orbit")
    ctx.tags = tags

@mod.action_class
class MouseActions:
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
        global cam_job, direction
        if cam_job:
            cron.cancel(cam_job)
            cam_job = None
        tags = set(ctx.tags)
        tags.discard("user.fps_orbit")
        ctx.tags = tags

    def fps_repeater():
        """Repeat previous direction"""
        if "user.fps_orbit" in ctx.tags:
            actions.user.mouse_move_repeat_dir_by_increment()
        else:
            actions.key("space")

    def mouse_move_repeat_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        global direction
        dx = direction[0] * settings.get("user.fps_mouse_x_speed_increment")
        dy = direction[1] * settings.get("user.fps_mouse_y_speed_increment")

        if direction:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy))
        actions.user.fps_stop_layer()

    def mouse_move_repeat_reverse_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        global direction
        dx = direction[0] * settings.get("user.fps_mouse_x_speed_increment") * -1
        dy = direction[1] * settings.get("user.fps_mouse_y_speed_increment") * -1

        if direction:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy))

    def fps_stop_layer():
        """Stop moving mouse or direction"""
        if cam_job:
            actions.user.mouse_move_native_stop()
        else:
            actions.key("shift:up")
            actions.user.release_dir_keys_all()

    def fps_grid_disable():
        """Disable roku grid"""
        actions.mode.enable("user.parrot")
        actions.mode.disable("user.roku_grid")

    def fps_grid():
        """Temporarily enable roku grid"""
        actions.mode.disable("user.parrot")
        actions.mode.enable("user.roku_grid")
        # cron.after("1s", actions.user.fps_grid_disable)
