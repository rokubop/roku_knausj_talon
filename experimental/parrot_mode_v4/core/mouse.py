from talon import Module, actions, cron, settings
import time

mod = Module()

gaze_job = None
scroll_job = None
scroll_speed_dynamic = 1
scroll_dir = 1
scroll_ts = None

mod.setting(
    "parrot_v4_scroll_speed",
    type=float,
    default=1,
    desc="Base scroll speed",
)
mod.setting(
    "parrot_v4_scroll_speed_multiplier",
    type=float,
    default=1,
    desc="Context specific scroll speed multiplier",
)

def scroll_continuous_helper():
    acceleration_speed = 1 + min((time.perf_counter() - scroll_ts) / 0.5, 4)
    print(settings.get("user.parrot_v4_scroll_speed"))
    print(settings.get("user.parrot_v4_scroll_speed_multiplier"))
    y = (
        settings.get("user.parrot_v4_scroll_speed")
        * settings.get("user.parrot_v4_scroll_speed_multiplier")
        * scroll_speed_dynamic
        * acceleration_speed
        * scroll_dir
    )
    actions.mouse_scroll(y, by_lines=True)

@mod.action_class
class Actions:
    def parrot_v4_mouse_scrolling(direction: str):
        """Toggle scrolling continuously"""
        global scroll_job, scroll_dir, scroll_ts
        new_scroll_dir = -1 if direction == "up" else 1

        if scroll_job != None:
            # Issuing a scroll in the same direction as existing aborts it
            if scroll_dir == new_scroll_dir:
                actions.user.mouse_scroll_stop()
                return
            # Issuing a scroll in the reverse direction resets acceleration
            else:
                scroll_dir = new_scroll_dir
                scroll_ts = time.perf_counter()

        if scroll_job is None:
            scroll_dir = new_scroll_dir
            scroll_ts = time.perf_counter()
            scroll_continuous_helper()
            scroll_job = cron.interval("16ms", scroll_continuous_helper)

    def parrot_v4_mouse_scroll_stop():
        """Stop mouse scroll"""
        global scroll_job, gaze_job
        return_value = scroll_job or gaze_job
        if scroll_job:
            cron.cancel(scroll_job)
            scroll_job = None
        if gaze_job:
            cron.cancel(gaze_job)
            gaze_job = None
        return return_value