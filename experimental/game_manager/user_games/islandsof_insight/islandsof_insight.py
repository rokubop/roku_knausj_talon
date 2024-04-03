# from talon import Module, Context, actions

# mod = Module()
# ctx = Context()

# mod.apps.islandsof_insight = r"""
# os: windows
# and app.exe: IslandsofInsight-Win64-Shipping.exe
# """

# ctx.matches = r"""
# os: windows
# app: islandsof_insight
# """

# mod.mode("islandsof_insight_parrot", "Parrot mode for talos 2 game")

# @mod.action_class
# class Actions:
#     def game_v2_islandsof_insight_parrot_mode_enable():
#         """Enable game mode"""
#         actions.user.parrot_v5_mode_enable("user.islandsof_insight_parrot")

#     def game_v2_islandsof_insight_parrot_mode_disable():
#         """Disable game mode"""
#         actions.user.parrot_v5_mode_disable()

# @ctx.action_class("user")
# class Actions:
#     def on_parrot_v5_mode_enable(ev: dict):
#         if ev["mode"] == "user.islandsof_insight_parrot":
#             actions.user.game_v2_canvas_box_color("222666")
#             actions.user.game_v2_canvas_status_enable()
#             actions.user.game_v2_canvas_status_update("mode", "game")
#         elif ev["mode"] == "user.islandsof_insight_nav_mode":
#             actions.user.game_v2_canvas_box_color("FCD12A")
#             actions.user.game_v2_canvas_status_enable()
#             actions.user.game_v2_canvas_status_update("mode", "nav")
#         else:
#             actions.user.game_v2_canvas_box_color("ff0000")
#             actions.user.game_v2_canvas_status_enable()
#             actions.user.game_v2_canvas_status_update("mode", "parrot global")
#         actions.next(ev)

#     def on_parrot_v5_mode_disable(ev: dict):
#         actions.user.event_mouse_move_stop_hard()
#         actions.user.game_v2_stop_all()
#         actions.user.game_v2_canvas_status_disable()
#         actions.next(ev)
