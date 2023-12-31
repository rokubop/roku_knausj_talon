key(keypad_multiply:down):  user.pedal_left_down()
key(keypad_multiply:up):    user.pedal_left_up()

key(keypad_minus:down):     user.pedal_center_down()
key(keypad_minus:up):       user.pedal_center_up()

key(keypad_plus:down):      user.pedal_right_down()
key(keypad_plus:up):        user.pedal_right_up()

pedal scroll:               user.pedal_set_tag("user.pedal_scroll_up_down")
pedal mute:                 user.pedal_set_tag("user.pedal_click_mute")
pedal gaze:                 user.pedal_set_tag("user.pedal_head_gaze")

# KEY_NUM_LOCK 0xDB 219
# KEY_KP_SLASH: 0xDC 220
# KEY_KP_ASTERISK: 0xDD 221
