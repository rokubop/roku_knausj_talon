from talon import Context, Module, actions, app, ui

mod = Module()
ctx = Context()

ctx.matches = """
os: windows
"""

def wait_for_fluent_search_window():
    for attempt in range(10):
        if ui.active_app().name == "FluentSearch":
            return True
        actions.sleep("50ms")

    app.notify("Gave up while waiting for Fluent Search")
    return False

@mod.action_class
class Action:
    def fluent_search_show_labels_window():
        """Shows Fluent Search’s Labels Window"""
        actions.key("alt-;")

    def fluent_search_show_labels_screen():
        """Shows Fluent Search’s Labels on the whole screen"""
        actions.key("ctrl-alt-;")

    def fluent_search(text: str):
        """Searches using Fluent Search"""

    def fluent_search_in_app(text: str, submit: bool):
        """Searches using Fluent Search’s In-app Search"""

@ctx.action_class("user")
class UserActions:
    def fluent_search(text: str):
        # XXX can't use app.focus() and unaware of any other way to
        # automate the way we do with LaunchBar
        # If you have a different search keyboard shortcut configured,
        # replace ctrl-alt-space with it below.
        actions.key("ctrl-alt-space")
        actions.sleep("50ms")
        actions.key("backspace")
        wait_for_fluent_search_window()
        if "\t" in text:
            plugin, text = text.split("\t", 1)
            actions.insert(plugin + "\t")
        actions.user.paste(text)

    def fluent_search_in_app(text: str, submit: bool):
        actions.key("alt-shift-/")
        wait_for_fluent_search_window()
        actions.user.paste(text)
        if submit:
            actions.key("enter")