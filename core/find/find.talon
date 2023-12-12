tag: user.find
-

<user.find> clip:           edit.find(clip.text())
# scout [<user.text>]$: edit.find(text or "")
scout [{user.prose_formatter}] <user.prose>$:
      key("ctrl-f")
      user.insert_formatted(prose, prose_formatter or "NOOP")
scout all [{user.prose_formatter}] <user.prose>$:
    key("ctrl-shift-f")
    user.insert_formatted(prose, prose_formatter or "NOOP")

<user.find> (all | ale) clip: user.find_everywhere(clip.text())

replace [<user.text>]$:     user.find_replace(text or "")
replace (all | ale) [<user.text>]$: user.find_replace_everywhere(text or "")

<user.find> case:           user.find_toggle_match_by_case()
<user.find> whole:          user.find_toggle_match_by_word()
<user.find> (expression | regex): user.find_toggle_match_by_regex()
replace case:               user.find_replace_toggle_preserve_case()

<user.find> last:           edit.find_previous()
<user.find> next:           edit.find_next()

<user.find> hide:
    edit.find("")
    sleep(100ms)
    key(escape)

replace confirm:            user.find_replace_confirm()
replace confirm (all | ale): user.find_replace_confirm_all()

<user.find> file clip:      user.find_file(clip.text())
<user.find> file [<user.filename>]$:
    user.find_file(filename or "")

<user.find> this:
    key(ctrl-c)
    sleep(100ms)
    edit.find(clip.text())
    sleep(100ms)
    key(enter)
