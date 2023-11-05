from talon import Context, Module, actions, cron, ctrl, settings
import win32api, win32con

mod = Module()
ctx = Context()
ctx_parrot_side_b = Context()
ctx_parrot_pan = Context()
ctx_parrot_fps_compass = Context()
ctx_parrot_fps_flick = Context()

mod.tag("parrot_fps", desc="Tag for fps parrot mode")
mod.tag("parrot_fps_compass", desc="Tag for fps compass parrot mode")
mod.tag("parrot_fps_flick", desc="Tag for fps flick parrot mode")
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
ctx_parrot_fps_compass.matches = """
tag: user.parrot_fps
and tag: user.parrot_fps_compass
and mode: user.parrot
"""
ctx_parrot_fps_flick.matches = """
tag: user.parrot_fps
and tag: user.parrot_fps_flick
and mode: user.parrot
"""
ctx.settings = {
    "key_hold": 64.0,
    "key_wait": 16.0,
}
mod.setting(
    "fps_calibrate_x_360",
    desc="mouse movement amount in order to do a 360",
    type=int,
    default=2000
)
mod.setting(
    "fps_calibrate_y_floor_to_center",
    desc="mouse movement to go from max down to center of screen",
    type=int,
    default=800
)

compass_north_anchor = 0
compass_north_offset = 0
y_offset = 0
last_action = None
set_last_action_job = None

def set_last_action(action):
    global last_action, set_last_action_job
    if set_last_action_job:
        cron.cancel(set_last_action_job)
    last_action = action
    set_last_action_job = cron.after("1s", lambda: set_last_action(None))

repeater_actions = {
    "compass_north": actions.user.fps_compass_go_north_relative,
    "compass_west": actions.user.fps_compass_go_west_relative,
    "compass_east": actions.user.fps_compass_go_east_relative,
    "compass_north_west": actions.user.fps_compass_go_north_west_relative,
    "compass_north_east": actions.user.fps_compass_go_north_east_relative,
    "compass_south_east": actions.user.fps_compass_go_south_east_relative,
    "compass_south_west": actions.user.fps_compass_go_south_west_relative,
    "compass_south": actions.user.fps_compass_go_south_relative,
    "flick_down": actions.user.fps_flick_mouse_down,
    "flick_down_left": actions.user.fps_flick_mouse_down_left,
    "flick_down_right": actions.user.fps_flick_mouse_down_right,
    "flick_up": actions.user.fps_flick_mouse_up,
}

reverser_actions = {
    "compass_north": actions.user.fps_compass_go_south_relative,
    "compass_west": actions.user.fps_compass_go_east_relative,
    "compass_east": actions.user.fps_compass_go_west_relative,
    "compass_north_west": actions.user.fps_compass_go_south_east_relative,
    "compass_north_east": actions.user.fps_compass_go_south_west_relative,
    "compass_south_east": actions.user.fps_compass_go_north_west_relative,
    "compass_south_west": actions.user.fps_compass_go_north_east_relative,
    "compass_south": actions.user.fps_compass_go_north_relative,
    "flick_down": actions.user.fps_flick_center,
    "flick_down_left": actions.user.fps_flick_center,
    "flick_down_right": actions.user.fps_flick_center,
    "flick_up": actions.user.fps_flick_center,
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
    def parrot_tut():
        global last_action
        if last_action:
            if last_action in repeater_actions:
                repeater_actions[last_action]()
        else:
            actions.user.parrot_mouse_click(1)

    def parrot_hiss():
        actions.user.hold_dir_key_mutually_exclusive('w')
    def parrot_hiss_stop(): actions.skip()
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    # def parrot_eh(): actions.user.hold_dir_key_mutually_exclusive('a')
    # def parrot_eh(): actions.user.parrot_position_mode_enable()
    def parrot_er():
        actions.user.enable_parrot_fps_compass()
        cron.after("1s", actions.user.disable_parrot_fps_compass)
    def parrot_shush(): actions.user.hold_dir_key_mutually_exclusive('s')
    def parrot_shush_stop(): actions.skip()
    def parrot_nn(): actions.user.parrot_activate_side_b_briefly()
    def parrot_ee(): actions.user.fps_stop_layer()
    def parrot_palate():
        global last_action
        if last_action:
            if last_action in repeater_actions:
                repeater_actions[last_action]()
        else:
            actions.key("space")
        # else:
        #     actions.user.fps_repeater()
    def parrot_t():actions.key("q")
    def parrot_guh():
        actions.user.enable_parrot_fps_flick()
        cron.after("1s", actions.user.disable_parrot_fps_flick)
        # actions.user.fps_grid()


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
    global direction, x_speed_continuous, y_speed_continuous, compass_north_offset
    if direction:
        dx, dy = direction
        deltax = int(dx * x_speed_continuous)
        compass_north_offset += deltax
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, deltax, int(dy * y_speed_continuous))

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

####################################################################################################
# Flick
@ctx_parrot_fps_flick.action_class("user")
class Actions:
    # def parrot_cluck():
    # def parrot_pop():
    # def parrot_tut(): actions.user.parrot_mouse_click(1)
    # def parrot_ah():
    # def parrot_oh():
    # def parrot_guh():
    # def parrot_t():
    # def parrot_nn():
    # def parrot_palate():
    def parrot_palate():
        actions.user.fps_set_center_anchor()
        actions.user.disable_parrot_fps_flick()
    def parrot_hiss():
        actions.user.fps_flick_mouse_down()
        actions.user.disable_parrot_fps_flick()
    def parrot_hiss_stop(): actions.skip()
    def parrot_eh():
        actions.user.fps_flick_mouse_down_left()
        actions.user.disable_parrot_fps_flick()
    def parrot_er():
        actions.user.fps_flick_mouse_down_right()
        actions.user.disable_parrot_fps_flick()
    def parrot_shush():
        actions.user.fps_flick_mouse_up()
        actions.user.disable_parrot_fps_flick()
    def parrot_shush_stop(): actions.skip()
    def parrot_ee():
        actions.user.fps_flick_mouse_center()
        actions.user.disable_parrot_fps_flick()
    def parrot_pop():
        actions.user.fps_flick_mouse_center()
        actions.user.disable_parrot_fps_flick()

####################################################################################################
# Compass
@ctx_parrot_fps_compass.action_class("user")
class Actions:
    # def parrot_cluck():
    # def parrot_tut():
    # def parrot_nn(): actions.user.parrot_activate_side_b_briefly()
    # def parrot_ee(): actions.user.fps_stop_layer()
    # def parrot_palate():actions.user.fps_grid()
    def parrot_pop():
        actions.user.fps_compass_snap_to_closest_45()
        actions.user.disable_parrot_fps_compass()
    def parrot_palate(): actions.user.fps_compass_set_north_anchor()
    def parrot_hiss():
        actions.user.fps_compass_go_north_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_hiss_stop(): actions.skip()
    def parrot_ah():
        actions.user.fps_compass_go_west_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_oh():
        actions.user.fps_compass_go_east_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_eh():
        actions.user.fps_compass_go_north_west_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_er():
        actions.user.fps_compass_go_north_east_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_guh():
        actions.user.fps_compass_go_south_east_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_t():
        actions.user.fps_compass_go_south_west_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_shush():
        actions.user.fps_compass_go_south_relative()
        actions.user.disable_parrot_fps_compass()
    def parrot_shush_stop(): actions.skip()


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

    def enable_parrot_fps_compass():
        """Enable parrot fps compass"""
        tags = set(ctx.tags)
        tags.add("user.parrot_fps_compass")
        ctx.tags = tags

    def disable_parrot_fps_compass():
        """Disable parrot fps compass"""
        tags = set(ctx.tags)
        tags.discard("user.parrot_fps_compass")
        ctx.tags = tags

    def enable_parrot_fps_flick():
        """Enable parrot fps flick"""
        tags = set(ctx.tags)
        tags.add("user.parrot_fps_flick")
        ctx.tags = tags

    def disable_parrot_fps_flick():
        """Disable parrot fps flick"""
        tags = set(ctx.tags)
        tags.discard("user.parrot_fps_flick")
        ctx.tags = tags

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

@mod.action_class
class FpsCompassActions:
    def fps_compass_set_north_anchor():
        """Set north anchor"""
        global compass_north_offset
        compass_north_offset = 0

    def fps_compass_snap_to_closest_45():
        """Snap to closest 45 degree angle"""
        global compass_north_offset, compass_north_anchor
        x360 = settings.get("user.fps_calibrate_x_360")

        compass_north_offset_normalized = compass_north_offset % x360
        if compass_north_offset_normalized < 0:
            compass_north_offset_normalized += x360

        normalized_degree = (compass_north_offset_normalized / x360 * 360)
        nearest_45_degree = round(normalized_degree/45) * 45
        snap_rotation = nearest_45_degree / 360 * x360
        delta = int(snap_rotation - compass_north_offset)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, delta, 0)
        compass_north_offset += delta

    def fps_compass_go_north_relative():
        """Go north relative to current position"""
        global compass_north_offset, compass_north_anchor
        delta  = compass_north_anchor - compass_north_offset
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, delta, 0)
        compass_north_offset = 0
        set_last_action("compass_north")

    def fps_compass_go_west_relative():
        """Go west relative to current position"""
        global compass_north_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        dx = -int(x360/4)
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
        set_last_action("compass_west")

    def fps_compass_go_east_relative():
        """Go east relative to current position"""
        global compass_north_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        dx = int(x360/4)
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
        set_last_action("compass_east")

    def fps_compass_go_north_west_relative():
        """Go north west relative to current position"""
        global compass_north_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        dx = -int(x360/8)
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
        set_last_action("compass_north_west")

    def fps_compass_go_north_east_relative():
        """Go north east relative to current position"""
        global compass_north_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        dx = int(x360/8)
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
        set_last_action("compass_north_east")

    def fps_compass_go_south_east_relative():
        """Go south east relative to current position"""
        global compass_north_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        dx = int(x360/8) + int(x360/4)
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
        set_last_action("compass_south_east")

    def fps_compass_go_south_west_relative():
        """Go south west relative to current position"""
        global compass_north_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        dx = -(int(x360/8) + int(x360/4))
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
        set_last_action("compass_south_west")

    def fps_compass_go_south_relative():
        """Go south relative to current position"""
        x360 = settings.get("user.fps_calibrate_x_360")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x360/2), 0)
        set_last_action("compass_south")

@mod.action_class
class FpsFlickActions:
    def fps_set_center_anchor():
        """Set center anchor"""
        global y_offset
        y_offset = 0

    def fps_flick_mouse_down():
        """Flick mouse down"""
        global compass_north_offset, compass_north_anchor, y_offset
        y90 = settings.get("user.fps_calibrate_y_floor_to_center")
        target_y_pos = int(y90 / 2)
        dy = target_y_pos - y_offset
        y_offset += dy
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, dy)
        set_last_action("flick_down")

    def fps_flick_mouse_down_left():
        """Flick mouse down left"""
        global compass_north_offset, compass_north_anchor, y_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        y90 = settings.get("user.fps_calibrate_y_floor_to_center")
        dx = -int(x360/8)
        target_y_pos = int(y90 / 2)
        dy = target_y_pos - y_offset
        y_offset += dy
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
        set_last_action("flick_down_left")

    def fps_flick_mouse_down_right():
        """Flick mouse down right"""
        global compass_north_offset, compass_north_anchor, y_offset
        x360 = settings.get("user.fps_calibrate_x_360")
        y90 = settings.get("user.fps_calibrate_y_floor_to_center")
        dx = int(x360/8)
        target_y_pos = int(y90 / 2)
        dy = target_y_pos - y_offset
        y_offset += dy
        compass_north_offset += dx
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
        set_last_action("flick_down_right")

    def fps_flick_mouse_up():
        """Flick mouse up"""
        global compass_north_offset, compass_north_anchor, y_offset
        y90 = settings.get("user.fps_calibrate_y_floor_to_center")
        target_y_pos = -int(y90 / 2)
        dy = target_y_pos - y_offset
        y_offset += dy
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, dy)
        set_last_action("flick_up")

    def fps_flick_mouse_center():
        """Flick mouse center"""
        global y_offset
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -y_offset)
        y_offset = 0
        set_last_action("flick_center")