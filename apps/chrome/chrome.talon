app: chrome
-
tag(): browser
tag(): user.tabs
tag(): user.find
tag(): user.emoji


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

(break | bug) [toggle | dog]: key(ctrl-f8)
(break | bug) (pause | resume): key(ctrl-f8)
(break | bug) (step | step over): key(f10)
(break | bug) (step in | step into): key(f11)
(break | bug) (step out | step outside): key(shift-f11)
(break | bug) (continue | run | play): key(f8)
break <number>:
    key(ctrl-g)
    "{number}"
    key(enter)
    sleep(100ms)
    key(ctrl-b)


(light | dark) mode:        key(alt-shift-d)
(hide | show) rack | rack (hide | show | dog | toggle): key(ctrl-shift-h)
(hide | show) bar | bar (hide | show | dog | toggle): key(ctrl-shift-y)
(hide | show) base | base (hide | show | dog | toggle): key(f12)
zen mode: key(ctrl-shift-y ctrl-shift-h)

<user.teleport> (sources | source):
    key(escape ctrl-shift-p)
    insert("sources")
    sleep(100ms)
    key(enter)

<user.teleport> network:
    key(escape ctrl-shift-p)
    insert("network")
    sleep(100ms)
    key(enter)

<user.teleport> elements:
    key(escape ctrl-shift-p)
    insert("elements")
    sleep(100ms)
    key(enter)

<user.teleport> (console | counsel):
    key(escape ctrl-shift-p)
    insert("console")
    sleep(100ms)
    key(enter)