from talon import actions, Module, Context, cron

mod = Module()
mod.tag("pedal_scroll_up_down", desc="pedal scrolling up or down")
ctx = Context()
ctx.matches = "tag: user.pedal_scroll_up_down"

pause_eye_tracking_job = None

@mod.action_class
class Actions:
    def pause_eye_tracking(time: str = "1500ms"):
        """Pauses eye tracking"""
        global pause_eye_tracking_job
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(False)
        if pause_eye_tracking_job:
            cron.cancel(pause_eye_tracking_job)
        pause_eye_tracking_job = cron.after(time, actions.user.parrot_use_default_tracking)

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('warning', '<*Pedal: Scrolling />')

    def pedal_left_down():
        actions.user.pause_eye_tracking()
        actions.user.mouse_scrolling("up")

    def pedal_left_up():
        actions.user.mouse_scroll_stop()

    def pedal_center_down():
        actions.user.pause_eye_tracking()
        actions.user.mouse_scrolling("down")

    def pedal_center_up():
        actions.user.mouse_scroll_stop()
