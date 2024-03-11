from talon import Module, Context, actions, cron

mod = Module()
ctx = Context()

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
    "hiss: special",
    "shush: jump",
    "palate:  Q",
    "tut: reset y",
    "tut x2: alt",
    "tut x3: alt hold",
    "t: dash",
    "nn: E",
    "er: exit mode"
]

mod.mode("hi_fi_rush_parrot", "Parrot mode for hi_fi_rush game")

@ctx.action_class("user")
class Actions:
    def on_parrot_v5_mode_enable(ev: dict):
        global commands
        if ev["mode"] == "user.hi_fi_rush_parrot":
            actions.user.game_v2_canvas_box_color("222666")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "game")
            actions.user.game_v2_canvas_commands_enable()
            actions.user.game_v2_canvas_commands_update(commands_cheatsheet)
        elif ev["mode"] == "user.hi_fi_rush_nav_mode":
            actions.user.game_v2_canvas_box_color("FCD12A")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "nav")
        else:
            actions.user.game_v2_canvas_box_color("ff0000")
            actions.user.game_v2_canvas_status_enable()
            actions.user.game_v2_canvas_status_update("mode", "parrot global")
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

@ctx_parrot.action_class("user")
class Actions:
    def on_parrot_combo_stop(ev: dict):
        print("on_parrot_combo_stop", ev["combo"])
        if ev["combo"] == "tut":
            actions.user.game_v2_reset_center_y()
        elif ev["combo"] == "tut tut":
            actions.key("alt")
        elif ev["combo"] == "tut tut tut":
            actions.key("alt:down")