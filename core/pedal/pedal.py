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
        actions.user.parrot_scroll_down()
        print("default center pedal down")

    def pedal_center_up():
        """Center pedal up"""
        actions.user.parrot_scroll_stop_soft()
        print('default center pedal up')

    def pedal_right_down():
        """Right pedal"""
        actions.user.parrot_scroll_up()
        print("default right pedal down")

    def pedal_right_up():
        """Right pedal up"""
        actions.user.parrot_scroll_stop_soft()
        print('default right pedal up')
