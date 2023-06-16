from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def serenade_toggle(self):
        """Toggle Serenade on or off."""
        actions.key("alt-z")
        self.talon_toggle()

    def serenade_wake():
        """Serenade on."""
        actions.key("alt-z")
        actions.user.talon_sleep()

    def serenade_sleep():
        """Serenade off."""
        actions.key("alt-z")

    def talon_sleep():
        """Stop listening for Talon commands."""
        actions.user.sleep_all()

    def talon_wake():
        """Start listening for Talon commands."""
        actions.user.wake_all()

    def talon_toggle():
        """Toggle Talon on or off."""
        if actions.speech.enabled():
            actions.user.talon_sleep()
        else:
            actions.user.talon_wake()

    def toggle_voice():
        """Toggle between Serenade and Talon."""
        actions.key("alt-z")
        actions.speech.toggle()