from talon import Module, Context, actions
from .create_flex_tag import create_flex_tag

mod = Module()
ctx = Context()
ctx_default = create_flex_tag("repeater_default")

ctx.tags = ["user.flex_repeater_default"]

@mod.action_class
class Actions:
    def flex_repeater():
        """Flex repeater"""
        pass

    def choose_flex_repeater():
        """Choose flex repeater"""
        pass

    def use_flex_repeater_default():
        """Enable flex repeater default"""
        ctx.tags = ["user.flex_repeater_default"]

    def use_flex_repeater_none():
        """Disable flex repeater default"""
        ctx.tags = []


@ctx_default.action_class("user")
class Actions:
    def flex_repeater():
        actions.user.repeat()
