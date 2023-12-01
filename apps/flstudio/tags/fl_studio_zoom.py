from talon import actions, Context, Module

mod = Module()

# zoom
mod.tag("fl_studio_zoom", desc="zoom mode")

ctx_zoom = Context()
ctx_zoom_parrot = Context()

ctx_zoom.matches = """
app: fl studio
tag: user.fl_studio_zoom
os: windows
"""

ctx_zoom_parrot.matches = """
app: fl studio
tag: user.fl_studio_zoom
mode: user.parrot
os: windows
"""

@mod.action_class
class Actions:
    def fl_zoom_in_x_start():
        """Start zooming in horizontally"""
        actions.user.pause_eye_tracking()
        actions.key("ctrl:down")
        actions.user.mouse_scrolling("up")

    def fl_zoom_out_x_start():
        """Stop zooming out horizontally"""
        actions.user.pause_eye_tracking()
        actions.key("ctrl:down")
        actions.user.mouse_scrolling("down")

    def fl_zoom_x_stop():
        """Stop zooming in horizontally"""
        actions.user.mouse_scroll_stop()
        actions.key("ctrl:up")

@ctx_zoom.action_class("user")
class Actions:
    def pedal_left_down():    actions.user.fl_zoom_in_x_start()
    def pedal_left_up():      actions.user.fl_zoom_x_stop()
    def pedal_center_down():  actions.user.fl_zoom_out_x_start()
    def pedal_center_up():    actions.user.fl_zoom_x_stop()

@ctx_zoom_parrot.action_class("user")
class Actions:
    def parrot_hiss():        actions.user.fl_zoom_in_x_start()
    def parrot_hiss_stop():   actions.user.fl_zoom_x_stop()
    def parrot_shush():       actions.user.fl_zoom_out_x_start()
    def parrot_shush_stop():  actions.user.fl_zoom_x_stop()


# scroll
mod.tag("fl_studio_scroll", desc="scroll mode")

ctx_scroll = Context()
ctx_scroll_parrot = Context()

ctx_scroll.matches = """
app: fl studio
tag: user.fl_studio_scroll
os: windows
"""

ctx_scroll_parrot.matches = """
app: fl studio
tag: user.fl_studio_scroll
mode: user.parrot
os: windows
"""

@mod.action_class
class Actions:
    def fl_scroll_up():
        """Start scrolling"""
        actions.user.pause_eye_tracking()
        actions.user.mouse_scrolling("up")

    def fl_scroll_down():
        """Stop scrolling"""
        actions.user.pause_eye_tracking()
        actions.user.mouse_scrolling("down")

    def fl_scroll_stop():
        """Stop scrolling"""
        actions.user.mouse_scroll_stop()

@ctx_scroll.action_class("user")
class Actions:
    def pedal_left_down():    actions.user.fl_scroll_up()
    def pedal_left_up():      actions.user.fl_scroll_stop()
    def pedal_center_down():  actions.user.fl_scroll_down()
    def pedal_center_up():    actions.user.fl_scroll_stop()

@ctx_scroll_parrot.action_class("user")
class Actions:
    def parrot_hiss():        actions.user.fl_scroll_down()
    def parrot_hiss_stop():   actions.user.fl_scroll_stop()
    def parrot_shush():       actions.user.fl_scroll_up()
    def parrot_shush_stop():  actions.user.fl_scroll_stop()