from talon import Module, actions

mod = Module()

setting_gaze_start = True
setting_head_start = True

gaze = setting_gaze_start
head = setting_head_start
last_head = setting_gaze_start
last_gaze = setting_head_start

@mod.action_class
class Actions:
    def tracking_control_gaze_toggle(state: bool = None):
        """Toggle gaze tracking"""
        global gaze, last_gaze
        last_gaze = gaze
        gaze = not gaze if state is None else state
        actions.tracking.control_gaze_toggle(gaze)

    def tracking_control_head_toggle(state: bool = None):
        """Toggle head tracking"""
        global head, last_head
        last_head = head
        head = not head if state is None else state
        actions.tracking.control_head_toggle(head)

    def tracking_control_enable():
        """Enable eye tracker"""
        global last_gaze, last_head
        if not actions.tracking.control_enabled():
            actions.tracking.control_toggle(True)
        actions.user.tracking_control_head_toggle(last_head)
        actions.user.tracking_control_gaze_toggle(last_gaze)

    def tracking_control_disable():
        """Disable eye tracker"""
        actions.tracking.control_toggle(False)

    def tracking_control_toggle(state: bool = None):
        """Toggle eye tracker"""
        if state is None:
            state = not actions.tracking.control_enabled()
        if state:
            actions.user.tracking_control_enable()
        else:
            actions.user.tracking_control_disable()

    def tracking_control_resume():
        """Resume eye tracker"""
        global last_gaze, last_head
        actions.user.tracking_control_head_toggle(last_head)
        actions.user.tracking_control_gaze_toggle(last_gaze)

    def tracking_control_teleport():
        """Teleport to gaze position"""
        global head, gaze
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(True)
        actions.sleep("50ms")
        actions.tracking.control_head_toggle(head)
        actions.tracking.control_gaze_toggle(gaze)

    def tracking_control_freeze():
        """Tracking freeze"""
        actions.user.tracking_control_head_toggle(False)
        actions.user.tracking_control_gaze_toggle(False)
