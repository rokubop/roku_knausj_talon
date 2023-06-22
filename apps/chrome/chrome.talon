app: chrome
-
tag(): browser
tag(): user.tabs

profile switch:
    user.chrome_mod("ctrl-shift-m")
    sleep(200ms)
    key(enter)

tab (recent | <user.show_list>): user.chrome_mod("ctrl-shift-a")

tab (recent | <user.show_list>) <user.text>$:
    user.chrome_mod("ctrl-shift-a")
    sleep(200ms)
    insert("{text}")

tab <user.teleport> <user.text>$:
    user.chrome_mod("ctrl-shift-a")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")
    key(enter)

tab split:                  user.rango_command_without_target("moveCurrentTabToNewWindow")

<user.teleport> [dock] <user.text>$:
    user.chrome_mod("ctrl-o")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")
    key(enter)

<user.find> dock <user.text>$:
    user.chrome_mod("ctrl-o")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")

please [<user.text>]:
    key(escape ctrl-shift-p)
    insert(text or "")

(light | dark) mode:        key(alt-shift-d)
