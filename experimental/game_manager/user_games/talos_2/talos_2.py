from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.talos_2 = r"""
os: windows
and app.exe: Talos2-Win64-Shipping.exe
"""

ctx.matches = r"""
os: windows
app: talos_2
"""

mod.mode("game_talos_2_parrot", "Parrot mode for talos 2 game")

@mod.action_class
class Actions:
    def game_v2_talos_2_game_parrot_mode_enable():
        """Enter game mode"""
        actions.mode.disable("command")
        actions.mode.enable("user.game_talos_2_parrot")
        actions.user.game_v2_canvas_status_enable()
        actions.user.game_v2_canvas_status_update("mode", "game")

    def game_v2_talos_2_game_parrot_mode_disable():
        """Enter game mode"""
        actions.mode.disable("user.game_talos_2_parrot")
        actions.user.game_v2_canvas_status_disable()
        actions.mode.enable("command")

@ctx.action_class("user")
class Actions:
    def parrot_mode_on_enable():
        print("hello world disk")
        actions.user.game_v2_canvas_status_enable()
        actions.user.game_v2_canvas_status_update("mode", "parrot global")

    def parrot_mode_on_disable():
        actions.user.game_v2_canvas_status_disable()
