from talon import Module, actions, Context

mod = Module()
ctx = Context()
ctx.tags = ["user.pedal_scroll_up_down"]

recent_tags = ["user.pedal_scroll_up_down", "user.pedal_click_mute"]

@mod.action_class
class Actions:
    def pedal_on_tag_enable():
        """Triggered when a tag is enabled"""
        actions.skip()

    def pedal_on_tag_disable():
        """Triggered when a tag is disabled"""
        actions.skip()

    def pedal_left_down():
        """Left pedal"""
        actions.skip()

    def pedal_left_up():
        """Left pedal up"""
        actions.skip()

    def pedal_center_down():
        """Center pedal"""
        actions.skip()

    def pedal_center_up():
        """Center pedal up"""
        actions.skip()

    def pedal_right_down():
        """Right pedal"""
        actions.skip()

    def pedal_right_up():
        """Right pedal up"""
        actions.user.toggle_recent_mode()

    def toggle_recent_mode():
        """Toggle recent mode"""
        global recent_tags
        recent_tags[0], recent_tags[1] = recent_tags[1], recent_tags[0]
        actions.user.pedal_on_tag_disable()
        ctx.tags = [recent_tags[0]]
        actions.user.pedal_on_tag_enable()
