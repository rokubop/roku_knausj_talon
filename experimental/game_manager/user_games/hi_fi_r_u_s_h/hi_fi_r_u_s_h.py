from talon import Module, Context, actions, cron

mod = Module()
ctx = Context()

mod.mode("hi_fi_rush_parrot", "Parrot mode for hi_fi_rush game")
mod.mode("hi_fi_rush_peppermint", "Peppermint mode for hi_fi_rush game")

mod.apps.hi_fi_rush = r"""
os: windows
and app.exe: Hi-Fi-RUSH.exe
"""

ctx.matches = r"""
os: windows
app: hi_fi_rush
"""

commands_cheatsheet = [
    "ah: left",
    "eh: forward",
    "oh: right",
    "guh: back",
    "pop: left click",
    "cluck: right click",
    "t: dash",
    "nn: E",
    "hiss: special",
    "shush: jump",
    "palate:  Q",
    "tut: reset y",
    "tut x2: alt",
    "tut x3: alt hold",
    "tut pop: left hold",
    "tut shush: jump hold",
    "tut palate: Q hold",
    "tut er: look mode",
    "tut hiss: toggle spam",
    "er: exit mode"
]

peppermint_cheatsheet = [
    "ah: left",
    "oh: right",
    "hiss: down",
    "shush: up",
    "pop: shoot",
    "er: shoot",
    "cluck: shoot",
    "guh: faster",
    "t: slower",
    "ee: stop",
]

look_cheatsheet = [
    "ah: left",
    "oh: right",
    "hiss: down",
    "shush: up",
    "pop: click + game",
    "er: game mode",
    "cluck: exit",
    "guh: faster",
    "t: slower",
    "ee: stop",
]

menu_cheatsheet = [
    "nn: click",
    "pop: click + exit",
    "hiss: scroll down",
    "shush: scroll up",
    "ah: hold left",
    "oh: right click",
    "eh: teleport",
    "er: look mode",
    "cluck: exit",
    "guh: ctrl",
    "t: shift",
    "tut: alt",
    "palate: repeat",
    "ee: stop",
]

spam = False

def show_default_game_commands():
    actions.user.game_v2_canvas_commands_enable()
    cheatsheet =[]
    for command in commands_cheatsheet:
        if spam and "hiss: special" in command:
            cheatsheet.append("hiss: spam")
        else:
            cheatsheet.append(command)
    actions.user.game_v2_canvas_commands_update(cheatsheet)


@ctx.action_class("user")
class Actions:
    def on_parrot_v5_mode_enable(ev: dict):
        global commands
        if ev["mode"] == "user.hi_fi_rush_parrot":
            actions.user.game_v2_canvas_box_color("222666")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "game")
            show_default_game_commands()
        elif ev["mode"] == "user.hi_fi_rush_nav_mode":
            actions.user.game_v2_canvas_box_color("FCD12A")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "nav")
        elif ev["mode"] == "user.rpg_mouse":
            actions.user.game_v2_canvas_box_color("FCD12A")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "look")
            actions.user.game_v2_canvas_commands_enable()
            actions.user.game_v2_canvas_commands_update(look_cheatsheet)
        elif ev["mode"] == "user.hi_fi_rush_peppermint":
            actions.user.game_v2_canvas_box_color("45f248")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "peppermint")
            actions.user.game_v2_canvas_commands_enable()
            actions.user.game_v2_canvas_commands_update(peppermint_cheatsheet)
        else:
            actions.user.game_v2_canvas_box_color("ff0000")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "parrot global")
            actions.user.game_v2_canvas_commands_enable()
            actions.user.game_v2_canvas_commands_update(menu_cheatsheet)
        actions.next(ev)

    def on_parrot_v5_mode_disable(ev: dict):
        actions.user.event_mouse_move_stop_hard()
        actions.user.game_v2_stop_all()
        actions.user.game_v2_canvas_hide()
        actions.next(ev)

ctx_parrot = Context()
ctx_parrot.matches = r"""
app: hi_fi_rush
and mode: user.parrot_v5
and mode: user.hi_fi_rush_parrot
"""
ctx_parrot.settings = {
    "user.game_v2_calibrate_x_360" : 2139,
    "user.game_v2_calibrate_y_ground_to_center" : 542
}

user = actions.user
key = actions.key

def toggle_spam():
    global spam
    spam = not spam
    show_default_game_commands()

def peppermint_mode():
    key("alt:down"),
    user.parrot_v5_mode_enable("user.hi_fi_rush_peppermint")

def rpg_mode():
    user.parrot_v5_mode_enable("user.rpg_mouse")

parrot_commands = {
    "eh":         ('forward', user.game_v2_move_dir_w),
    "guh":        ("back", user.game_v2_move_dir_s),
    "ah":         ("left", user.game_v2_move_dir_a),
    "oh":         ("right", user.game_v2_move_dir_d),
    'ee':         ("stop", user.game_v2_stop_layer_by_layer),
    "pop":        ("L click", lambda: user.event_mouse_click(0)),
    "cluck":      ("R click", lambda: user.event_mouse_click(1)),
    "nn":         ("E", lambda: key("e")),
    "palate":     ("Q", lambda: key("q")),
    "t":          ("shift", lambda: key("shift")),
    "hiss":       ("R", lambda: key("r") if not spam else key("space")),
    "shush":      ("space", lambda: key("space")),
    "er":         ("exit", user.parrot_v5_mode_disable),
    "tut":        ("reset y", user.game_v2_reset_center_y),
    "tut er":     ("look mode", rpg_mode),
    "tut ah":     ("turn left", lambda: user.game_v2_turn_left(90, 300)),
    "tut oh":     ("turn right", lambda: user.game_v2_turn_right(90, 300)),
    "tut guh":    ("turn around", user.game_v2_snap_180),
    "tut hiss":   ("toggle spam", toggle_spam),
    "tut pop":    ("L click hold", lambda: user.event_mouse_drag(0)),
    "tut shush":  ("space hold", lambda: key("space:down")),
    "tut palate": ("Q hold", lambda: key("q:down")),
    "tut tut":    ("alt", lambda: key("alt")),
    "tut tut tut":("alt hold", peppermint_mode),
}

parrot_config = {
    "mode": "game",
    "color": "222666",
    "commands" : parrot_commands
}

@ctx_parrot.action_class("user")
class Actions:
    def parrot_config():
        return parrot_config