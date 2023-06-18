from talon import Module

mod = Module()
mod.tag(
    "game_arrow_keys_toggle_wsad_movement",
    """If holding foot pedals or arrow keys down for a long time poses an issue,
then this tag allows the user to toggle movement (auto walk) and switch movement direction
by just pressing them once without having to hold them continuously.
See the comment on actions.user.game_movement_toggle_direction_switch(direction_key) for more details."""
)
