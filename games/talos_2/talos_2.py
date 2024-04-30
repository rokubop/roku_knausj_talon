# from talon import Module, Context, actions
# mod = Module()
# ctx = Context()
# mod.apps.talos_2 = r"""
# os: windows
# and app.exe: Talos2-Win64-Shipping.exe
# """
# ctx.matches = r"""
# os: windows
# app: talos_2
# """
# @ctx.action_class("user")
# class Actions:
#     def pedal_left_down():
#         actions.user.fps_turn_left()

#     def pedal_left_up():
#         actions.user.fps_turn_left_stop()

#     def pedal_center_down():
#         actions.user.fps_turn_right()

#     def pedal_center_up():
#         actions.user.fps_turn_right_stop()

#     def pedal_right_down():
#         actions.user.fps_move_forward_toggle()

#     def pedal_right_up():
#         actions.skip()
