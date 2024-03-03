# Head Triggered Actions

This allows you to trigger 4 distinct actions (up, down, left, right) based on the position of your head

## Instructions

1. Copy the `head_triggered_actions.py` file to your `talon/user` directory, and also `user_example.py` and `user_example.talon`.

    To try out the functionality, you can say `head start`. This will enable head tracking only, and you should see a box appear on the screen, and a red line that indicates when you've passed the threshold for left, right, up, down. You must assign actions to these. Say `head stop` to stop the head-triggered actions. Say `head reset` to reset the position.

### User setup

2. **Copy user_example.py** for the context you want to to apply to

    ```python
    from talon import Context

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

## Other info:
- Sometimes the mouse jumps while in head tracking mode, so this tries to recalibrate the anchor point every time that happens.
- Sometimes you will still need to manually reset the position
- Defaults to frozen mouse after stopping
- Does not work with mouse movement actions like turning a character in game, because every time you programmatically move the mouse, you lose head tracking ability for 1 second.