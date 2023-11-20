from talon import Module, actions, Context

mod = Module()
ctx = Context()
ctx.tags = ["user.pedal_scroll_up_down"]

recent_tags = []

@mod.action_class
class Actions:
    def pedal_available_tags():
        """
        Returns a list of available tags for the given context,
        starting with the one that should be active first
        """
        return ["user.pedal_scroll_up_down", "user.pedal_click_mute"]

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
        actions.user.toggle_last_tag()

    def toggle_last_tag():
        """Toggle last tag for the current context"""
        global recent_tags
        available_tags = actions.user.pedal_available_tags()

        print("available_tags", available_tags)
        print("recent_tags", recent_tags)

        if set(recent_tags) != set(available_tags):
            # tags different = new context setting
            # initialize recent_tags
            print('setting tags')
            recent_tags = available_tags
        elif len(recent_tags) > 1:
            # swap tags if we have more than one
            recent_tags[0], recent_tags[1] = recent_tags[1], recent_tags[0]

        actions.user.pedal_on_tag_disable()
        if recent_tags:
            ctx.tags = [recent_tags[0]]
        else:
            ctx.tags = []
        actions.user.pedal_on_tag_enable()
