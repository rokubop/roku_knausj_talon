# Head Triggered Actions

This allows you to trigger 4 distinct actions (up, down, left, right) based on the position of your head

## Instructions

1. Copy the `head_triggered_actions` folder to your `talon/user` directory.

    > To try out the functionality, you can uncomment `example.py` and `example.talon`, then go to Google Chrome and say `head start`. You should see a box appear on the screen that triggers "left", "right", "up", and "down" keys based on the position of your head. Say `head stop` to stop the head-triggered actions.

### User setup

2. **Create a new Python file** for the context you want to to apply to

    ```python
    ctx = Context()

    ctx.matches = r"""
    app.name: Google Chrome
    """

    ctx.settings = {
        "user.head_triggered_actions_x_threshold": 100,
        "user.head_triggered_actions_y_threshold": 50,
        "user.head_triggered_actions_show_ui": True,
    }
    ```

3. **Define these actions for the ctx**:

    ```python
    @ctx.action_class("user")
    class Actions:
        def on_head_left_trigger():
        def on_head_left_leave():
        def on_head_right_trigger():
        def on_head_right_leave():
        def on_head_up_trigger():
        def on_head_up_leave():
        def on_head_down_trigger():
        def on_head_down_leave():
        def on_head_center_trigger():
        def on_head_center_leave():
    ```

4. **Create Talon actions** to start, stop, or reset the head-triggered actions.

    ```python
    head start:                 user.head_triggered_actions_start()
    head stop:                  user.head_triggered_actions_stop()
    head reset:                 user.head_triggered_actions_reset()
    ```