from talon import Context, Module, actions

mod = Module()
mod.tag("parrot_v4_global_positioner", desc="Global positioner")
ctx = Context()

ctx.matches = """
mode: user.parrot_v4_global
tag: user.parrot_v4_global_positioner
"""

ctx.settings = {
    "user.parrot_v4_show_cursor_color": True,
    "user.parrot_v4_cursor_color": "00FF00",
}

def teleport_and_head_track():
    actions.tracking.control_head_toggle(False)
    actions.tracking.control_gaze_toggle(True)
    actions.sleep("50ms")
    actions.tracking.control_gaze_toggle(False)
    actions.tracking.control_head_toggle(True)

def freeze():
    actions.tracking.control_gaze_toggle(False)
    actions.tracking.control_head_toggle(False)

@mod.action_class
class Actions:
    def parrot_v4_global_tag_positioner_enable():
        """Positioner enable"""
        teleport_and_head_track()
        actions.user.parrot_v4_global_tag_enable("user.parrot_v4_global_positioner")

    def parrot_v4_global_tag_positioner_disable():
        """Positioner disabled"""
        freeze()
        actions.user.parrot_v4_global_tag_disable("user.parrot_v4_global_positioner")

@ctx.action_class("user")
class Actions:
    def parrot_v4_on_before_mouse_click():
        actions.user.parrot_v4_global_tag_positioner_disable()
        # actions.next()

    def parrot_v4_on_before_mouse_scroll():
        actions.user.parrot_v4_global_tag_positioner_disable()
        # actions.next()

    def parrot_v4_on_stopper():
        actions.user.parrot_v4_global_tag_positioner_disable()
        # actions.next()