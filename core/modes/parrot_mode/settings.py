from talon import Module

mod = Module()

mod.setting(
    "parrot_default_tag",
    desc="default tag for parrot",
    type=str,
    default="user.parrot_default"
)

mod.setting(
    "roku_persist_frozen_mouse_on_exit", bool, default=True
)

mod.setting(
    "parrot_mode_mouse_freeze_on_click", bool, default=True
)