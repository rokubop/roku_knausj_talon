app: card_survival_tropical_island
-
settings():
    # key_hold = 64.0
    # key_wait = 16.0
    user.mouse_hold = 16000
    user.mouse_wait = 0

craft | blue:               key(b)
rest | sleep:               key(t)
stats:                      key(d)
hurt | injury | injuries:   key(h)
me | character | car:       key(c)
journal:                    key(j)
help:
    key(j)
    sleep(100ms)
    mouse_move(1633, 59)
    mouse_click(0)
    sleep(100ms)
    mouse_move(1414, 225)
    mouse_click(0)
next:
    mouse_move(1716, 952)
    mouse_click(0)
back:
    mouse_move(574, 951)
    mouse_click(0)
hunt | bow:
    mouse_move(832, 127)
    mouse_click(0)
shirt | dress:
    mouse_move(1010, 128)
    mouse_click(0)
home | base | house:
    mouse_move(490, 125)
    mouse_click(0)
tools | tool:
    mouse_move(658, 123)
    mouse_click(0)
cook | meal | dish:
    mouse_move(1351, 128)
    mouse_click(0)
health:
    mouse_move(1525, 128)
    mouse_click(0)
hat | farm:
    mouse_move(1696, 118)
    mouse_click(0)
burn | roast:
    mouse_move(1178, 121)
    mouse_click(0)
