from talon import actions, Module

mod = Module()
mod.tag("game_quick_access_menu")

is_quick_access_menu_shown: bool = False


@mod.action_class
class Actions:

    def game_quick_access_menu_toggle(is_show: bool = None):
        """Toggles the quick access menu on/off depending on whether or not it is shown.

        This method does not contain any logic but it defaults to
        calling actions.user.game_quick_access_menu_show()
        and actions.user.game_quick_access_menu_hide().

        It tracks the state of the quick access menu (displayed/not displayed)
        independently of actions.user.game_quick_access_menu_show()
        and actions.user.game_quick_access_menu_hide()
        in case their override is needed."""
        global is_quick_access_menu_shown
        if is_show is None:
            is_show = not is_quick_access_menu_shown

        if is_show:
            actions.user.game_quick_access_menu_show()
        else:
            actions.user.game_quick_access_menu_hide()

        is_quick_access_menu_shown = is_show  # just in case an override of menu show/hide is needed

    def game_quick_access_menu_show():
        """Toggles the quick access menu on. Defaults to pressing down the tab key.
        Tracks the state of the quick access menu (displayed/not displayed)."""
        global is_quick_access_menu_shown
        actions.key("tab:down")
        is_quick_access_menu_shown = True

    def game_quick_access_menu_hide():
        """Toggles the quick access menu off. Defaults to releasing the tab key.
        Tracks the state of the quick access menu (displayed/not displayed)."""
        global is_quick_access_menu_shown
        actions.key("tab:up")
        is_quick_access_menu_shown = False
