from talon import Module

mod = Module()

mod.setting(
    name="event_mouse_scroll_speed",
    type=float,
    default=1,
    desc="Setting for event mouse scroll speed")

mod.setting(
    name="event_mouse_refresh_interval_ms",
    type=int,
    default=16,
    desc="Setting for how fast it refreshes movement in milliseconds")
