from talon import Module, Context, imgui, ui
from itertools import islice
import re

mod = Module()
ctx = Context()

def get_app_name(text: str, max_len=20) -> str:
    pattern = re.compile(r"[A-Z][a-z]*|[a-z]+|\d")
    return "_".join(
        list(islice(pattern.findall(text.replace(".exe", "")), max_len))
    ).lower()

@imgui.open(y=0)
def gui_x(gui: imgui.GUI):
    gui.text("Game v2")
    gui.line()

    # gui.spacer()
    # game_folder = get_current_game_folder():
    #     gui.text(app_name)

    gui.text("Commands you can say:")
    gui.line()
    gui.text("* Game create files (Creates a talon and python file for the currently focused game)")
    gui.text("* Game customize (Open the game's talon file)")

    # gui.spacer()
    gui.text("* Game calibrate x <number> (e.g 4000. For calibrating a 360 degree turn)")
    gui.text("* Game calibrate y <number> (e.g 1000. For calibrating ground to center of screen)")
    gui.spacer()
    if gui.button("Game help close"):
        gui_x.hide()

@mod.action_class
class Actions:
    def game_v2_help_show():
        """Show help menu"""
        gui_x.show()

    def game_v2_help_close():
        """Close the game help menu"""
        gui_x.hide()
