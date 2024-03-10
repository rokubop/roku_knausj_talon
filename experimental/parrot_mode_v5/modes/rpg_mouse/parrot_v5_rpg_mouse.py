from talon import Module, Context, actions, settings, ctrl

mod = Module()
mod.mode("parrot_v5_rpg_mouse", "rpg mouse parrot mode v5")

ctx = Context()
ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_rpg_mouse
"""

@ctx.action_class("user")
class Events:
    def on_parrot_v5_mode_enable(ev: dict):
        actions.user.parrot_v5_ui_cursor_yellow()

    def on_rpg_mouse_speed_change(speed: str):
        if speed == "slow":
            actions.user.parrot_v5_ui_cursor_yellow()
        elif speed == "medium":
            actions.user.parrot_v5_ui_cursor_custom_color("ccff33")
        elif speed == "fast":
            actions.user.parrot_v5_ui_cursor_custom_color("66ff33")

    def on_parrot_v5_mode_disable(ev: dict):
        actions.user.rpg_mouse_stop()
        actions.user.rpg_mouse_reset_speed()

        if not ev.get("transition", False):
            actions.user.parrot_v5_ui_clear()

    def on_event_mouse_button_down():
        actions.user.rpg_mouse_stop()
