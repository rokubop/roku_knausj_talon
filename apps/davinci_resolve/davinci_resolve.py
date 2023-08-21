from talon import Module, Context, ctrl

mod = Module()
mod.list("davinci_mouse_location", desc="Mouse locations")

mod.apps.davinci_resolve = """
os: windows
and app.app: davinci resolve
"""

ctx = Context()
ctx.matches = """
os: windows
app.app: davinci resolve
"""

ctx.lists["self.davinci_mouse_location"] = {
  "edit": "845,1013",
  "fusion": "963,1014",
  "color": "1081,1011",
  "render": "1322,1013",
  "cut": "720,1013",
  "effects":"226,63",
  "pool": "118,58",
  "media": "118,58",
}

@mod.action_class
class Actions:
    def davinci_click_position(position: str):
      """click a mouse location and return to original position"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(*position.split(","))
      ctrl.mouse_click()
      ctrl.mouse_move(*pos)