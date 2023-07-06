from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.apps.dave_the_diver = """
title: DAVE THE DIVER
app.exe: DaveTheDiver.exe
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: dave_the_diver
"""

horse_run = None

@ctx.action_class("user")
class GameActions:
    def get_held_game_keys():
        keys = ["shift", "enter", "escape", "a", "d", "w", "r", "s", "e", "up", "down", "left", "right"]
        return keys

    def game_inventory_show():
        actions.key("b")

    def custom_game_cleanup():
        actions.user.rdr_horse_stop()

    def release_held_game_keys():
        for key in actions.user.get_held_game_keys():
            actions.user.release_game_key(key)
        actions.user.rdr_horse_stop()

    def game_camera_first_person():
        actions.key("v")


@mod.action_class
class DaveTheDiverActions:

    def dave_mouse_click(button: int = 0):
        """Click the mouse button"""
        ctrl.mouse_click(button=button, hold=64000)


    def dave_test():
        """Click the mouse button"""
        print("test")
        ctrl.key_press("a", hold=64000)

    # def rdr_horse_kick():
    #     """"""
    #     actions.key("w")

    # def rdr_horse_run():
    #     """"""
    #     global horse_run
    #     if horse_run:
    #         return
    #     horse_run = cron.interval("200ms", actions.user.rdr_horse_kick)

    # def rdr_horse_stop():
    #     """"""
    #     global horse_run
    #     if not horse_run:
    #         return
    #     cron.cancel(horse_run)
    #     horse_run = None