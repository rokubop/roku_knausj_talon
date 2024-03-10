from talon import Module, Context, actions
mod = Module()
ctx = Context()

mod.apps.canofwormholes = r"""
os: windows
and app.exe: canofwormholes.exe
"""

ctx.matches = r"""
os: windows
app: canofwormholes
"""

mod.mode("game_canofwormholes_parrot", "Parrot mode for talos 2 game")
mod.tag("game_canofwormholes_nav_discrete", "Nav discrete mode")
ctx_nav_discrete = Context()
ctx_nav_discrete.matches = r"""
app: canofwormholes
mode: user.game_canofwormholes_parrot
tag: user.game_canofwormholes_nav_discrete
"""

@mod.action_class
class Actions:
    def game_v2_canofwormholes_game_parrot_mode_enable():
        """Enter game mode"""
        actions.mode.disable("command")
        actions.mode.enable("user.game_canofwormholes_parrot")
        actions.user.game_v2_canvas_box_color("222666")
        actions.user.game_v2_canvas_status_enable()
        actions.user.game_v2_canvas_status_update("mode", "game")

    def game_v2_canofwormholes_game_parrot_mode_disable():
        """Enter game mode"""
        actions.user.event_mouse_move_stop_hard()
        actions.user.game_v2_stop_all()
        actions.mode.disable("user.game_canofwormholes_parrot")
        actions.user.game_v2_canvas_status_disable()
        actions.mode.enable("command")

    def game_v2_canofwormholes_nav_discrete_toggle():
        """Toggle nav discrete mode"""
        tags = set(ctx.tags)

        if "user.game_canofwormholes_nav_discrete" in tags:
            tags.remove("user.game_canofwormholes_nav_discrete")
        else:
            tags.add("user.game_canofwormholes_nav_discrete")

        ctx.tags = list(tags)

@ctx.action_class("user")
class Actions:
    def on_parrot_v5_mode_enable(ev: dict):
        actions.user.game_v2_canvas_box_color("ff0000")
        actions.user.game_v2_canvas_status_enable()
        actions.user.game_v2_canvas_status_update("mode", "parrot global")
        actions.next(ev)

    def on_parrot_v5_mode_disable(ev: dict):
        actions.user.game_v2_canvas_status_disable()
        actions.next(ev)

    def on_head_left_trigger():
        print("on_head_left_trigger")
        actions.user.game_v2_move_dir_spam("a")

    def on_head_right_trigger():
        actions.user.game_v2_move_dir_spam("d")

    def on_head_down_trigger():
        actions.user.game_v2_move_dir_spam("s")

    def on_head_up_trigger():
        actions.user.game_v2_move_dir_spam("w")

    def on_head_center_trigger():
        actions.user.game_v2_stop_all()
