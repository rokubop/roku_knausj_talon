from talon import Module, actions, ctrl, cron, scope, Context, settings

mod = Module()

pedal_mode = "scroll"

right_down = False
right_side_b = False
right_toggle = False

@mod.action_class
class Actions:
    def pedal_left_down():
        """Left pedal"""
        global right_side_b

        if right_down:
            right_side_b = True
            return

        # actions.key("ctrl-shift-m")
        if pedal_mode == "scroll":
            actions.user.mouse_scrolling("up")
        elif pedal_mode == "mute":
            ctrl.mouse_click(button=0, down=True)

    def pedal_left_up():
        """Left pedal up"""

        if pedal_mode == "scroll":
            actions.user.mouse_scroll_stop()
        elif pedal_mode == "mute":
            ctrl.mouse_click(button=0, up=True)

    def pedal_center_down():
        """Center pedal"""
        if pedal_mode == "scroll":
            actions.user.mouse_scrolling("down")
        elif pedal_mode == "mute":
            actions.speech.toggle()

    def pedal_center_up():
        """Center pedal up"""
        if pedal_mode == "scroll":
            actions.user.mouse_scroll_stop()

    def pedal_right_down():
        """Right pedal"""
        global right_toggle

        if right_toggle:
            right_toggle = False

            actions.user.hud_publish_mouse_particle('float_up', '30F343')
            actions.speech.toggle(True)
            actions.user.talon_wake()
            actions.sound.set_microphone("Microphone (Yeti X)")
            actions.user.hud_add_log('event', '<*Using Talon Voice/>')
            return
        else:
            right_toggle = True
            actions.speech.toggle(False)
            actions.user.hud_publish_mouse_particle('float_up', 'ff0000')
            actions.sleep("1s")
            actions.sound.set_microphone("None")
            actions.user.talon_sleep()
            return
        # global right_down
        # right_down = True
        # # actions.user.quick_pick_show()
        # actions.speech.toggle(True)
        # actions.user.talon_wake()
        # actions.sound.set_microphone("Microphone (Yeti X)")

    def pedal_right_up():
        """Right pedal up"""
        # global right_down, right_side_b
        # right_down = False
        # if right_side_b:
        #     right_side_b = False
        #     actions.speech.toggle(True)
        #     actions.user.talon_wake()
        #     actions.sound.set_microphone("Microphone (Yeti X)")
        #     return
        # actions.speech.toggle(False)
        # actions.user.talon_sleep()
        # actions.sound.set_microphone("None")

    def pedal_mode_scroll():
        """Change the pedal mode to scroll"""
        global pedal_mode
        pedal_mode = "scroll"

    def pedal_mode_mute():
        """Change the pedal mode to mute"""
        global pedal_mode
        pedal_mode = "mute"


