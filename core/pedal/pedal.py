from talon import Module, actions, Context, cron

mod = Module()
ctx = Context()
ctx.tags = ["user.pedal_scroll_up_down"]

recent_tags = []
open_menu = False
open_menu_cron = None

@mod.action_class
class Actions:
    def pedal_available_tags():
        """Returns a list of available tags for the given context, starting with the one that should be active first"""
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
        global open_menu_cron
        open_menu_cron = cron.after("1s", actions.user.pedal_open_menu)
        actions.skip()

    def pedal_right_up():
        """Right pedal up"""
        global open_menu, open_menu_cron
        if open_menu:
            if open_menu_cron:
                cron.cancel(open_menu_cron)
                open_menu_cron = None
                open_menu = False
        else:
            actions.user.toggle_last_tag()

    def pedal_open_menu():
        """Pedal open menu"""
        global open_menu, open_menu_cron
        # actions.user.canvas_test_one()
        cron.cancel(open_menu_cron)
        open_menu = True
        open_menu_cron = None

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

        new_tags = recent_tags[0] if recent_tags else []
        actions.user.pedal_set_tag(new_tags)

    def pedal_set_tag(user_tag: str):
        """Set the current pedal tag"""
        actions.user.pedal_on_tag_disable()
        ctx.tags = [user_tag]
        actions.user.pedal_on_tag_enable()
