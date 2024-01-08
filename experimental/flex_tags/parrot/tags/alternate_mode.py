from talon import Module, Context, actions
from .create_flex_tag import create_flex_tag

mod = Module()
ctx = Context()
ctx_rpg_mouse = create_flex_tag("alternate_mode_rpg_mouse")

ctx.tags = ["user.flex_alternate_mode_rpg_mouse"]

@mod.action_class
class Actions:
    def flex_alternate_mode():
        """Flex alternate_mode"""
        pass

    def choose_flex_alternate_mode():
        """Choose flex alternate_mode"""
        pass

    def use_flex_alternate_mode_rpg_mouse():
        """Enable flex alternate_mode rpg_mouse"""
        ctx.tags = ["user.flex_alternate_mode_rpg_mouse"]

    def use_flex_alternate_mode_none():
        """Disable flex alternate_mode default"""
        ctx.tags = []


@ctx_rpg_mouse.action_class("user")
class Actions:
    def flex_alternate_mode():
        actions.user.parrot_rpg_mouse_mode_enable()
