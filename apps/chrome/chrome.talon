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
    insert("{text}")
    key(enter)

# roku

(light | dark) mode: key(alt-shift-d)