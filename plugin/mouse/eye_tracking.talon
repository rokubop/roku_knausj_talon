# settings():
#     user.click_stops_tracking = true
#     user.scroll_stops_tracking = true

zoom mouse:                 tracking.control_zoom_toggle()
control mouse:              tracking.control_toggle()
track calibrate:            tracking.calibrate()

track start:
    tracking.control_toggle(true)
    tracking.control_gaze_toggle(true)
    tracking.control_head_toggle(true)
track stop:
    tracking.control_toggle(false)
    tracking.control_zoom_enabled(false)
track (pause | freeze):
    tracking.control_gaze_toggle(false)
    tracking.control_head_toggle(false)
track resume:
    tracking.control_head_toggle(true)
    tracking.control_gaze_toggle(true)
track full:
    tracking.control_toggle(true)
    tracking.control_gaze_toggle(true)
    tracking.control_head_toggle(true)
track (jump | here):
    tracking.control_toggle(true)
    tracking.control_gaze_toggle(true)
    tracking.control_head_toggle(true)
    sleep(100ms)
    tracking.control_gaze_toggle(false)
    tracking.control_head_toggle(false)
track head:
    tracking.control_toggle(true)
    tracking.control_head_toggle(true)
    tracking.control_gaze_toggle(false)
track debug:                tracking.control_debug_toggle()
# track calibrate:            tracking.calibrate()
