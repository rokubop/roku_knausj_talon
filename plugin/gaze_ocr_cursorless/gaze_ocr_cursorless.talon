tag: user.ocr_cursorless
-
# Prerequisite: talon-gaze-ocr
# Cursorless like commands for apps without cursorless like text editors
hover <user.timestamped_prose>$: user.move_cursor_to_word(timestamped_prose)
click <user.timestamped_prose>$: user.click_text(timestamped_prose)
double click <user.timestamped_prose>$: user.double_click_text(timestamped_prose)
right click <user.timestamped_prose>$: user.right_click_text(timestamped_prose)
middle click <user.timestamped_prose>$: user.middle_click_text(timestamped_prose)
<user.modifiers> click <user.timestamped_prose>$:
    user.modifier_click_text(modifiers, timestamped*_prose)
pre <user.timestamped_prose>$: user.move_text_cursor_to_word(timestamped_prose, "before")
post <user.timestamped_prose>$: user.move_text_cursor_to_word(timestamped_prose, "after")
post <user.timestamped_prose> then:
    user.move_text_cursor_to_word(timestamped_prose, "after")
    skip()
pour <user.timestamped_prose>$:
    user.move_text_cursor_to_word(timestamped_prose, "before")
    edit.line_insert_down()
drink <user.timestamped_prose>$:
    user.move_text_cursor_to_word(timestamped_prose, "before")
    edit.line_insert_up()

take <user.prose_range>$: user.perform_ocr_action("select", "", prose_range)
twin wrap <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key(')
quad wrap <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key(")
curly wrap <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("{")
ski wrap <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("`")
quad wrap this: key(")
twin wrap this: key(')
round wrap this: key("(")
square wrap this: key("[")
curly wrap this: key("{")
ski wrap this: key("`")
round wrap <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("(")
square wrap <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("[")
form bold at <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("ctrl-b")
form task at <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("ctrl-l")
form (itatlic | itatlics) at <user.prose_range>$:
    user.perform_ocr_action("select", "", prose_range)
    key("ctrl-i")

{user.ocr_actions} [{user.ocr_modifiers}] <user.prose_range>$:
    user.perform_ocr_action(ocr_actions, ocr_modifiers or "", prose_range)

(clear | change) [{user.ocr_modifiers}] <user.prose_range> (word | say) <user.prose>$:
    user.replace_text(ocr_modifiers or "", prose_range, prose)
pre <user.timestamped_prose> (word | say) <user.prose>$:
    user.insert_adjacent_to_text(timestamped_prose, "before", prose)
post <user.timestamped_prose> (word | say) <user.prose>$:
    user.insert_adjacent_to_text(timestamped_prose, "after", prose)
phones <user.timestamped_prose>$:
    user.change_text_homophone(timestamped_prose)