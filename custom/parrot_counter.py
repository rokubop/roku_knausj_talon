from talon import Context, actions, Module

mod = Module()
mod.mode("parrot_counter", "Counter parrot mode")

ctx = Context(  )
ctx.matches = r"""
os: windows
mode: user.parrot_counter
"""

builder = None
success = 0
error = 0
soft_error = 0

def increment_success():
    global success
    success += 1
    hide_ui()
    show_ui()

def increment_error():
    global error
    error += 1
    hide_ui()
    show_ui()

def increment_soft_error():
    global soft_error
    soft_error += 1
    hide_ui()
    show_ui()

def decrement_success():
    global success
    success -= 1
    hide_ui()
    show_ui()

def decrement_error():
    global error
    error -= 1
    hide_ui()
    show_ui()

parrot_config = {
    "pop":        ("increment success", increment_success),
    "palate":     ("increment error", increment_error),
    "cluck":      ("increment soft error", increment_soft_error),
    "ah":         ("back", actions.key("left")) ,
    'shush:th_200':("play/pause", actions.key("space")),
    "er":      ("exit mode", actions.user.parrot_mode_counter_disable),
}

def show_ui():
    global builder, success, error, soft_error
    builder = actions.user.ui_html_builder_screen(
        id="parrot_commands",
    )
    box = builder.add_div(
        align_items="flex_start",
        flex_direction="column",
        gap=32,
        padding=16 ,
        background_color="000000AA"  )
    counter = box.add_div(flex_direction="row", gap= 32)
    counter.add_text(f"{success}", color="green", size=36, font_weight="bold")
    counter.add_text(f"{error}", color="red", size=36, font_weight="bold")
    counter.add_text(f"{soft_error}", color="87CEEB", size=36, font_weight="bold")

    commands = box.add_div(flex_direction="row", gap=16)
    command_column = commands.add_div(gap=8)
    command_column.add_text("sound", font_weight="bold")
    for command, (action, _) in parrot_config.items():
        command_column.add_text(command)
    actions_column = commands.add_div(gap=8)
    actions_column.add_text("action", font_weight="bold")
    for command, (action, _) in parrot_config.items():
        actions_column.add_text(action)

    builder.show()

def hide_ui():
    global builder
    builder.hide()

@mod.action_class
class Actions:
    def parrot_mode_counter_enable() :
        """Enable the parrot counter mode"""
        global success, error, soft_error
        actions.mode.enable("user.parrot_counter")
        actions.mode.disable("command")
        success = 0
        error = 0
        soft_error = 0
        show_ui(  )

    def parrot_mode_counter_disable():
        """Enable the parrot counter mode"""
        actions.mode.disable("user.parrot_counter")
        actions.mode.enable("command")
        hide_ui()



@ctx.action_class("user")
class Actions:
    def parrot_config():
        return parrot_config
