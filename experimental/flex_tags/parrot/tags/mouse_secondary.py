from talon import Module, Context, actions, ctrl
from .create_flex_tag import create_flex_tag

mod, ctx = Module(), Context()
ctx_right_click = create_flex_tag("mouse_secondary_right_click")

@mod.action_class
class Actions:
    def flex_mouse_secondary():
        """Right click, middle click, right drag, middle drag"""
        pass

    def use_flex_mouse_secondary_default():
        """Enable flex mouse_secondary default"""
        ctx.tags = [f"user.flex_mouse_secondary_right_click"]

@ctx_right_click.action_class("user")
class RightClick:
    def flex_mouse_secondary():
        ctrl.mouse_click(1)