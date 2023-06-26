from talon import Module, actions, Context

game_camera_module = Module()

setting_turn_around_delta = game_camera_module.setting(
    "game_turn_around_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera around

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_turn_horizontally_delta = game_camera_module.setting(
    "game_turn_horizontally_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera horizontally

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_turn_vertically_delta = game_camera_module.setting(
    "game_turn_vertically_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular vertical delta
        that mouse needs to be moved by
        in order to turn the camera vertically

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")

game_camera_module.tag("game_camera_controls")
game_camera_module.list("game_camera_direction")
ctx = Context()
ctx.matches = """mode: user.game"""
ctx.lists["user.game_camera_direction"] = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "let": "left",
    "rye": "right",
}

def _mouse_move(dx: int, dy: int):
    print("mouse move", dx, dy)
    import platform
    os = platform.system().lower()
    if os.startswith("windows"):
        import win32api, win32con
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
        # I couldn't get the usual ctrl.mouse_move call to work with most first/third person games on windows
        # winAPI does not produce the most reproducible results but it works well enough
    else:
        # todo find out what API best integrates with games for each platform
        from talon import ctrl
        (x, y) = ctrl.mouse_pos()
        x += dx
        y += dy
        ctrl.mouse_move(x, y, dx=dx, dy=dy)


@game_camera_module.action_class
class CameraActions:

    def game_turn_camera_around():
        """WIP turn camera around"""
        dx = setting_turn_around_delta.get()
        _mouse_move(dx, 0)

    def game_turn_camera(direction: str, cursor_movement_multiplier: float = None):
        """WIP turn camera in the specified direction"""
        dy = dx = 0
        if direction in ["right", "left"]:
            dx = setting_turn_horizontally_delta.get()
        elif direction in ["down", "up"]:
            dy = setting_turn_vertically_delta.get()

        if direction == "left":
            dx *= -1
        elif direction == "up":
            dy *= -1

        if cursor_movement_multiplier:
            dx = (int)(dx * cursor_movement_multiplier)
            dy = (int)(dy * cursor_movement_multiplier)

        _mouse_move(dx, dy)

    def game_camera_first_person():
        """Change camera to first person perspective. No action performed by default. Needs to be overridden."""
        return

    def game_camera_third_person():
        """Change camera to third person perspective. Defaults to calling actions.user.game_camera_first_person()"""
        actions.user.game_camera_first_person()


game_camera_module.tag("game_camera_zoom")


# to do: setting for adjusting zoom amount
@game_camera_module.action_class
class CameraZoomActions:

    def game_camera_zoom_level_switch():
        """Change zoom level, as in an isometric cRPG. Defaults to pressing z."""
        actions.key("z")

    def game_camera_zoom_in():
        """Zoom in the camera. Defaults to a singular scroll up.
        Adjust the setting: user.mouse_wheel_down_amount to adjust the zoom amount."""
        actions.user.mouse_scroll_up()

    def game_camera_zoom_out():
        """Zoom out the camera. Defaults to a singular scroll down.
        Adjust the setting: user.mouse_wheel_down_amount to adjust the zoom amount."""
        actions.user.mouse_scroll_down()

    def game_camera_zoom_in_continuous():
        """Zoom in the camera continuously. Defaults to a singular scroll up.
        Adjust the setting: user.mouse_continuous_scroll_amount to adjust the zoom amount.
        """
        actions.user.mouse_scroll_up_continuous()

    def game_camera_zoom_out_continuous():
        """Zoom out the camera continuously. Defaults to a singular scroll down.
        Adjust the setting: user.mouse_continuous_scroll_amount to adjust the zoom amount.
        """
        actions.user.mouse_scroll_down_continuous()

    def game_camera_zoom_continuous_stop():
        """Stop continuous camera zoom. Defaults to user.mouse_scroll_stop().
        See also the settings: user.mouse_enable_pop_stops_scroll, user.mouse_enable_hiss_stops_scroll"""
        actions.user.mouse_scroll_stop()
