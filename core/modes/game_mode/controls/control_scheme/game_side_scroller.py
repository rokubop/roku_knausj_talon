from talon import Module, Context, actions, actions, cron

mod = Module()
ctx = Context()
ctx.matches = """
tag: user.game_side_scroller
"""

is_moving = False
current_movement = ""
is_crouched = False
is_menu = True
is_game = False

@mod.action_class
class Actions:
    def game_side_scroller_toggle_menu_mode():
        """toggle menu mode"""
        global is_menu
        global is_game
        is_menu = True
        is_game = False

    def game_side_scroller_toggle_game_mode():
        """toggle game mode"""
        global is_menu
        global is_game
        is_game = True
        is_menu = False

    def game_side_scroller_start_stop():
        """start or stop moving"""
        global is_moving
        global current_movement
        if is_moving:
            is_moving = False
            for key in ["w", "a", "d"]:
                actions.key(f"{key}:up")
        else:
            is_moving = True
            actions.key(f"{current_movement}:down")

    def game_side_scroller_direction(dir: str):
        """move direction"""
        global is_moving
        global current_movement
        is_moving = True
        current_movement = dir;
        for key in ["w", "a", "d"]:
            if key == dir:
                actions.key(f"{key}:down")
            else:
                actions.key(f"{key}:up")

    def game_side_scroller_right():
        """move right"""
        actions.user.game_side_scroller_direction("d")

    def game_side_scroller_left():
        """move left"""
        actions.user.game_side_scroller_direction("a")

    def game_side_scroller_up():
        """move up"""
        actions.user.game_side_scroller_direction("w")

    def game_side_scroller_down():
        """move down"""
        actions.user.game_side_scroller_direction("s")


@ctx.action_class("user")
class UserActions:
    def game_crouch():
        global is_crouched
        if is_crouched:
            is_crouched = False
            actions.key("s:up")
        else:
            is_crouched = True
            actions.key("s:down")

    def on_palate():
        actions.user.game_jump()

    def on_pop():
        actions.user.game_side_scroller_start_stop()

    def noise_shush_start():
        actions.user.game_side_scroller_left()

    def noise_shush_stop():
        print("")

    def noise_hiss_start():
        actions.user.game_side_scroller_right()

    def noise_hiss_stop():
        print("")