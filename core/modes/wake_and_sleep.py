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

    def sleep_toggle():
        """Toggle between sleep and wake."""
        if actions.user.is_hard_sleep():
            actions.user.hud_publish_mouse_particle('float_up', '36d96a')
            actions.speech.enable()
        else:
            actions.user.hud_publish_mouse_particle('float_up', '493fd9')
            actions.user.switcher_hide_running()
            actions.user.history_disable()
            actions.user.homophones_hide()
            actions.user.help_hide()
            actions.user.mouse_sleep()
            actions.speech.disable()
            actions.user.engine_sleep()
        actions.user.toggle_hard_sleep()