from talon import Module

mod = Module()

mod.setting(
    "parrot_default_tag",
    desc="default tag for parrot",
    type=str,
    default="user.parrot_default"
)

mod.setting(
    "parrot_rpg_increment_x",
    desc="X increment for parrot mouse rpg mode",
    type=int,
    default=26
)

mod.setting(
    "parrot_rpg_increment_y",
    desc="Y increment for parrot mouse rpg mode",
    type=int,
    default=26
)

mod.setting(
    "parrot_rpg_interaction_axis_y_pos",
    desc="Y position of an interaction bar in the application",
    type=int,
    default=140
)

mod.setting(
    "roku_persist_frozen_mouse_on_exit", bool, default=True
)

mod.setting(
    "parrot_mode_mouse_freeze_on_click", bool, default=True
)