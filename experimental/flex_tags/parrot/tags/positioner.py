from talon import Module, Context, actions
from .create_flex_tag import create_flex_tag

mod = Module()
ctx = Context()
ctx_default = create_flex_tag("positioner_default")

ctx.tags = ["user.flex_positioner_default"]

@mod.action_class
class Actions:
    def flex_position():
        """Flex positioner"""
        pass

    def choose_flex_positioner():
        """Choose flex positioner"""
        pass

    def use_flex_positioner_default():
        """Enable flex positioner default"""
        ctx.tags = ["user.flex_positioner_default"]

    def use_flex_positioner_none():
        """Disable flex positioner default"""
        ctx.tags = []


@ctx_default.action_class("user")
class Actions:
    def flex_position():
        actions.user.parrot_position_mode_enable()
