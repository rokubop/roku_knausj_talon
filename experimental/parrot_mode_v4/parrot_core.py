from talon import Context, Module, actions, ctrl, settings

mod = Module()
ctx = Context()
mod.mode("parrot_v4_global", "Global parrot mode")
mod.mode("parrot_v4_app", "App parrot mode")
mod.setting("parrot_v4_prefer_app_or_global", type=str, default="global", desc="Prefer global or app mode")
mod.setting("parrot_v4_show_cursor_color", type=bool, default=False, desc="Show cursor or not")
mod.setting("parrot_v4_cursor_color", type=str, desc="Cursor color")

def no_op():
    pass

@mod.action_class
class Actions:
    def parrot_v4_mode_enable():
        """Enable parrot mode - global or app mode"""
        print("enabling v4 parrot mode")
        actions.user.clear_screen_regions()
        actions.mode.save()
        actions.mode.disable("command")
        actions.mode.disable("dictation")
        mode = settings.get("user.parrot_v4_prefer_app_or_global")
        if mode == "app":
            actions.mode.enable("user.parrot_v4_app")
        else:
            actions.mode.enable("user.parrot_v4_global")
        actions.user.parrot_v4_update_ui()

    def parrot_v4_mode_disable():
        """Disable parrot mode"""
        print("disabling v4 parrot mode")
        actions.user.parrot_v4_on_stopper()
        actions.user.clear_screen_regions()
        actions.mode.restore()

    def parrot_v4_update_ui():
        """Update UI"""
        show_cursor_color = settings.get("user.parrot_v4_show_cursor_color") or False
        if show_cursor_color:
            cursor_color = settings.get("user.parrot_v4_cursor_color")
            actions.user.add_color_cursor(cursor_color)

    def parrot_v4_mouse_click(button: int = 0, hold: int = 16000):
        """Mouse click"""
        actions.user.parrot_v4_on_before_mouse_click()
        ctrl.mouse_click(button=button, hold=hold)
        actions.user.parrot_v4_on_after_mouse_click()

    def parrot_v4_on_before_mouse_click():
        """Event fired before a mouse click"""
        no_op()

    def parrot_v4_on_after_mouse_click():
        """Event fired after a mouse click"""
        no_op()

    def parrot_v4_on_before_mouse_scroll():
        """Event fired before a mouse scroll"""
        no_op()

    def parrot_v4_on_after_mouse_scroll():
        """Event fired after a mouse scroll"""
        no_op()

    def parrot_v4_on_stopper():
        """Event fired on stopper"""
        print("module stopper")
        no_op()