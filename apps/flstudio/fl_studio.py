from talon import Module, Context, actions, ctrl, app
from datetime import datetime
import time

mod = Module()
mod.tag("fl_studio_pan_mode", desc="Tag for fl studio pan mode")
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
modifiers = []

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

    def fl_view_mixer():
      """View mixer"""
      actions.key("f9")

    def fl_view_playlist():
      """View playlist"""
      actions.key("f5")

    def fl_view_channel():
      """View channel"""
      actions.key("f6")

    def fl_view_piano_roll():
      """View a piano roll"""
      actions.key("f7")

    def fl_view_window_next():
      """View next window"""
      actions.key("tab")

    def fl_view_window_last():
      """View last window"""
      actions.key("shift-tab")

    def fl_toggle_stretch():
      """Stretch toggle"""
      actions.key("shift-m")

    def fl_studio_pan_mode_disable():
      """Disable fl studio pan mode"""
      print("disable")
      ctx.tags = []

    def fl_studio_pan_mode_enable():
      """Enable fl studio pan mode"""
      print("enablean")
      ctx.tags = ["user.fl_studio_pan_mode"]

global noise

@ctx.action_class("user")
class UserActions:
  def virtual_region_one():
    """Virtual region one"""
    actions.user.fl_view_window_next()

  def virtual_region_two():
    """Virtual region two"""
    actions.user.fl_toggle_keys()

  def virtual_region_three():
    """Virtual region three"""
    actions.user.fl_view_window_last()

  def virtual_region_four():
    """Virtual region four"""
    actions.user.fl_toggle_bar()

  def virtual_region_five():
    """Virtual region five"""
    actions.user.fl_view_playlist()

  def virtual_region_six():
    """Virtual region six"""
    actions.user.fl_toggle_stretch()

  def virtual_region_seven():
    """Virtual region seven"""
    actions.user.fl_view_channel()

  def virtual_region_eight():
    """Virtual region eight"""
    actions.user.fl_view_mixer()

  def virtual_region_nine():
    """Virtual region nine"""
    actions.user.fl_view_piano_roll()
  # def on_cluck():
  #   """Do cluck"""
  #   global noise
  #   noise = "cluck"
  #   print("on_cluck from fl")
  #   # actions.user.hud_activate_virtual_key()
  #   actions.user.on_pop()
  #   actions.user.on_pop()

  # def on_tut():
  #   """Do on_tut"""
  #   global noise
  #   noise = "tut"
  #   print("on_tut")
  #   # actions.key("escape")

  # def on_palate():
  #   """Do on_palate"""
  #   actions.mouse_click(1)
  #   # actions.key("escape")

  # def on_eh():
  #   """Do on_eh"""
  #   global noise
  #   noise = "eh"
  #   print("on_eh")
  #   actions.user.hud_activate_virtual_key()

  # def on_oh():
  #   """Do on_oh"""
  #   global noise, modifiers
  #   noise = "oh"
  #   print("oh triggers ctrl")
  #   if "ctrl" not in modifiers:
  #     modifiers.append("ctrl")

  # def on_uh():
  #   """Do on_uh"""
  #   global noise, modifiers
  #   noise = "uh"
  #   print("uh triggers shift")
  #   if "shift" not in modifiers:
  #     modifiers.append("shift")

  # def on_ah():
  #   """Do on_ah"""
  #   global noise, modifiers
  #   noise = "ah"
  #   print("ah triggers alt")
  #   if "alt" not in modifiers:
  #     modifiers.append("alt")

  # def noise_shush_start():
  #     global modifiers
  #     print("on_shush_start from fl")
  #     print(modifiers)
  #     if "ctrl" in modifiers:
  #       print("ctrl-right start")
  #       actions.user.mouse_drag_new('ctrl')
  #       modifiers.clear()
  #     elif "shift" in modifiers:
  #       print("shift-right start")
  #       actions.user.mouse_drag_new('shift')
  #       modifiers.clear()
  #     elif "alt" in modifiers:
  #       print("alt-right start")
  #       actions.user.mouse_drag_new('alt')
  #       modifiers.clear()
  #     else:
  #       print("right start")
  #       actions.user.mouse_drag_new('right')

  # def noise_shush_stop():
  #     print("on_shush_stop from fl")
  #     actions.user.mouse_drag_end()

  # def noise_hiss_start():
  #     global modifiers
  #     print("on_hiss_start from fl")
  #     print(modifiers)
  #     if "ctrl" in modifiers:
  #       print("ctrl-right")
  #       actions.user.mouse_drag_new('ctrl')
  #       modifiers.clear()
  #     elif "shift" in modifiers:
  #       print("shift-right")
  #       actions.user.mouse_drag_new('shift')
  #       modifiers.clear()
  #     elif "alt" in modifiers:
  #       print("alt-right")
  #       actions.user.mouse_drag_new('alt')
  #       modifiers.clear()
  #     else:
  #       print("left start")
  #       actions.user.mouse_drag_new('left')
  #     # actions.user.noise_debounce("hiss", True)

  # def noise_hiss_stop():
  #     print("on_hiss_stop from fl")
  #     actions.user.mouse_drag_end()

  # def noise_ee_start():
  #   global modifiers
  #   print("on_ee_start from fl")
  #   for modifier in modifiers:
  #     actions.key(f"{modifier}:down")
  #   actions.user.mouse_scrolling("down")

  # def noise_ee_stop():
  #   global modifiers
  #   print("on_ee_stop from fl")
  #   actions.user.mouse_scroll_stop()
  #   for modifier in modifiers:
  #     actions.key(f"{modifier}:up")
  #   modifiers.clear()

  # def noise_oo_start():
  #   global modifiers
  #   print("on_oo_start from fl")
  #   for modifier in modifiers:
  #     actions.key(f"{modifier}:down")
  #   actions.user.mouse_scrolling("up")

  # def noise_oo_stop():
  #   global modifiers
  #   print("on_oo_stop from fl")
  #   actions.user.mouse_scroll_stop()
  #   for modifier in modifiers:
  #     actions.key(f"{modifier}:up")
  #   modifiers.clear()

# def register_regions():
#     keys = [
# 	    actions.user.hud_create_virtual_key(actions.user.fl_view_window_next, 'One'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_toggle_keys, 'Two'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_view_window_last, 'Three'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_toggle_bar, 'Four'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_view_playlist, 'Five'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_toggle_stretch, 'Six'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_view_channel, 'Seven'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_view_mixer, 'Eight'),
# 	    actions.user.hud_create_virtual_key(actions.user.fl_view_piano_roll, 'Nine')
# 	  ]
#     actions.user.hud_register_virtual_keyboard('fl_keyboard', keys)
#     actions.user.hud_set_virtual_keyboard('fl_keyboard')
#     actions.user.hud_set_virtual_keyboard_visibility(0)

# app.register('ready', register_regions)

# def on_app_switch(application):
#     if application.name == "fl studio":

#     else:


# ui.register("app_activate", on_app_switch)