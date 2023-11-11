from talon import Context, Module, actions, cron, ctrl, settings
import time
import win32api, win32con

mod = Module()
ctx = Context()
ctx_parrot_side_b = Context()
ctx_parrot_pan = Context()
ctx_parrot_fps_compass = Context()
ctx_parrot_fps_flick = Context()
ctx_parrot_fps_walk_dir = Context()
ctx_parrot_fps_orbit_scan = Context()
ctx_fps_room = Context()
ctx_fps_world = Context()
ctx_fps_side_b = Context()
ctx_fps_side_c = Context()

mod.tag("parrot_fps", desc="Tag for fps parrot mode")
mod.tag("parrot_fps_compass", desc="Tag for fps compass parrot mode")
mod.tag("parrot_fps_flick", desc="Tag for fps flick parrot mode")
mod.tag("parrot_fps_walk_dir", desc="Tag for fps walk dir")
mod.tag("parrot_fps_orbit_scan", desc="Tag for fps orbit scan")
mod.tag("fps_room", desc="Tag for fps room")
mod.tag("fps_world", desc="Tag for fps world")
mod.tag("fps_side_b", desc="Tag for fps side b")
mod.tag("fps_side_c", desc="Tag for fps side c")
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
ctx_parrot_fps_walk_dir.matches = """
tag: user.parrot_fps
and tag: user.parrot_fps_walk_dir
and mode: user.parrot
"""
ctx_parrot_fps_orbit_scan.matches = """
tag: user.parrot_fps
and tag: user.parrot_fps_orbit_scan
and mode: user.parrot
"""
ctx_fps_room.matches = """
tag: user.parrot_fps
and tag: user.fps_room
and mode: user.parrot
"""
ctx_fps_world.matches = """
tag: user.parrot_fps
and tag: user.fps_world
and mode: user.parrot
"""
ctx_fps_side_b.matches = """
tag: user.parrot_fps
and tag: user.fps_side_b
and mode: user.parrot
and os: windows
"""
ctx_fps_side_c.matches = """
tag: user.parrot_fps
and tag: user.fps_side_c
and mode: user.parrot
and os: windows
"""

ctx.settings = {
    "key_hold": 64.0,
    "key_wait": 16.0,
}
ctx.tags = ["user.parrot_fps"]

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
last_mode = "parrot_fps_compass"

def set_last_action(action):
    global last_action, set_last_action_job
    if set_last_action_job:
        cron.cancel(set_last_action_job)
    last_action = action
    set_last_action_job = cron.after("3s", lambda: set_last_action(None))

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

is_running = False
cluck_brief = None

@ctx_fps_room.action_class("user")
class FpsRoom:
    def parrot_palate(): actions.user.fps_flick_mouse_down_toggle()
    def parrot_cluck():
        if not actions.user.fps_check_cluck_should_exit_parrot_mode():
            actions.key('e')
            actions.user.parrot_mouse_click(0)
            actions.user.fps_stop_layer()
    def parrot_pop(): actions.user.fps_compass_snap_to_closest_90()
    def parrot_tut(): actions.user.parrot_mouse_click(1)

@ctx_fps_world.action_class("user")
class FpsWorld:
    def parrot_palate(): actions.key("space")
    def parrot_cluck():
        if not actions.user.fps_check_cluck_should_exit_parrot_mode():
            actions.key("shift")
    def parrot_pop(): actions.user.fps_compass_snap_to_closest_90()
    def parrot_tut(): print("tut")

@ctx.action_class("user")
class FpsDefault:
    # base
    def parrot_mode_on_enable():
        actions.user.toggle_world_or_room_tag('world')
        actions.user.hud_publish_content("pop=align\ncluck=click\ntut=right click\npalate=look down", "example", "World mode")
        actions.user.hud_add_log('success', '<*Note:/> Parrot mode enabled')
    def parrot_eh(): actions.user.fps_direction_go_or_toggle()
    def parrot_guh(): actions.user.fps_direction_back_or_toggle()
    def parrot_ah(): actions.user.fps_turn_left_soft_continuous()
    def parrot_oh(): actions.user.fps_turn_right_soft_continuous()
    def parrot_hiss(): actions.user.fps_turn_left()
    def parrot_hiss_stop(): actions.user.fps_turn_left_stop()
    def parrot_shush(): actions.user.fps_turn_right()
    def parrot_shush_stop(): actions.user.fps_turn_right_stop()
    def parrot_ee():
        actions.user.fps_stop_layer()
        actions.user.fps_turn_halt()

    # modes
    def parrot_nn(): actions.user.enable_fps_side_b_briefly()
    def parrot_er(): actions.user.enable_fps_side_c_briefly()
    def parrot_t(): print("t")

    # room mode - er ah
    # world mode - er oh
    # position mode - er eh
    # exit mode - er cluck

@ctx_fps_side_b.action_class("user")
class FpsDefaultSideB:
    def parrot_eh():
        actions.user.disable_fps_side_b()
        actions.user.parrot_position_mode_enable()
    def parrot_palate():
        actions.user.disable_fps_side_b()
        actions.user.toggle_world_or_room_tag()
    def parrot_hiss():
        actions.user.disable_fps_side_b()
        actions.user.enable_parrot_fps_orbit_scan()
        actions.user.mouse_move_native_down()
    def parrot_hiss_stop(): actions.skip()
    def parrot_shush():
        actions.user.disable_fps_side_b()
        actions.user.enable_parrot_fps_orbit_scan()
        actions.user.mouse_move_native_up()
    def parrot_shush_stop(): actions.skip()
    # def parrot_cluck():
    #     actions.user.hud_add_log('warning', '<*Note:/> Parrot mode disabled')
    #     actions.user.parrot_mode_disable()
    def parrot_er():
        actions.user.disable_fps_side_b()
        actions.user.parrot_rpg_mouse_mode_enable()
    def parrot_pop(): actions.user.fps_compass_set_north_anchor()

# @ctx.action_class("user")
# class Actions:
#     def parrot_cluck():
#         actions.user.parrot_mode_disable()
#         actions.user.fps_stop_layer()
#         actions.user.fps_stop_layer()
#     def parrot_pop():
#         actions.key('e')
#         actions.user.parrot_mouse_click(0)
#         actions.user.fps_stop_layer()
#     def parrot_t():
#         global is_running
#         if is_running:
#             actions.key("shift:up")
#             is_running = False
#         else:
#             actions.key("shift:down")
#             is_running = True
#     # def parrot_guh(): actions.skip()
#     def parrot_tut():
#         global last_action
#         if last_action:
#             if last_action in repeater_actions:
#                 repeater_actions[last_action]()
#         else:
#             actions.user.parrot_mouse_click(1)
#     def parrot_hiss():
#         actions.user.hold_dir_key_mutually_exclusive('w')
#     def parrot_hiss_stop(): actions.skip()
#     def parrot_ah():
#         global last_mode
#         if last_mode == "parrot_fps_compass":
#             actions.user.fps_compass_go_north_west_relative()
#             actions.user.fps_compass_snap_to_closest_45()
#         elif last_mode == "parrot_fps_orbit_scan":
#             actions.user.mouse_move_native_left()
#         elif last_mode == "parrot_fps_move_dir":
#             actions.user.hold_dir_key_mutually_exclusive('a')
#     def parrot_oh():
#         global last_mode
#         if last_mode == "parrot_fps_compass":
#             actions.user.fps_compass_go_north_east_relative()
#             actions.user.fps_compass_snap_to_closest_45()
#         elif last_mode == "parrot_fps_orbit_scan":
#             actions.user.mouse_move_native_right()
#         elif last_mode == "parrot_fps_move_dir":
#             actions.user.hold_dir_key_mutually_exclusive('d')
#     def parrot_eh():
#         global last_mode
#         if last_mode == "parrot_fps_move_dir":
#             actions.user.parrot_mode_reset_tags()
#             actions.user.parrot_position_mode_enable()
#         last_mode = "parrot_fps_move_dir"
#     # def parrot_eh(): actions.user.parrot_position_mode_enable()
#     def parrot_er():
#         global last_mode
#         last_mode = "parrot_fps_compass"
#         actions.user.enable_parrot_fps_compass()
#         cron.after("1s", actions.user.disable_parrot_fps_compass)
#     def parrot_shush(): actions.user.hold_dir_key_mutually_exclusive('s')
#     def parrot_shush_stop(): actions.skip()
#     def parrot_nn():
#         global last_mode
#         last_mode = "parrot_fps_orbit_scan"
#         actions.user.enable_parrot_fps_orbit_scan()
#         # actions.user.parrot_activate_side_b_briefly()
#     def parrot_ee(): actions.user.fps_stop_layer()
#     def parrot_palate():
#         global last_action
#         if last_action:
#             if last_action in repeater_actions:
#                 repeater_actions[last_action]()
#         else:
#             actions.key("space")
#     # def parrot_t(): actions.key("q")
#     def parrot_guh():
#         actions.user.fps_flick_mouse_down_toggle()
#         # actions.user.enable_parrot_fps_flick()
#         # cron.after("1s", actions.user.disable_parrot_fps_flick)
#         # actions.user.fps_grid()


# @ctx_parrot_side_b.action_class("user")
# class FpsDefaultA:
#     def parrot_cluck():
#         if (actions.user.parrot_side_b_source_tag() == "user.parrot_fps"):
#             actions.user.parrot_mode_append_tag("user.parrot_default")
#             actions.user.parrot_mode_remove_tag("user.parrot_fps")
#         else:
#             actions.user.parrot_mode_reset_tags()
#     def parrot_hiss():
#         if (actions.user.parrot_side_b_source_tag() == "user.parrot_pan"):
#             actions.user.parrot_pan_mode_disable()
#             actions.user.hold_dir_key_mutually_exclusive('w')
#         else:
#             actions.user.parrot_mode_append_tag("user.parrot_pan")
#             actions.user.add_color_cursor("FFA500")
#             actions.user.mouse_move_native_down()
#         actions.user.parrot_side_b_disable()
#     def parrot_hiss_stop(): pass
#     def parrot_shush():
#         if (actions.user.parrot_side_b_source_tag() == "user.parrot_pan"):
#             actions.user.parrot_pan_mode_disable()
#             actions.user.hold_dir_key_mutually_exclusive('s')
#         else:
#             actions.user.parrot_mode_append_tag("user.parrot_pan")
#             actions.user.add_color_cursor("FFA500")
#             actions.user.mouse_move_native_up()
#         actions.user.parrot_side_b_disable()
#     def parrot_shush_stop(): pass
#     def parrot_eh(): actions.user.parrot_position_mode_enable()
#     def parrot_ee(): win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1200, 0)

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
        actions.user.hud_publish_mouse_particle('float_up', 'ff0000')
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
    def parrot_palate():
        actions.user.fps_compass_set_north_anchor()
        actions.user.hud_publish_mouse_particle('float_up', 'ff0000')
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

####################################################################################################
# Walk Direction
@ctx_parrot_fps_walk_dir.action_class("user")
class Actions:
    def parrot_ee(): actions.user.fps_stop_layer()
    def parrot_ah():
        actions.user.hold_dir_key_mutually_exclusive('a')
    def parrot_oh():
        actions.user.hold_dir_key_mutually_exclusive('d')

####################################################################################################
# Orbit Scan
@ctx_parrot_fps_orbit_scan.action_class("user")
class Actions:
    def parrot_palate(): actions.user.mouse_move_repeat_dir_by_increment()
    def parrot_tut(): actions.user.mouse_move_repeat_reverse_dir_by_increment()
    def parrot_ee(): actions.user.fps_stop_layer()
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    def parrot_hiss(): actions.user.mouse_move_native_down()
    def parrot_hiss_stop(): pass
    def parrot_shush(): actions.user.mouse_move_native_up()
    def parrot_shush_stop(): pass
    def parrot_nn(): actions.user.disable_parrot_fps_orbit_scan()
    def parrot_cluck():
        actions.user.disable_parrot_fps_orbit_scan()
    def parrot_er():
        actions.user.disable_parrot_fps_orbit_scan()
        actions.next()
    def parrot_eh():
        actions.user.disable_parrot_fps_orbit_scan()
        actions.next()
    def parrot_guh():
        actions.user.disable_parrot_fps_orbit_scan()
        actions.next()

fps_stop_curve = {
    '20': 40,
    '19': 30,
    '18': 10,
    '17': 5,
    '16': 4,
    '15': 4,
    '14': 3,
    '13': 3,
    '12': 2,
    '11': 1,
    '10': 1,
    '9': 1,
    '8': 1,
    '7': 1,
    '6': 1,
    '5': 1,
    '4': 1,
    '3': 1,
    '2': 1,
    '1': 1,
    '0': 0
}
fps_turn_job = None
fps_turn_dir = -1
fps_turn_ts = None
fps_turn_multiplier_linear = 0
fps_turn_multiplier_dynamic = fps_stop_curve[str(fps_turn_multiplier_linear)]
fps_turn_stop = False

def fps_multiplier_reset():
    fps_update_val_multiplier(20)

def fps_update_val_multiplier(val: int):
    global fps_turn_multiplier_linear, fps_turn_multiplier_dynamic
    print('val:', val)
    fps_turn_multiplier_linear = val
    fps_turn_multiplier_dynamic = fps_stop_curve[str(fps_turn_multiplier_linear)]

def fps_turn_tick():
    global fps_turn_dir, fps_turn_ts, fps_turn_multiplier_linear, fps_turn_multiplier_dynamic, fps_turn_job, fps_turn_stop, compass_north_offset
    dx = int(fps_turn_dir * fps_turn_multiplier_dynamic)
    compass_north_offset += dx
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)
    if fps_turn_stop and fps_turn_multiplier_linear > 0:
        fps_update_val_multiplier(fps_turn_multiplier_linear - 1)
    if fps_turn_multiplier_linear <= 0:
        _fps_turn_halt()

def _fps_turn_halt():
    global fps_turn_job, fps_turn_stop
    if fps_turn_job:
        cron.cancel(fps_turn_job)
    fps_turn_job = None
    fps_turn_stop = True
    fps_update_val_multiplier(0)

def _fps_turn_stop():
    global fps_turn_stop
    fps_turn_stop = True

cluck_brief = False

def disable_cluck_brief():
    global cluck_brief
    cluck_brief = False

@mod.action_class
class ModeActions:
    def fps_check_cluck_should_exit_parrot_mode():
        """Check if cluck should exit parrot mode"""
        global cluck_brief
        if cluck_brief:
            actions.user.hud_add_log('error', '<*Note:/> Parrot mode disabled')
            actions.user.parrot_mode_disable()
            cluck_brief = False
            return True
        cluck_brief = True
        cron.after("1s", disable_cluck_brief)
        return False

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

    def fps_turn_halt():
        """Halt turning"""
        _fps_turn_halt()

    def fps_turn_left():
        """Turn left"""
        global fps_turn_job, fps_turn_dir, fps_turn_ts, fps_turn_stop
        fps_turn_stop = False
        fps_multiplier_reset()

        if fps_turn_job != None:
            if fps_turn_dir == -1:
                fps_multiplier_reset()
                return
            else:
                fps_turn_dir = -1
                fps_multiplier_reset()
                fps_turn_ts = time.perf_counter()

        if fps_turn_job is None:
            fps_turn_dir = -1
            fps_turn_ts = time.perf_counter()
            fps_turn_tick()
            fps_turn_job = cron.interval("16ms", fps_turn_tick)

    def fps_turn_left_stop():
        """Turn left stop"""
        _fps_turn_stop()

    def fps_turn_right():
        """Turn right"""
        global fps_turn_job, fps_turn_dir, fps_turn_ts, fps_turn_multiplier_linear, fps_turn_stop
        fps_turn_stop = False
        fps_multiplier_reset()

        if fps_turn_job != None:
            if fps_turn_dir == 1:
                fps_multiplier_reset()
                return
            else:
                fps_turn_dir = 1
                fps_multiplier_reset()
                fps_turn_ts = time.perf_counter()

        if fps_turn_job is None:
            fps_turn_dir = 1
            fps_turn_ts = time.perf_counter()
            fps_turn_tick()
            fps_turn_job = cron.interval("16ms", fps_turn_tick)

    def fps_turn_right_stop():
        """Turn right stop"""
        _fps_turn_stop()

    def fps_turn_left_soft_continuous():
        """Turn left soft continuous"""
        actions.user.mouse_move_native_left()

    def fps_turn_right_soft_continuous():
        """Turn right soft continuous"""
        actions.user.mouse_move_native_right()

    def enable_fps_side_b_briefly():
        """Enable fps side b briefly"""
        tags = set(ctx.tags)
        tags.add("user.fps_side_b")
        ctx.tags = tags
        cron.after("1s", actions.user.disable_fps_side_b)
        actions.user.hud_add_log('command', '<*Note:/> Side b enabled')

    def disable_fps_side_b():
        """Disable fps side b briefly"""
        tags = set(ctx.tags)
        tags.discard("user.fps_side_b")
        ctx.tags = tags

    def enable_fps_side_c_briefly():
        """Enable fps side c briefly"""
        tags = set(ctx.tags)
        tags.add("user.fps_side_c")
        ctx.tags = tags
        cron.after("1s", actions.user.disable_fps_side_c)

    def disable_fps_side_c():
        """Disable fps side c briefly"""
        tags = set(ctx.tags)
        tags.discard("user.fps_side_c")
        ctx.tags = tags

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

    def toggle_world_or_room_tag(type: str = None):
        """Toggle world or room tag"""
        tags = set(ctx.tags)
        if type == 'world':
            tags.discard("user.fps_room")
            tags.add("user.fps_world")
            actions.user.hud_publish_content("pop=align\ncluck=shift\npalate=jump", "example", "World mode")
            actions.user.hud_add_log('warning', '<*Note:/> World Room Enabled')
        elif type == 'room':
            tags.discard("user.fps_world")
            tags.add("user.fps_room")
            actions.user.hud_publish_content("pop=align\ncluck=click\ntut=right click\npalate=look down", "example", "Room mode")
            actions.user.hud_add_log('event', '<*Note:/> FPS Room Enabled')
        elif "user.fps_world" in tags:
            tags.discard("user.fps_world")
            tags.add("user.fps_room")
            actions.user.hud_publish_content("pop=align\ncluck=click\ntut=right click\npalate=look down", "example", "Room mode")
            actions.user.hud_add_log('event', '<*Note:/> FPS Room Enabled')
        elif "user.fps_room" in tags:
            tags.discard("user.fps_room")
            tags.add("user.fps_world")
            actions.user.hud_publish_content("pop=align\ncluck=shift\npalate=jump", "example", "World mode")
            actions.user.hud_add_log('warning', '<*Note:/> World Room Enabled')
        else:
            tags.add("user.fps_world")
        ctx.tags = tags

    def disable_parrot_fps_compass():
        """Disable parrot fps compass"""
        tags = set(ctx.tags)
        tags.discard("user.parrot_fps_compass")
        ctx.tags = tags

    def enable_parrot_fps_walk_dir():
        """Enable parrot walk dir"""
        tags = set(ctx.tags)
        tags.add("user.parrot_fps_walk_dir")
        ctx.tags = tags

    def disable_parrot_fps_walk_dir():
        """Disable parrot walk dir"""
        tags = set(ctx.tags)
        tags.discard("user.parrot_fps_walk_dir")
        ctx.tags = tags

    def enable_parrot_fps_orbit_scan():
        """Enable parrot orbit scan"""
        tags = set(ctx.tags)
        tags.add("user.parrot_fps_orbit_scan")
        ctx.tags = tags
        actions.user.add_color_cursor("FFA500")
        actions.user.hud_add_log('command', '<*Note:/> Orbit mode set!')

    def disable_parrot_fps_orbit_scan():
        """Disable parrot orbit scan"""
        tags = set(ctx.tags)
        tags.discard("user.parrot_fps_orbit_scan")
        ctx.tags = tags
        actions.user.parrot_set_cursor_color()

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
        # actions.user.fps_stop_layer()

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

    def fps_direction_go_or_toggle():
        """Toggle direction"""
        actions.key("s:up")
        actions.key("w:down")


    def fps_direction_back_or_toggle():
        """Toggle back direction"""
        actions.key("w:up")
        actions.key("s:down")

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
        actions.user.hud_add_log('command', '<*Note:/> North anchor set!')

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

    def fps_compass_snap_to_closest_90():
        """Snap to closest 90 degree angle"""
        global compass_north_offset, compass_north_anchor
        x360 = settings.get("user.fps_calibrate_x_360")

        compass_north_offset_normalized = compass_north_offset % x360
        if compass_north_offset_normalized < 0:
            compass_north_offset_normalized += x360

        normalized_degree = (compass_north_offset_normalized / x360 * 360)
        nearest_90_degree = round(normalized_degree/90) * 90
        snap_rotation = nearest_90_degree / 360 * x360
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

    def fps_flick_mouse_down_toggle():
        """Toggle flick mouse down"""
        global y_offset
        if y_offset <= 100:
            actions.user.fps_flick_mouse_down()
        else:
            actions.user.fps_flick_mouse_center()

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