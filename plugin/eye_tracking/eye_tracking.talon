zoom mouse:                 tracking.control_zoom_toggle()
control mouse:              tracking.control_toggle()
track calibrate:            tracking.calibrate()

tracker:                    user.tracking_control_toggle()
track start:                user.tracking_control_toggle(true)
track stop:                 user.tracking_control_toggle(false)
track (pause | freeze):     user.tracking_control_freeze()
track resume:               user.tracking_control_resume()
track full:
    user.tracking_control_toggle(true)
    user.tracking_control_gaze_toggle(true)
    user.tracking_control_head_toggle(true)
track (jump | here):        user.tracking_control_teleport()
track head:
    user.tracking_control_toggle(true)
    user.tracking_control_head_toggle(true)
    user.tracking_control_gaze_toggle(false)
track debug:                tracking.control_debug_toggle()
