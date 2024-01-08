# from talon import Module, Context, actions

# mod = Module()

# head = False
# gaze = False

# @mod.action_class
# class Actions:
#     def use_tag_tracking_head():
#         """Use head tracking only"""
#         if not actions.tracking.control_enabled():
#             actions.tracking.control_toggle(True)
#         actions.tracking.control_
#         actions.tracking.control_gaze_enabled()
#         actions.tracking.control_head_enabled()
#         actions.user.tracking_control_head_toggle(True)
#         actions.user.tracking_control_gaze_toggle(False)

#     def use_tag_tracking_full():
#         """Use gaze and head tracking"""
#         if not actions.tracking.control_enabled():
#             actions.tracking.control_toggle(True)
#         head_toggle(True)
#         gaze_toggle(True)

#     def tracking_control_head_toggle(enabled: bool):
#         """Toggle head tracking"""
#         head = enabled or not head
#         actions.tracking.control_head_toggle(head)

#     def tracking_control_gaze_toggle(enabled: bool):
#         """Toggle gaze tracking"""
#         gaze = enabled or not gaze
#         actions.tracking.control_gaze_toggle(gaze)


#     def tracking_control_head_enabled():
#         """Returns whether head tracking is enabled"""
#         return head

#     def tracking_control_gaze_enabled():
#         """Returns whether gaze tracking is enabled"""
#         return gaze
