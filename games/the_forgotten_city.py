from talon import Module, Context, actions, ctrl, cron

mod = Module()
mod.apps.the_forgotten_city = """
app.name: The Forgotten City
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: the_forgotten_city
"""

#
# horse_run = None

# @ctx.action_class("user")
# class GameActions:
    # def get_held_game_keys():
    #     keys = ["shift", "enter", "escape", "a", "d", "w", "r", "s", "e", "up", "down", "left", "right"]
    #     return keys

    # def game_inventory_show():
    #     actions.key("b")

    # def custom_game_cleanup():
    #     actions.user.rdr_horse_stop()

    # def release_held_game_keys():
    #     for key in actions.user.get_held_game_keys():
    #         actions.user.release_game_key(key)
    #     actions.user.rdr_horse_stop()

    # def game_camera_first_person():
    #     actions.key("v")


# @mod.action_class
# class TheForgottenCityActions:
#     def fc_test():
#         """"""
#         ctrl.key_press("space", hold=8000)
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