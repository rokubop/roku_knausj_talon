win.title: /DevTools/
mode: command
-

pop [<user.text>]:
    key("ctrl-p")
    sleep(400ms)
    user.insert_formatted(text, "NO_SPACES")
    sleep(100ms)

step [over]: key(f10)
step (in | into): key(f11)
step out: key(shift-f11)
play: key(f8)

break this:         key(ctrl-b)
break (yes | no): key(ctrl-f8)

break pause: key(ctrl-f8)
break resume:
    key(ctrl-f8)
    key(f8)
break (continue | run | play): key(f8)
break <number>:
    key(ctrl-g)
    "{number}"
    key(enter)
    sleep(100ms)
    key(ctrl-b)