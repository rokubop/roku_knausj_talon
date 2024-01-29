from talon import Module, actions

mod = Module()

gaze = False
head = False

@mod.action_class
class Actions:
    def tracking_control_gaze_toggle(state: bool = None):
        """Toggle gaze tracking"""
        global gaze
        gaze = state or not gaze
        actions.tracking.control_gaze_toggle(gaze)

    def tracking_control_head_toggle(state: bool = None):
        """Toggle head tracking"""
        global head
        head = state or not head
        actions.tracking.control_gaze_toggle(head)

    def tracking_control_gaze_enabled():
        """Check if gaze tracking is enabled"""
        return gaze

    def tracking_control_head_enabled():
        """Check if head tracking is enabled"""
        return head

    def tracking_teleport_use_head():
        """Toggle omega mouse"""
        actions.tracking.control_toggle(True)
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        actions.tracking.control_head_toggle(True)
        actions.tracking.control_gaze_toggle(False)

    def tracking_freeze():
        """Tracking freeze"""
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(False)
