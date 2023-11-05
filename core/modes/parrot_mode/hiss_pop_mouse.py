# from talon import Module, Context, actions
# from ....plugin.debouncer import Debouncer

# mod_parrot_hiss_pop_mouse = Module()
# # mod_parrot_hiss_pop_mouse.mode("parrot", "Parrot Mode for controlling mouse, modifiers, and scrolling")
# mod_parrot_hiss_pop_mouse.tag("parrot_hiss_pop_mouse", desc="Tag for hiss pop mouse")

# ctx = Context()

# hiss_debouncer = Debouncer(
#     150,
#     actions.user.parrot_hiss_pop_mouse_prepare_click,
#     actions.user.noooppp)

# is_gaze_enabled = False

# @mod_parrot_hiss_pop_mouse.action_class
# class ParrotHissPopMouseActions:
#     def parrot_hiss_pop_mouse_click():
#         """Hiss pop mouse click"""
#         actions.mouse_click()
#         if not is_gaze_enabled:
#             actions.tracking.control_gaze_toggle(False)
#             actions.tracking.control_head_toggle(False)

#     def parrot_hiss_pop_mouse_and_scroll_start():
#         """Hiss pop mouse and scroll start"""
#         hiss_debouncer.start()

#     def parrot_hiss_pop_mouse_and_scroll_stop_soft():
#         """Stop scrolling the mouse"""
#         hiss_debouncer.stop()

#     def noooppp():
#         """Noop"""
#         print("nop")

#     def parrot_hiss_pop_mouse_prepare_click():
#         """Hiss pop mouse prepare click"""
#         global is_gaze_enabled
#         print("Hiss pop mouse prepare click")
#         # Turn on gaze momentarily to teleport the mouse
#         actions.tracking.control_head_toggle(False)
#         actions.tracking.control_gaze_toggle(True)
#         actions.sleep("50ms")
#         # Prepare for click by using head tracking
#         actions.tracking.control_gaze_toggle(False)
#         actions.sleep("50ms")
#         actions.tracking.control_head_toggle(True)
#         is_gaze_enabled = False

#     def parrot_hiss_pop_mouse_halt_no_click_soft():
#         """Hiss pop mouse halt no click"""
#         actions.sleep("500ms")
#         actions.tracking.control_gaze_toggle(False)
#         actions.tracking.control_head_toggle(False)

#     def parrot_hiss_pop_mouse_halt_no_click():
#         """Hiss pop mouse halt no click"""
#         actions.tracking.control_gaze_toggle(False)
#         actions.tracking.control_head_toggle(False)

#     def parrot_hiss_pop_mouse_set_default_tracking():
#         """Hiss pop mouse set default tracking"""
#         global is_gaze_enabled
#         actions.tracking.control_gaze_toggle(True)
#         actions.tracking.control_head_toggle(True)
#         is_gaze_enabled = True

#     def parrot_hiss_pop_mouse_stop_if_preferred():
#         """Hiss pop mouse stop if preferred"""
#         if not is_gaze_enabled:
#             actions.tracking.control_gaze_toggle(False)
#             actions.tracking.control_head_toggle(False)

#     def parrot_hiss_pop_mouse_enable():
#         """Parrot hiss pop mouse enable"""
#         print("Parrot hiss pop mouse enabled")
#         actions.user.add_green_cursor()
#         # actions.tracking.control_toggle(True)
#         ctx.tags = ["user.parrot_hiss_pop_mouse"]

#     def parrot_hiss_pop_mouse_disable():
#         """Parrot hiss pop mouse disable"""
#         global is_gaze_enabled
#         print("Parrot hiss pop mouse disabled")
#         actions.user.clear_screen_regions()
#         actions.user.add_red_cursor()
#         actions.tracking.control_gaze_toggle(False)
#         actions.tracking.control_head_toggle(False)
#         is_gaze_enabled = False
#         # actions.tracking.control_gaze_toggle(True)
#         # actions.tracking.control_head_toggle(True)
#         # actions.tracking.control_toggle(False)
#         ctx.tags = []

# # mod = Module()
# # mod.mode("parrot", "Parrot Mode for controlling mouse, modifiers, and scrolling")
# # ctx = Context()
# # @mod.action_class
# # class ParrotModeActions:
# #     def parrot_hiss_pop_mouse_enable():
# #         """Parrot hiss pop mouse enable"""
# #         print("Parrot hiss pop mouse enabled")
# #         actions.user.add_green_cursor()
# #         actions.tracking.control_toggle(True)
# #         ctx.tags = ["user.parrot_hiss_pop_mouse"]

# #     def parrot_hiss_pop_mouse_disable():
# #         """Parrot hiss pop mouse disable"""
# #         print("Parrot hiss pop mouse disabled")
# #         actions.user.clear_screen_regions()
# #         actions.user.add_red_cursor()
# #         actions.tracking.control_gaze_toggle(True)
# #         actions.tracking.control_head_toggle(True)
# #         ctx.tags = []
