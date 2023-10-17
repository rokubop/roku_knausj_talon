from talon import Module, actions, ctrl, cron, scope, Context, settings

mod = Module()

@mod.action_class
class Actions:
    def pedal_left_down():
        """Left pedal"""
        print("default left pedal down")
        ctrl.mouse_click(button=0, down=True)

    def pedal_left_up():
        """Left pedal up"""
        print('default left pedal up')
        ctrl.mouse_click(button=0, up=True)

    def pedal_center_down():
        """Center pedal"""
        # actions.user.parrot_scroll_down()
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
        print("default center pedal down")

    def pedal_center_up():
        """Center pedal up"""
        # actions.user.parrot_scroll_stop_soft()
        print('default center pedal up')

    def pedal_right_down():
        """Right pedal"""
        actions.user.quick_pick_show()
        # actions.key("ctrl-shift-m")
        # actions.user.parrot_scroll_up()
        print("default right pedal down")

    def pedal_right_up():
        """Right pedal up"""

        # actions.user.parrot_scroll_stop_soft()
        print('default right pedal up')
