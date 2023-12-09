from talon import actions, Context, Module

mod = Module()

mod.tag("fl_studio_phase_plant", desc="Phase plant")

ctx_phase_plant = Context()

ctx_phase_plant.matches = """
app: fl studio
tag: user.fl_studio_phase_plant
"""
