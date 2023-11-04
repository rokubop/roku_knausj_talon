from talon import Module, Context, actions, ctrl, cron, settings
import win32api, win32con

mod = Module()
ctx = Context()

mod.tag(
    "fps_camera",
    desc="FPS camera commands",
)
mod.setting("fps_camera_interval_x", type=int, default=500)
mod.setting("fps_camera_interval_y", type=int, default=300)
mod.list("fps_direction", desc="FPS camera direction")

ctx.lists["self.fps_direction"] = [
    "left",
    "right",
    "up",
    "down",
]

nav_job = None
direction = (0, 1)

# def nav_tick():
#     global direction
#     if direction:
#         x, y = ctrl.mouse_pos()
#         dx, dy = direction
#         ctrl.mouse_move(x + dx * speed, y + dy * speed)
speed = 5

def nav_tick():
    global direction, speed
    if direction:
        dx, dy = direction
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx * speed), int(dy * speed))

def start_moving(dx, dy):
    global nav_job, direction
    if nav_job:
        cron.cancel(nav_job)
    direction = (dx, dy)
    nav_job = cron.interval("16ms", nav_tick)

@mod.action_class
class FpsCameraActions:
    def fps_scan(direction: str):
        """Start moving mouse in the given direction"""
        if direction == "left":
            actions.user.fps_scan_left()
        elif direction == "right":
            actions.user.fps_scan_right()
        elif direction == "up":
            actions.user.fps_scan_up()
        elif direction == "down":
            actions.user.fps_scan_down()

    def fps_scan_left():
        """Start moving mouse to the left"""
        start_moving(-1, 0)

    def fps_scan_right():
        """Start moving mouse to the right"""
        start_moving(1, 0)

    def fps_scan_down():
        """Start moving mouse down"""
        start_moving(0, 1)

    def fps_scan_up():
        """Start moving mouse up"""
        start_moving(0, -1)

    def fps_nudge(direction: str):
        """Move mouse in the given direction"""
        if direction == "left":
            actions.user.fps_nudge_left()
        elif direction == "right":
            actions.user.fps_nudge_right()
        elif direction == "up":
            actions.user.fps_nudge_up()
        elif direction == "down":
            actions.user.fps_nudge_down()

    def fps_soft(direction: str):
        """Move mouse in the given direction"""
        if direction == "left":
            actions.user.fps_soft_left()
        elif direction == "right":
            actions.user.fps_soft_right()
        elif direction == "up":
            actions.user.fps_soft_up()
        elif direction == "down":
            actions.user.fps_soft_down()

    # def fps_camera_repeat_reverse_dir_by_increment():
    #     """Repeat previous direction by the increment defined by the settings"""
    #     x, y = ctrl.mouse_pos()
    #     increment_x = settings.get("user.parrot_fps_increment_x")
    #     increment_y = settings.get("user.parrot_fps_increment_y")
    #     dx = direction[0] * increment_x * -1
    #     dy = direction[1] * increment_y * -1

    #     if direction:
    #         ctrl.mouse_move(x + dx, y + dy)

    def fps_stop():
        """Stop moving mouse"""
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)

    def fps_camera_mode_enable():
        """Enable parrot mouse nav mode"""
        actions.user.fps_stop()

    def fps_camera_mode_disable_full():
        """Disable parrot mouse nav mode and exit parrot mode"""
        actions.user.fps_stop()

    def fps_camera_mode_disable():
        """Disable parrot mouse nav mode"""
        actions.user.fps_stop()

    def fps_nudge_left():
        """Move mouse left"""
        actions.user.fps_scan_left()
        actions.sleep("300ms")
        actions.user.fps_stop()

    def fps_nudge_right():
        """Move mouse right"""
        actions.user.fps_scan_right()
        actions.sleep("300ms")
        actions.user.fps_stop()

    def fps_nudge_down():
        """Move mouse down"""
        actions.user.fps_scan_down()
        actions.sleep("300ms")
        actions.user.fps_stop()

    def fps_nudge_up():
        """Move mouse up"""
        actions.user.fps_scan_up()
        actions.sleep("300ms")
        actions.user.fps_stop()

    def fps_soft_left():
        """Move mouse left"""
        actions.user.fps_scan_left()
        actions.sleep("500ms")
        actions.user.fps_stop()

    def fps_soft_down():
        """Move mouse down"""
        actions.user.fps_scan_down()
        actions.sleep("500ms")
        actions.user.fps_stop()

    def fps_soft_right():
        """Move mouse right"""
        actions.user.fps_scan_right()
        actions.sleep("500ms")
        actions.user.fps_stop()

    def fps_soft_up():
        """Move mouse up"""
        actions.user.fps_scan_up()
        actions.sleep("500ms")
        actions.user.fps_stop()
