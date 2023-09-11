# go <user.arrow_keys>:       user.move_cursor(arrow_keys)
<user.letter>:              key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>:          key(symbol_key)
<user.function_key>:        key(function_key)
<user.special_key>:         key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
# for key combos consisting only of modifiers, eg. `press super`.
press <user.modifiers>:     key(modifiers)
# for consistency with dictation mode and explicit arrow keys if you need them.
press <user.keys>:          key(keys)

hold <user.modifiers>:      key("{modifiers}:down")
hold <user.keys>:           key("{keys}:down")
release <user.keys>:        key("{keys}:up")
release <user.modifiers>:   key("{modifiers}:up")
caps lock:                  key(capslock)
num lock:                   key(numlock)
# doesn't work
# key(alt-l): key(right)
# key(alt-j): key(down)
# key(alt-k): key(up)
# key(alt-h): key(left)

# key(alt-shift-l): key(shift-right)
# key(alt-shift-j): key(shift-down)
# key(alt-shift-k): key(shift-up)
# key(alt-shift-h): key(shift-left)
