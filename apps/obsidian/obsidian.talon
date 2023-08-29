app: obsidian
-
tag(): user.tabs
tag(): user.find
tag(): user.line_commands
tag(): user.splits
tag(): user.emoji
tag(): user.ocr_cursorless

<user.teleport> daily note:
    key(ctrl-p)
    insert('today daily note')
    key(enter)

<user.teleport> [<user.text>] [{user.file_extension}]:
    key(ctrl-o)
    edit.delete_line()
    sleep(100ms)
    insert(text or "")
    insert(file_extension or "")
    sleep(300ms)

please [<user.text>]:
    key(ctrl-p)
    edit.delete_line()
    insert(text or "")

add H one [<user.text>]:
    insert("# ")
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
add H two [<user.text>]:
    insert("## ")
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
add H three [<user.text>]:
    insert("### ")
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
add H four [<user.text>]:
    insert("#### ")
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
add H five [<user.text>]:
    insert("##### ")
    user.insert_formatted(text or "", "CAPITALIZE_FIRST_WORD")
add list: insert("- ")
add task: insert("- [ ] ")
task (yes | no): key(ctrl-l)

bar (show | hide | dog) | (show | hide) (bar | files):
    key(alt-b)

rack (show | hide | dog) | (show | hide) (rack | calendar):
    key(alt-c)

task (dog | check | uncheck | complete):
    key(ctrl-l)

show (help | settings): key(ctrl-,)