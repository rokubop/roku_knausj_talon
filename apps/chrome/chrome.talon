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
split <user.window_snap_position>:
    user.rango_command_without_target("moveCurrentTabToNewWindow")
    sleep(200ms)
    user.snap_window(window_snap_position)

<user.teleport> dock <user.text>$:
    user.chrome_mod("o")
    sleep(200ms)
    user.insert_formatted("{text}", "NO_SPACES")
    sleep(200ms)

<user.show_list> dock <user.text>$:
    user.chrome_mod("o")
    sleep(200ms)
    edit.delete_line()
    user.insert_formatted("{text}", "NO_SPACES")

please [<user.text>]:
    key(escape ctrl-shift-p)
    sleep(200ms)
    insert(text or "")

go <number>:
    key(ctrl-g)
    "{number}"
    key(enter)

(break | bug) this:         key(ctrl-b)
(break | bug) (toggle | dog | yes | no): key(ctrl-f8)
(break | bug) pause: key(ctrl-f8)
(break | bug) resume:
    key(ctrl-f8)
    key(f8)
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

base next:                  key("ctrl-]")
base last:                  key("ctrl-[")
(base | rack) switch:       key("ctrl-shift-d")

term (show | hide | dog):   key(escape)
term clear:                 key(ctrl-l)

zen mode:                   key(ctrl-shift-y ctrl-shift-h)

(<user.teleport> | show) {user.chrome_dev_tabs}:
    user.chrome_please(chrome_dev_tabs)

inspect this:
    mouse_click(1)
    sleep(100ms)
    key(up)
    key(enter)

image save:
    mouse_click(1)
    sleep(100ms)
    key(down down)
    key(enter)

image copy:
    mouse_click(1)
    sleep(100ms)
    key(down down down)
    key(enter)

image copy url:
    mouse_click(1)
    sleep(100ms)
    key(down down down down)
    key(enter)

image (open | blank | stash):
    mouse_click(1)
    sleep(100ms)
    key(down)
    key(enter)

mobile (toggle | dog | show | hide | view): key(ctrl-shift-m)
