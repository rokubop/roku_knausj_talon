win.title: /DevTools/
mode: command
-

<user.teleport> [<user.text>]:
    key("ctrl-p")
    sleep(400ms)
    "{text}"
    sleep(100ms)

(step | next): key(f10)
[step] (in | into): key(f11)
[step] out: key(shift-f11)
play: key(f8)
