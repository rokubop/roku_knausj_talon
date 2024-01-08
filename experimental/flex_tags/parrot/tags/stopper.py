from talon import Module, Context, actions
from .create_flex_tag import create_flex_tag

mod = Module()
ctx = Context()
ctx_default = create_flex_tag("stopper_default")

ctx.tags = ["user.flex_stopper_default"]

@mod.action_class
class Actions:
    def flex_stop():
        """Flex stopper"""
        pass

    def choose_flex_stopper():
        """Choose flex stopper"""
        pass

    def use_flex_stopper_default():
        """Enable flex stopper default"""
        ctx.tags = ["user.flex_stopper_default"]

    def use_flex_stopper_none():
        """Disable flex stopper default"""
        ctx.tags = []


@ctx_default.action_class("user")
class Actions:
    def flex_stop():
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(False)
