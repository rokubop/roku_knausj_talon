"""
Hold down the pedal to scroll in the current direction.
Double tap the pedal to change the direction.

Actions:
user.pedal_scroll_up_or_down_dbl_tap()
user.pedal_scroll_up_or_down_dbl_tap_stop()
"""
from talon import Module, actions, cron

mod = Module()

double_tap_timeout_setting = "500ms"

double_tap_timer = None
double_tap_enabled = False
scroll_dir = "down"

def start_double_tap_timer():
    global double_tap_timer, double_tap_enabled
    clear_double_tap_timer()
    double_tap_enabled = True
    double_tap_timer = cron.after(double_tap_timeout_setting, clear_double_tap_timer)

def clear_double_tap_timer():
    global double_tap_enabled, double_tap_timer
    double_tap_enabled = False
    if double_tap_timer:
        cron.cancel(double_tap_timer)
        double_tap_timer = None

@mod.action_class
class Actions:
    def pedal_scroll_up_or_down_dbl_tap():
        """
        Hold down the pedal to scroll in the current direction.
        Double tap the pedal to change the direction.
        """
        global scroll_dir, double_tap_enabled

        if double_tap_enabled:
            scroll_dir = "down" if scroll_dir == "up" else "up"

        actions.user.mouse_scrolling(scroll_dir)
        start_double_tap_timer()

    def pedal_scroll_up_or_down_dbl_tap_stop():
        """Stop scrolling"""
        actions.user.mouse_scroll_stop()
