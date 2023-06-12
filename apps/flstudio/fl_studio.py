from talon import Module, Context

mod = Module()
mod.list("fl_instrument", desc="Instruments")
mod.list("fl_plugin", desc="Plugins")

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

# ctx.lists["self.timing"] = {
#   "one": 1000,
#   "two": 2000,
#   "three": 3000,
#   "four": 4000,
#   "five": 5000,
#   "six": 6000,
#   "seven": 7000,
#   "eight": 8000,
#   "nine": 9000,
#   "ten": 10000,
# }
