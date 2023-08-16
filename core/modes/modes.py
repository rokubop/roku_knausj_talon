from talon import Module, actions, app, speech_system

mod = Module()

modes = {
    "admin": "enable extra administration commands terminal (docker, etc)",
    "debug": "a way to force debugger commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
}

for key, value in modes.items():
    mod.mode(key, value)

global hard_sleep
hard_sleep = False

@mod.action_class
class Actions:
    def wake_if_not_hard_sleep():
        """Wakes up if hard sleep is not active."""
        if not hard_sleep:
            actions.speech.enable()
            actions.user.hud_publish_mouse_particle('float_up', '36d96a')

    def set_hard_sleep():
        """Sets hard sleep mode."""
        global hard_sleep
        hard_sleep = True

    def unset_hard_sleep():
        """Unsets hard sleep mode."""
        global hard_sleep
        hard_sleep = False


    def talon_mode():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()

        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            if app.platform == "mac":
                actions.user.engine_sleep()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("switch to command mode")

    def dragon_mode():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            if app.platform == "mac":
                actions.user.engine_wake()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("start normal mode")
