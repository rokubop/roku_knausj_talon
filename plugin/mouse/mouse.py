import os

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, settings, ui
from talon_plugins import eye_zoom_mouse

key = actions.key
self = actions.self
scroll_amount = 0
click_job = None
scroll_job = None
gaze_job = None
_stay_job = None
_stay_x = 0
_stay_y = 0
cancel_scroll_on_pop = True
control_mouse_forced = False
hiss_scroll_up = False

default_cursor = {
    "AppStarting": r"%SystemRoot%\Cursors\aero_working.ani",
    "Arrow": r"%SystemRoot%\Cursors\aero_arrow.cur",
    "Hand": r"%SystemRoot%\Cursors\aero_link.cur",
    "Help": r"%SystemRoot%\Cursors\aero_helpsel.cur",
    "No": r"%SystemRoot%\Cursors\aero_unavail.cur",
    "NWPen": r"%SystemRoot%\Cursors\aero_pen.cur",
    "Person": r"%SystemRoot%\Cursors\aero_person.cur",
    "Pin": r"%SystemRoot%\Cursors\aero_pin.cur",
    "SizeAll": r"%SystemRoot%\Cursors\aero_move.cur",
    "SizeNESW": r"%SystemRoot%\Cursors\aero_nesw.cur",
    "SizeNS": r"%SystemRoot%\Cursors\aero_ns.cur",
    "SizeNWSE": r"%SystemRoot%\Cursors\aero_nwse.cur",
    "SizeWE": r"%SystemRoot%\Cursors\aero_ew.cur",
    "UpArrow": r"%SystemRoot%\Cursors\aero_up.cur",
    "Wait": r"%SystemRoot%\Cursors\aero_busy.ani",
    "Crosshair": "",
    "IBeam": "",
}

# todo figure out why notepad++ still shows the cursor sometimes.
hidden_cursor = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), r"Resources\HiddenCursor.cur"
)

mod = Module()
ctx = Context()

mod.list("mouse_click", desc="Available mouse clicks")
ctx.lists["self.mouse_click"] = {
    "left": "left",
    "right": "right",
    "middle": "middle",
    "mid": "middle",
    "double": "double",
    "dub": "double",
    "triple": "triple",
    "trip": "triple",
    "control": "control",
    "ctrl": "control",
    "troll": "control",
    "shift": "shift",
    "center": "center",
}

mod.list(
    "mouse_button", desc="List of mouse button words to mouse_click index parameter"
)
mod.tag(
    "mouse_cursor_commands_enable", desc="Tag enables hide/show mouse cursor commands"
)
mod.setting(
    "mouse_enable_pop_click",
    type=int,
    default=0,
    desc="Pop noise clicks left mouse button. 0 = off, 1 = on with eyetracker but not with zoom mouse mode, 2 = on but not with zoom mouse mode",
)
mod.setting(
    "mouse_enable_pop_stops_scroll",
    type=bool,
    default=False,
    desc="When enabled, pop stops continuous scroll modes (wheel upper/downer/gaze)",
)
mod.setting(
    "mouse_enable_pop_stops_drag",
    type=bool,
    default=False,
    desc="When enabled, pop stops mouse drag",
)
mod.setting(
    "mouse_enable_hiss_scroll",
    type=bool,
    default=False,
    desc="Hiss noise scrolls down when enabled",
)
mod.setting(
    "mouse_wake_hides_cursor",
    type=bool,
    default=False,
    desc="When enabled, mouse wake will hide the cursor. mouse_wake enables zoom mouse.",
)
mod.setting(
    "mouse_hide_mouse_gui",
    type=bool,
    default=False,
    desc="When enabled, the 'Scroll Mouse' GUI will not be shown.",
)
mod.setting(
    "mouse_continuous_scroll_amount",
    type=int,
    default=80,
    desc="The default amount used when scrolling continuously",
)
mod.setting(
    "mouse_wheel_down_amount",
    type=int,
    default=120,
    desc="The amount to scroll up/down (equivalent to mouse wheel on Windows by default)",
)
mod.setting(
    "mouse_wheel_horizontal_amount",
    type=int,
    default=40,
    desc="The amount to scroll left/right",
)

continuous_scroll_mode = ""


@imgui.open(x=700, y=0)
def gui_wheel(gui: imgui.GUI):
    gui.text(f"Scroll mode: {continuous_scroll_mode}")
    gui.line()
    if gui.button("Wheel Stop [stop scrolling]"):
        actions.user.mouse_scroll_stop()


is_dragging = True

@mod.action_class
class RokuActions:
    def mouse_move_relative_window(x: int, y: int):
        """move the mouse cursor relative to the current window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (x * rect.width / 1920), rect.top + (y * rect.height / 1080))

    def mouse_move_relative_screen(screen: int, x: int, y: int):
        """move the mouse cursor relative to the current window"""
        rect = ui.screens()[screen - 1].rect

        # rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (x * rect.width / 1920), rect.top + (y * rect.height / 1080))

@mod.action_class
class Actions:
    def mouse_click(action: str = "left", button: int = 0):
        """Click mouse button - left, right, middle, ctrl-shift-left, double"""
        modifiers = action.split("-")

        if "shift" in modifiers:
            actions.key("shift:down")
        if "control" in modifiers or "ctrl" in modifiers:
            actions.key("ctrl:down")
        if "alt" in modifiers:
            actions.key("alt:down")
        if "win" in modifiers:
            actions.key("win:down")

        if "left" in modifiers:
            actions.mouse_click(0)
        elif "right" in modifiers:
            actions.mouse_click(1)
        elif "middle" in modifiers:
            actions.mouse_click(2)
        elif action == "double":
            actions.mouse_click(button)
            actions.mouse_click(button)
        elif action == "triple":
            actions.mouse_click(button)
            actions.mouse_click(button)
            actions.mouse_click(button)

        if "shift" in modifiers:
            actions.key("shift:up")
        if "control" in modifiers or "ctrl" in modifiers:
            actions.key("ctrl:up")
        if "alt" in modifiers:
            actions.key("alt:up")
        if "win" in modifiers:
            actions.key("win:up")

    def zoom_close():
        """Closes an in-progress zoom. Talon will move the cursor position but not click."""
        if eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_OVERLAY:
            actions.tracking.zoom_cancel()

    def mouse_show_cursor():
        """Shows the cursor"""
        show_cursor_helper(True)

    def mouse_hide_cursor():
        """Hides the cursor"""
        show_cursor_helper(False)

    def mouse_wake():
        """Enable control mouse, zoom mouse, and disables cursor"""
        actions.tracking.control_zoom_toggle(True)

        if settings.get("user.mouse_wake_hides_cursor"):
            show_cursor_helper(False)

    def mouse_drag_new(action: str):
        """Press and hold a specific mouse button for dragging"""
        if action == "left":
            actions.user.mouse_drag(0)
        elif action == "right":
            actions.user.mouse_drag(1)
        elif action == "middle":
            actions.user.mouse_drag(2)
        elif action == "double":
            actions.user.mouse_drag(0)
            actions.user.mouse_drag(0)
        elif action == "triple":
            actions.user.mouse_drag(0)
            actions.user.mouse_drag(0)
            actions.user.mouse_drag(0)
        elif action == "control" or action == "ctrl":
            actions.key("ctrl:down")
            actions.user.mouse_drag(0)
            actions.key("ctrl:up")
        elif action == "shift":
            actions.key("shift:down")
            actions.user.mouse_drag(0)
            actions.key("shift:up")
        elif action == "alt":
            actions.key("alt:down")
            actions.user.mouse_drag(0)
            actions.key("alt:up")

    def mouse_drag(button: int):
        """Press and hold/release a specific mouse button for dragging"""
        global is_dragging
        # Clear any existing drags
        actions.user.mouse_drag_end()

        # Start drag
        is_dragging = True
        ctrl.mouse_click(button=button, down=True)

    def mouse_drag_end():
        """Releases any held mouse buttons"""
        global is_dragging
        is_dragging = False
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)

    def mouse_is_dragging():
        """Check if the mouse is being held down"""
        global is_dragging
        return is_dragging

    def mouse_sleep():
        """Disables control mouse, zoom mouse, and re-enables cursor"""
        actions.tracking.control_zoom_toggle(False)
        actions.tracking.control_toggle(False)
        actions.tracking.control1_toggle(False)

        show_cursor_helper(True)
        stop_scroll()
        actions.user.mouse_drag_end()

    def mouse_scroll_down(amount: float = 1):
        """Scrolls down"""
        mouse_scroll(amount * settings.get("user.mouse_wheel_down_amount"))()

    def mouse_scroll_down_continuous():
        """Scrolls down continuously"""
        global continuous_scroll_mode
        continuous_scroll_mode = "scroll down continuous"
        mouse_scroll(settings.get("user.mouse_continuous_scroll_amount"))()

        if scroll_job is None:
            start_scroll()

        if not settings.get("user.mouse_hide_mouse_gui"):
            gui_wheel.show()

    def mouse_scroll_up(amount: float = 1):
        """Scrolls up"""
        mouse_scroll(-amount * settings.get("user.mouse_wheel_down_amount"))()

    def mouse_scroll_up_continuous():
        """Scrolls up continuously"""
        global continuous_scroll_mode
        continuous_scroll_mode = "scroll up continuous"
        mouse_scroll(-settings.get("user.mouse_continuous_scroll_amount"))()

        if scroll_job is None:
            start_scroll()
        if not settings.get("user.mouse_hide_mouse_gui"):
            gui_wheel.show()

    def mouse_scroll_left(amount: float = 1):
        """Scrolls left"""
        actions.mouse_scroll(
            0, -amount * settings.get("user.mouse_wheel_horizontal_amount")
        )

    def mouse_scroll_right(amount: float = 1):
        """Scrolls right"""
        actions.mouse_scroll(
            0, amount * settings.get("user.mouse_wheel_horizontal_amount")
        )

    def mouse_scroll_stop():
        """Stops scrolling"""
        stop_scroll()

    def mouse_gaze_scroll():
        """Starts gaze scroll"""
        global continuous_scroll_mode
        # this calls stop_scroll, which resets continuous_scroll_mode
        start_cursor_scrolling()

        continuous_scroll_mode = "gaze scroll"

        if not settings.get("user.mouse_hide_mouse_gui"):
            gui_wheel.show()

        # enable 'control mouse' if eye tracker is present and not enabled already
        global control_mouse_forced
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle(True)
            control_mouse_forced = True

    def copy_mouse_position():
        """Copy the current mouse position coordinates"""
        position = ctrl.mouse_pos()
        clip.set_text(repr(position))

    def mouse_move_center_active_window():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))

    def hiss_scroll_up():
        """Change mouse hiss scroll direction to up"""
        global hiss_scroll_up
        hiss_scroll_up = True

    def hiss_scroll_down():
        """Change mouse hiss scroll direction to down"""
        global hiss_scroll_up
        hiss_scroll_up = False

    def mouse_toggle_stay_in_place():
        """toggle stay in place"""
        global _stay_job
        if _stay_job:
            _stop_stay_job()
        else:
            _start_stay_job()

    def mouse_stay_in_place(is_stay: bool):
        """stay in place so that for example
        content that is not hoverable
        but activates on hover
        can be read without turning the eye tracker off only for a couple of seconds
        which in theory may damage it if done too frequently"""
        if is_stay:
            _start_stay_job()
        else:
            _stop_stay_job()

def show_cursor_helper(show):
    """Show/hide the cursor"""
    if app.platform == "windows":
        import ctypes
        import winreg

        import win32con

        try:
            Registrykey = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_WRITE
            )

            for value_name, value in default_cursor.items():
                if show:
                    winreg.SetValueEx(
                        Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, value
                    )
                else:
                    winreg.SetValueEx(
                        Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, hidden_cursor
                    )

            winreg.CloseKey(Registrykey)

            ctypes.windll.user32.SystemParametersInfoA(
                win32con.SPI_SETCURSORS, 0, None, 0
            )

        except OSError:
            print(f"Unable to show_cursor({str(show)})")
    else:
        ctrl.cursor_visible(show)

@ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        if (
            settings.get("user.mouse_enable_pop_stops_drag")
            and ctrl.mouse_buttons_down()
        ):
            actions.user.mouse_drag_end()
        elif settings.get("user.mouse_enable_pop_stops_scroll") and (
            gaze_job or scroll_job
        ):
            # Allow pop to stop scroll
            stop_scroll()
        else:
            # Otherwise respect the mouse_enable_pop_click setting
            setting_val = settings.get("user.mouse_enable_pop_click")

            is_using_eye_tracker = (
                actions.tracking.control_zoom_enabled()
                or actions.tracking.control_enabled()
                or actions.tracking.control1_enabled()
            )
            should_click = (
                setting_val == 2 and not actions.tracking.control_zoom_enabled()
            ) or (
                setting_val == 1
                and is_using_eye_tracker
                and not actions.tracking.control_zoom_enabled()
            )
            if should_click:
                ctrl.mouse_click(button=0, hold=16000)

@ctx.action("user.on_pop")
def on_pop():
    if actions.user.parrot_mode_is_disabled_permanent():
        return

    actions.user.mouse_scroll_stop()

    settings_mouse_enable_pop_click = settings.get("user.mouse_enable_pop_click")

    if settings_mouse_enable_pop_click >= 1 and (gaze_job or scroll_job):
        # Allow pop to stop scroll
        stop_scroll()
    elif actions.user.mouse_is_dragging():
        print("pop as drag end")
        actions.user.mouse_drag_end()
    else:
        # Otherwise respect the mouse_enable_pop_click setting
        setting_val = settings_mouse_enable_pop_click

        is_using_eye_tracker = (
            actions.tracking.control_zoom_enabled()
            or actions.tracking.control_enabled()
            or actions.tracking.control1_enabled()
        )
        should_click = (
            setting_val == 2 and not actions.tracking.control_zoom_enabled()
        ) or (
            setting_val == 1
            and is_using_eye_tracker
            and not actions.tracking.control_zoom_enabled()
        )
        if should_click:
            ctrl.mouse_click(button=0, hold=16000)

    def noise_trigger_hiss(active: bool):
        if settings.get("user.mouse_enable_hiss_scroll"):
            if active:
                if hiss_scroll_up:
                    actions.user.mouse_scroll_up_continuous()
                else:
                    actions.user.mouse_scroll_down_continuous()
            else:
                actions.user.mouse_scroll_stop()


def mouse_scroll(amount):
    def scroll():
        global scroll_amount
        if continuous_scroll_mode:
            if (scroll_amount >= 0) == (amount >= 0):
                scroll_amount += amount
            else:
                scroll_amount = amount
        actions.mouse_scroll(y=int(amount))

    return scroll


def scroll_continuous_helper():
    global scroll_amount
    # print("scroll_continuous_helper")
    if scroll_amount and (eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_IDLE):
        actions.mouse_scroll(by_lines=False, y=int(scroll_amount / 10))


def start_scroll():
    global scroll_job
    scroll_job = cron.interval("60ms", scroll_continuous_helper)


def gaze_scroll():
    # print("gaze_scroll")
    if (
        eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_IDLE
    ):  # or eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_SLEEP:
        x, y = ctrl.mouse_pos()

        # the rect for the window containing the mouse
        rect = None

        # on windows, check the active_window first since ui.windows() is not z-ordered
        if app.platform == "windows" and ui.active_window().rect.contains(x, y):
            rect = ui.active_window().rect
        else:
            windows = ui.windows()
            for w in windows:
                if w.rect.contains(x, y):
                    rect = w.rect
                    break

        if rect is None:
            # print("no window found!")
            return

        midpoint = rect.y + rect.height / 2
        amount = int(((y - midpoint) / (rect.height / 10)) ** 3)
        actions.mouse_scroll(by_lines=False, y=amount)

    # print(f"gaze_scroll: {midpoint} {rect.height} {amount}")


def stop_scroll():
    global scroll_amount, scroll_job, gaze_job, continuous_scroll_mode
    scroll_amount = 0
    if scroll_job:
        cron.cancel(scroll_job)

    if gaze_job:
        cron.cancel(gaze_job)

    global control_mouse_forced
    if control_mouse_forced:
        actions.tracking.control_toggle(False)
        control_mouse_forced = False

    scroll_job = None
    gaze_job = None
    gui_wheel.hide()

    continuous_scroll_mode = ""


def start_cursor_scrolling():
    global scroll_job, gaze_job
    stop_scroll()
    gaze_job = cron.interval("60ms", gaze_scroll)


def _mouse_stay():
    ctrl.mouse_move(_stay_x, _stay_y, dx=0, dy=0)


def _start_stay_job():
    global _stay_job, _stay_x, _stay_y
    if _stay_job:
        return
    _stay_x, _stay_y = ctrl.mouse_pos()
    _stay_job = cron.interval("1ms", _mouse_stay)


def _stop_stay_job():
    global _stay_job
    if not _stay_job:
        return
    cron.cancel(_stay_job)
    _stay_job = None