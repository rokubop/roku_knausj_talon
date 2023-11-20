key(keypad_multiply:down):
    user.pedal_left_down()
key(keypad_multiply:up):
    user.pedal_left_up()

key(keypad_minus:down):
    user.pedal_center_down()
key(keypad_minus:up):
    user.pedal_center_up()

key(keypad_plus:down):
    user.pedal_right_down()
key(keypad_plus:up):
    user.pedal_right_up()

pedal scroll:               user.pedal_mode_scroll()
pedal mute:                 user.pedal_mode_mute()

# KEY_NUM_LOCK 0xDB 219
# KEY_KP_SLASH: 0xDC 220
# KEY_KP_ASTERISK: 0xDD 221
