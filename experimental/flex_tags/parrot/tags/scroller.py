from talon import Module, Context, actions
from ...core.debouncer import Debouncer
from .create_flex_tag import create_flex_tag

mod, ctx = Module(), Context()
ctx_flex_scroller_default = create_flex_tag("scroller_default")

shush_debouncer = Debouncer(150, actions.user.parrot_scroll_up_start, actions.user.parrot_scroll_up_stop)
hiss_debouncer = Debouncer(150, actions.user.parrot_scroll_down_start, actions.user.parrot_scroll_down_stop)

@mod.action_class
class Actions:
    def flex_scroll_down(): """Flex scroll down"""; pass
    def flex_scroll_down_stop(): """Flex scroll down stop"""; pass
    def flex_scroll_up(): """Flex scroll up"""; pass
    def flex_scroll_up_stop(): """Flex scroll up stop"""; pass

    def use_flex_scroller_default():
        """Enable flex scroller default"""
        ctx.tags = ["user.flex_scroller_default"]

@ctx_flex_scroller_default.action_class("user")
class ScrollerDefaultActions:
    def flex_scroll_down():
        hiss_debouncer.start()

    def flex_scroll_down_stop():
        shush_debouncer.stop()
        hiss_debouncer.stop()

    def flex_scroll_up():
        shush_debouncer.start()

    def flex_scroll_up_stop():
        shush_debouncer.stop()
        hiss_debouncer.stop()