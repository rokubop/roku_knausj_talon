from talon import Module, Context, actions, ctrl
from .create_flex_tag import create_flex_tag

mod, ctx = Module(), Context()
ctx_flex_special = create_flex_tag("special_click_exit")

@mod.action_class
class Actions:
    def flex_special(): """Flex special"""; pass

    def use_flex_special_default():
        """Enable flex scroller default"""
        ctx.tags = ["user.flex_special_click_exit"]

@ctx_flex_special.action_class("user")
class ClickExit:
    def flex_special():
        ctrl.mouse_click(0)
        actions.user.mode_disable_parrot_v2()