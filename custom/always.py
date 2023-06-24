from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def serenade_wake():
        """Serenade on."""
        actions.key("alt-z")
        actions.user.talon_sleep()

    def serenade_sleep():
        """Serenade off."""
        actions.key("alt-z")

    def talon_sleep():
        """Stop listening for Talon commands."""
        actions.speech.disable()

    def talon_wake():
        """Start listening for Talon commands."""
        actions.speech.enable()

    def talon_toggle():
        """Toggle Talon on or off."""
        if actions.speech.enabled():
            actions.user.talon_sleep()
            actions.sound.set_microphone("None")
        else:
            actions.user.talon_wake()
            actions.sound.set_microphone("Microphone (Yeti X)")

    def toggle_voice():
        """Toggle between Serenade and Talon."""
        actions.key("alt-z")
        actions.speech.toggle()

    # def serenade_toggle(self):
    #     """Toggle Serenade on or off."""
    #     actions.key("alt-z")
    #     if actions.speech.enabled():
    #         actions.user.talon_sleep()
    #     else:
    #         actions.user.talon_wake()