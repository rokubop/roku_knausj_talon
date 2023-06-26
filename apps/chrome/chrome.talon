app: chrome
-
tag(): browser
tag(): user.tabs
tag(): user.find

<user.teleport> (profile | user):
    user.chrome_mod("shift-m")
    sleep(200ms)
    key(enter)

<user.teleport> tab:
    user.chrome_mod("shift-a")
    sleep(200ms)
    key(enter)

<user.teleport> [tab] <user.text>$:
    user.chrome_mod("shift-a")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")
    key(enter)

<user.find> tab:            user.chrome_mod("shift-a")
tab (recent | <user.show_list>): user.chrome_mod("shift-a")

tab (recent | <user.show_list>) <user.text>$:
    user.chrome_mod("shift-a")
    sleep(200ms)
    insert("{text}")

tab split:                  user.rango_command_without_target("moveCurrentTabToNewWindow")

<user.teleport> dock <user.text>$:
    user.chrome_mod("o")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")
    key(enter)

<user.find> dock <user.text>$:
    user.chrome_mod("o")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")

please [<user.text>]:
    key(escape ctrl-shift-p)
    insert(text or "")

go <number>:
    key(ctrl-g)
    "{number}"
    key(enter)

[breakpoint | breakpoints] (toggle | dog): key(ctrl-f8)

(light | dark) mode:        key(alt-shift-d)
