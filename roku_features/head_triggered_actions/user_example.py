from talon import Module, Context, actions

ctx = Context()

ctx.matches = r"""
# replace this with the application this applies to
app.name: Google Chrome
"""

ctx.settings = {
    "user.head_triggered_actions_x_threshold": 100,
    "user.head_triggered_actions_y_threshold": 50,
    "user.head_triggered_actions_show_ui": True,
}

@ctx.action_class("user")
class Actions:
    def on_head_left_trigger():
        print("on_head_left_trigger")
        # actions.key('a:down')
        # actions.key('left:down')

    def on_head_left_leave():
        print("on_head_left_leave")
        # actions.key('a:up')
        # actions.key('left:up')

    def on_head_right_trigger():
        print("on_head_right_trigger")
        # actions.key('d:down')
        # actions.key('right:down')

    def on_head_right_leave():
        print("on_head_right_leave")
        # actions.key('d:up')
        # actions.key('right:up')
#
    def on_head_up_trigger():
        print("on_head_up_trigger")
        # actions.key('w:down')
        # actions.key('up:down')

    def on_head_up_leave():
        print("on_head_up_leave")
        # actions.key('w:up')
        # actions.key('up:up')

    def on_head_down_trigger():
        print("on_head_down_trigger")
        # actions.key('s:down')
        # actions.key('down:down')

    def on_head_down_leave():
        print("on_head_down_leave")
        # actions.key('s:up')
        # actions.key('down:up')

    # def on_head_center_trigger():
    #     pass

    # def on_head_center_leave():
    #     pass