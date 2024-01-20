from talon import Context, Module, actions, ctrl, settings
from .utils.Debouncer import ContinuousHoldDebouncer

mod = Module()
ctx = Context()

scroll_down_action = ContinuousHoldDebouncer(
    150,
    lambda: actions.user.parrot_v4_mouse_scrolling("down"),
    actions.user.parrot_v4_mouse_scroll_stop)

scroll_up_action = ContinuousHoldDebouncer(
    150,
    lambda: actions.user.parrot_v4_mouse_scrolling("up"),
    actions.user.parrot_v4_mouse_scroll_stop)

@mod.action_class
class Tags:
    def parrot_v4_global_tag_enable(tag: str):
        """Enable global tag"""
        tags = set(ctx.tags)
        tags.add(tag)
        ctx.tags = list(tags)
        actions.user.parrot_v4_update_ui()

    def parrot_v4_global_tag_disable(tag: str):
        """Disable global tag"""
        tags = set(ctx.tags)
        tags.remove(tag)
        ctx.tags = list(tags)
        actions.user.parrot_v4_update_ui()

@mod.action_class
class Actions:
    def parrot_v4_click_primary():
        """Primary click"""
        actions.user.parrot_v4_mouse_click(0)

    def parrot_v4_click_alternate():
        """Alternate click"""
        actions.user.parrot_v4_mouse_click(1)

    def parrot_v4_drag_primary():
        """Primary drag"""
        actions.user.parrot_v4_global_tag_drag_enable()

    def parrot_v4_repeater():
        """Repeater"""
        actions.core.repeat_phrase()

    def parrot_v4_stopper():
        """Primary stopper"""
        print("calling parrot stopper")
        actions.user.parrot_v4_on_stopper()

    def parrot_v4_positioner():
        """Primary stopper"""
        actions.user.parrot_v4_global_tag_positioner_enable()

    def parrot_v4_mode_b_enable():
        """Mode B"""
        print("Enable mode B")

    def parrot_v4_set_modifier(modifier: str):
        """Set modifier"""
        print(f"Setting modifier: {modifier}")

    def parrot_v4_activate_side_b_briefly():
        """Side B"""
        print("Enable side B")

    def parrot_v4_activate_side_c_briefly():
        """Side C"""
        print("Enable side C")

    def parrot_v4_activate_side_d_briefly():
        """Side D"""
        print("Enable side D")

    def parrot_v4_scroller_down():
        """Scroller down"""
        actions.user.parrot_v4_on_before_mouse_scroll()
        scroll_down_action.start()
        print("scroll down")

    def parrot_v4_scroller_up():
        """Scroller up"""
        actions.user.parrot_v4_on_before_mouse_scroll()
        scroll_up_action.start()
        print("scroll up")

    def parrot_v4_scroller_stop():
        """Scroller stop"""
        print("scroll stop")
        scroll_down_action.stop()
        scroll_up_action.stop()
