from talon import Module, Context, actions, ctrl

mod = Module()
mod.list("fl_instrument", desc="Instruments")
mod.list("fl_plugin", desc="Plugins")
mod.list("fl_slot_y_position", desc="Slot position")
mod.list("fl_mixer_x_position", desc="Mixer position")

ctx = Context()
ctx.matches = """
app: fl studio
os: windows
"""

ctx.lists["self.fl_instrument"] = {
  "addictive drums": "a",
  "addictive keys": "b",
  "analog lab": "c",
  "big kick": "d",
  "flex": "e",
  "kontakt": "f",
  "contact": "f",
  "phase plant": "g",
  "scaler": "h",
  "scaler two": "h",
  "serum": "i",
  "synth": "i",
  "sublab": "j",
  "vital": "k",
  "xo": "l",
  "labs": "m",
}

ctx.lists["self.fl_plugin"] = {
  "clip shifter": "clipshifter",
  "chain leader": "chain leader",
  "chain follower": "chain follower",
  "delay": "deelay",
  "decapitate or": "decap",
  "echo boy": "echoboy",
  "frequency shifter": "mfreq",
  "fruity eq": "fruity param",
  "fruity limiter": "fruity lim",
  "fruity balance": "fruity bal",
  "fruity send": "fruity send",
  "kick starter": "kickstart",
  "micro": "fin-micro",
  "fin micro": "fin-micro",
  "micro shift": "microshift",
  "morph eq": "morph eq",
  'oscilloscope': "oszi",
  "ozone image or": "ozone imager",
  "ozone image or two": "ozone imager",
  'ott': "ott",
  "neo verb": "neoverb",
  'patcher': "patcher",
  "pro c two": "pro-c",
  "pro q three": "pro-q",
  "pro l two": "pro-l",
  "pro mb": "pro-m",
  "rc twenty": "rc-20",
  "saturn two": "saturn",
  'saturn': "saturn",
  "shaper box": "shaperbox 3",
  "soothe two": "soothe",
  'soothe': "soothe",
  "tape stop": "tapestop",
  "transient shaper": "transient processor",
  "transient processor": "transient processor",
  'thu': "th-u",
  "valhalla delay": "valhalladelay",
  "valhalla room": "valhallaroom",
  "valhalla vintage": "valhallavintage",
  "valhalla supermassive": "valhallasupermassive",
  "vocal synth": "vocalsynth",
  'supermassive': "valhallasupermassive",
  'wider': "wider",
}

ctx.lists["self.fl_slot_y_position"] = {
  "one": "685",
  "two": "704",
  "three": "724",
  "four": "743",
  "five": "762",
  "six": "781",
  "seven": "800",
  "eight": "819",
  "nine": "839",
  "ten": "858",
}

ctx.lists["self.fl_mixer_x_position"] = {
  "one": "629",
  "two": "673",
  "three": "714",
  "four": "762",
  "five": "807",
  "six": "851",
  "seven": "892",
  "eight": "938",
  "nine": "983",
  "ten": "1027",
}

fl_bar_is_visible = True
mixer_y_pos = 693
slot_x_pos = 385
slot_triangle_menu_x_pos = 291
slot_light_toggle_x_pos = 491

@mod.action_class
class Actions:
    def fl_normalize():
      """normalized plus preferred settings"""
      x, y = ctrl.mouse_pos()
      actions.mouse_click(0)
      ctrl.mouse_move(x - 137, y - 11)
      actions.user.fl_set_declicking_mode()
      ctrl.mouse_move(x + 163, y - 108)
      actions.user.fl_set_resample_mode()
      ctrl.mouse_move(x, y)

    def fl_set_normalized_layout():
      """ """
      ctrl.mouse_move(156, 19)
      ctrl.mouse_click(0)
      actions.key("up:8 right up:2")
      actions.key("enter")

    def fl_set_declicking_mode():
      """ """
      ctrl.mouse_click(0)
      actions.key("down:2 enter")

    def fl_set_resample_mode():
      """ """
      ctrl.mouse_click(0)
      actions.key("down:2 enter")

    def fl_toggle_keys():
      """toggle keyboard"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(494, 60)
      ctrl.mouse_click(0)
      ctrl.mouse_move(*pos)

    def fl_toggle_bar():
      """toggle sidebar"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(130, 93)
      ctrl.mouse_click(1)
      actions.key("alt-f8")
      ctrl.mouse_move(*pos)

    def fl_click_slot(slot_y_position: str):
      """click a slot position"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(slot_x_pos, slot_y_position)
      ctrl.mouse_click(0)
      ctrl.mouse_move(*pos)

    def fl_click_slot_light(slot_y_position: str):
      """click a slot position"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(slot_light_toggle_x_pos, slot_y_position)
      ctrl.mouse_click(0)
      ctrl.mouse_move(*pos)

    def fl_click_slot_menu(slot_y_position: str):
      """click a slot position"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(slot_triangle_menu_x_pos, slot_y_position)
      ctrl.mouse_click(0)

    def fl_move_mouse_to_slot(slot_y_position: str):
      """click a slot position"""
      pos = ctrl.mouse_pos()
      ctrl.mouse_move(slot_x_pos, slot_y_position)

    def fl_choose_plugin(plugin: str):
      """choose a plugin"""
      ctrl.mouse_click(1)
      actions.sleep("100ms")
      actions.insert(plugin)
      actions.key("enter")

    def fl_go_to_mixer_start():
      """go to the beginning of the mixer"""
      ctrl.mouse_move(1087, 692)
      ctrl.mouse_scroll(-4000)

    def fl_click_mixer(mixer_x_position: str):
      """go to the beginning of the mixer"""
      ctrl.mouse_move(mixer_x_position, mixer_y_pos)
      ctrl.mouse_click(0)
