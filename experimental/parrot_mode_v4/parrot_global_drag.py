from talon import Context, Module, actions, ctrl

mod = Module()
mod.tag("parrot_v4_global_dragging", desc="Global dragging")
ctx = Context()
ctx.matches = """
mode: user.parrot_v4_global
tag: user.parrot_v4_global_dragging
"""

ctx.settings = {
    "user.parrot_v4_show_cursor_color": True,
    "user.parrot_v4_cursor_color": "0000FF",
}

dragging = False

@mod.action_class
class Tags:
    def parrot_v4_global_tag_drag_enable():
        """Enable drag mode"""
        global dragging
        dragging = True
        ctrl.mouse_click(button=0, down=True)
        actions.user.parrot_v4_global_tag_enable("user.parrot_v4_global_dragging")

    def parrot_v4_global_tag_drag_disable():
        """Disable drag mode"""
        global dragging
        dragging = False
        ctrl.mouse_click(button=0, up=True)
        actions.user.parrot_v4_global_tag_disable("user.parrot_v4_global_dragging")


@ctx.action_class("user")
class Overrides:
    def parrot_v4_mouse_click(button: int = 0, hold: int = 16000):
        actions.user.parrot_v4_global_tag_drag_disable()

@ctx.action_class("user")
class Events:
    def parrot_v4_on_stopper():
        print("hello from the stopper modifier")
        if dragging:
            actions.user.parrot_v4_global_tag_drag_disable()
            actions.next()