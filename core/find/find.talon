tag: user.find
-

scout clip:                 edit.find(clip.text())
# scout [<user.text>]$: edit.find(text or "")
scout [{user.prose_formatter}] [<user.prose>]$:
    key("ctrl-f")
    user.insert_formatted(prose or "", prose_formatter or "NOOP")
scout all [{user.prose_formatter}] [<user.prose>]$:
    key("ctrl-shift-f")
    user.insert_formatted(prose or "", prose_formatter or "NOOP")

scout (all | ale) clip:     user.find_everywhere(clip.text())

replace [<user.text>]$:     user.find_replace(text or "")
replace (all | ale) [<user.text>]$: user.find_replace_everywhere(text or "")

scout case:                 user.find_toggle_match_by_case()
scout whole:                user.find_toggle_match_by_word()
scout (expression | regex): user.find_toggle_match_by_regex()
replace case:               user.find_replace_toggle_preserve_case()

scout last:                 edit.find_previous()
scout next:                 edit.find_next()

scout hide:
    edit.find("")
    sleep(100ms)
    key(escape)

replace confirm:            user.find_replace_confirm()
replace confirm (all | ale): user.find_replace_confirm_all()

scout file clip:            user.find_file(clip.text())
scout file [<user.filename>]$:
    user.find_file(filename or "")

scout this:
    key(ctrl-c)
    sleep(100ms)
    edit.find(clip.text())
    sleep(100ms)
    key(enter)
