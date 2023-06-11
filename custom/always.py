from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def talon_sleep():
        """Stop listening for Talon commands."""
        actions.user.sleep_all()

    def talon_wake():
        """Start listening for Talon commands."""
        actions.user.wake_all()

    def talon_toggle():
        """Toggle Talon on or off."""
        actions.speech.toggle()

    def toggle_voice():
        """Toggle between Serenade and Talon."""
        actions.key("alt-z")
        actions.speech.toggle()