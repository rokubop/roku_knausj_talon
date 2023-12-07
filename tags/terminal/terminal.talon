tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

<user.teleport> <user.text>: "z {text}\n"
lisa:                       user.terminal_list_directories()
lisa all:                   user.terminal_list_all_directories()
katie [dir] [<user.text>]:  user.terminal_change_directory(text or "")
katie root:                 user.terminal_change_directory_root()
katie (up | back):          user.terminal_change_directory("..")
go <user.system_path>:      insert('cd "{system_path}"\n')
path <user.system_path>:    insert('"{system_path}"')
clear screen:               user.terminal_clear_screen()
run last:                   user.terminal_run_last()
rerun [<user.text>]:        user.terminal_rerun_search(text or "")
rerun search:               user.terminal_rerun_search("")
kill all:                   user.terminal_kill_all()
make dear:                  "mkdir"
make dear <user.text>:      "mkdir {text}"
show settings:              key(ctrl-,)
grep [<user.text>]:         user.insert_between('grep -iE \'{text or ""}', '\'')
grep exclude [<user.text>]: user.insert_between('grep -ivE \'{text or ""}', '\'')
history:                    "history -n 20 | code -\n"

copy paste:
    edit.copy()
    sleep(50ms)
    edit.paste()
