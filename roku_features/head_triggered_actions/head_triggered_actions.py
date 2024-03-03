
from talon import Module, actions, ui, ctrl, cron, settings
from talon.canvas import Canvas
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.types import Rect

mod = Module()

mod.setting(
    name="head_triggered_actions_x_threshold",
    type=int,
    default=100,
    desc="The threshold for head triggered actions in x direction",
)
mod.setting(
    name="head_triggered_actions_y_threshold",
    type=int,
    default=50,
    desc="The threshold for head triggered actions in y direction",
)
mod.setting(
    name="head_triggered_actions_show_ui",
    type=bool,
    default=True,
    desc="Show the head triggered actions UI",
)

update_interval = '20ms'
mouse_did_jump_threshold = 30

anchor_center_xy = None
last_position_name = None
last_xy = None
monitor_mouse_job = None
canvas = None

def get_current_position_name():
    """Determine the current position based on the mouse's relation to the anchor_center_xy."""
    (x, y) = ctrl.mouse_pos()
    threshold_x = settings.get("user.head_triggered_actions_x_threshold")
    threshold_y = settings.get("user.head_triggered_actions_y_threshold")
    if abs(anchor_center_xy[0] - x) > threshold_x:
        return "left" if x < anchor_center_xy[0] else "right"
    if abs(anchor_center_xy[1] - y) > threshold_y:
        return "up" if y < anchor_center_xy[1] else "down"
    return "center"

def trigger_actions(last_position_name, current_position_name):
    """Trigger the appropriate actions based on position changes."""
    leave_actions = {
        "left": actions.user.on_head_left_leave,
        "right": actions.user.on_head_right_leave,
        "up": actions.user.on_head_up_leave,
        "down": actions.user.on_head_down_leave,
        "center": actions.user.on_head_center_leave
    }
    trigger_actions = {
        "left": actions.user.on_head_left_trigger,
        "right": actions.user.on_head_right_trigger,
        "up": actions.user.on_head_up_trigger,
        "down": actions.user.on_head_down_trigger,
        "center": actions.user.on_head_center_trigger
    }

    if last_position_name != current_position_name:
        if last_position_name:
            leave_actions.get(last_position_name)()

        trigger_actions.get(current_position_name)()

def paint_active_position(c: SkiaCanvas):
    global anchor_center_xy
    if anchor_center_xy:
        (x, y) = ctrl.mouse_pos()
        current_position_name = get_current_position_name()
        threshold_x = settings.get("user.head_triggered_actions_x_threshold")
        threshold_y = settings.get("user.head_triggered_actions_y_threshold")
        c.paint.color = "ff0000"
        (anchor_x, anchor_y) = anchor_center_xy
        top_left = (anchor_x - threshold_x, anchor_y - threshold_y)
        bottom_left = (anchor_x - threshold_x, anchor_y + threshold_y)
        top_right = (anchor_x + threshold_x, anchor_y - threshold_y)
        bottom_right = (anchor_x + threshold_x, anchor_y + threshold_y)
        if current_position_name == "left":
            c.draw_line(top_left[0], top_left[1], bottom_left[0], bottom_left[1])
        elif current_position_name == "right":
            c.draw_line(top_right[0], top_right[1], bottom_right[0], bottom_right[1])
        elif current_position_name == "up":
            c.draw_line(top_left[0], top_left[1], top_right[0], top_right[1])
        elif current_position_name == "down":
            c.draw_line(bottom_left[0], bottom_left[1], bottom_right[0], bottom_right[1])

def check_did_mouse_jump():
    global last_xy, mouse_did_jump_threshold
    did_jump = False
    (x, y) = ctrl.mouse_pos()
    if last_xy is not None and (abs(x - last_xy[0]) > mouse_did_jump_threshold or abs(y - last_xy[1]) > mouse_did_jump_threshold):
        did_jump = True
    return did_jump

def trigger_update():
    global anchor_center_xy, last_position_name, canvas, last_xy
    current_position_name = get_current_position_name()
    trigger_actions(last_position_name, current_position_name)
    last_position_name = current_position_name
    last_xy = ctrl.mouse_pos()
    if canvas is not None:
        canvas.freeze()

def recalibrate_anchor_jumped():
    global anchor_center_xy, last_xy
    (x, y) = ctrl.mouse_pos()

    current_offset = (anchor_center_xy[0] - last_xy[0], anchor_center_xy[1] - last_xy[1])
    new_anchor = (x + current_offset[0], y + current_offset[1])
    anchor_center_xy = new_anchor
    last_xy = None
    if canvas is not None:
        canvas.freeze()

def monitor_mouse_tick():
    global anchor_center_xy
    if anchor_center_xy:
        if check_did_mouse_jump():
            recalibrate_anchor_jumped()
        else:
            trigger_update()

def on_draw(c: SkiaCanvas):
    global anchor_center_xy, last_position_name
    if anchor_center_xy:
        threshold_x = settings.get("user.head_triggered_actions_x_threshold")
        threshold_y = settings.get("user.head_triggered_actions_y_threshold")
        c.paint.color = "ffffff"
        c.paint.style = c.paint.Style.STROKE
        left = anchor_center_xy[0] - threshold_x
        top = anchor_center_xy[1] - threshold_y
        width = threshold_x * 2
        height = threshold_y * 2
        c.draw_rect(Rect(left, top, width, height))
        paint_active_position(c)

def set_anchor_and_poll():
    global anchor_center_xy, monitor_mouse_job, update_interval
    anchor_center_xy = ctrl.mouse_pos()
    if monitor_mouse_job == None:
        monitor_mouse_job = cron.interval(update_interval, monitor_mouse_tick)

@mod.action_class
class Actions:
    def head_triggered_actions_show_ui():
        """Show head triggered actions thresholds and box"""
        global canvas
        if canvas is None:
            screen = ui.main_screen()
            canvas = Canvas.from_screen(screen)
            canvas.register("draw", on_draw)
            canvas.freeze()

    def head_triggered_actions_hide_ui():
        """Hide head triggered actions thresholds and box"""
        global canvas
        if canvas:
            canvas.unregister("draw", on_draw)
            canvas.hide()
            canvas.close()
            canvas = None

    def head_triggered_actions_start():
        """Start monitoring head triggered actions"""
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle(True)

        actions.tracking.control_head_toggle(True)
        actions.tracking.control_gaze_toggle(False)
        if settings.get("user.head_triggered_actions_show_ui"):
            actions.user.head_triggered_actions_show_ui()
        set_anchor_and_poll()

    def head_triggered_actions_stop():
        """Stop monitoring head triggered actions"""
        global anchor_center_xy, last_position_name, monitor_mouse_job, last_xy
        if monitor_mouse_job:
            cron.cancel(monitor_mouse_job)
            monitor_mouse_job = None
        anchor_center_xy = None
        last_position_name = None
        last_xy = None
        actions.user.head_triggered_actions_hide_ui()
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(False)

    def head_triggered_actions_reset():
        """Reset anchor for head triggered actions"""
        actions.user.head_triggered_actions_stop()
        actions.user.head_triggered_actions_start()

    # Events for the user to override with ctx
    def on_head_left_trigger():
        """Action fired on head triggered left"""
        print("on_head_left_trigger")

    def on_head_right_trigger():
        """Action fired on head triggered right"""
        print("on_head_right_trigger")

    def on_head_up_trigger():
        """Action fired on head triggered up"""
        print("on_head_up_trigger")

    def on_head_down_trigger():
        """Action fired on head triggered down"""
        print("on_head_down_trigger")

    def on_head_center_trigger():
        """Action fired on head triggered center"""
        print("on_head_center_trigger")

    def on_head_left_leave():
        """Action fired on head triggered left"""
        print("on_head_left_leave")

    def on_head_right_leave():
        """Action fired on head triggered right"""
        print("on_head_right_leave")

    def on_head_up_leave():
        """Action fired on head triggered up"""
        print("on_head_up_leave")

    def on_head_down_leave():
        """Action fired on head triggered down"""
        print("on_head_down_leave")

    def on_head_center_leave():
        """Action fired on head triggered center"""
        print("on_head_center_leave")