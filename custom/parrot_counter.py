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
    actions.user.ui_elements_set_text("success", success)

def increment_error():
    global error
    error += 1
    actions.user.ui_elements_set_text("error", error)

def increment_soft_error():
    global soft_error
    soft_error += 1
    actions.user.ui_elements_set_text("soft_error", soft_error)

def decrement_success():
    global success
    success -= 1
    actions.user.ui_elements_set_text("success", success)

def decrement_error():
    global error
    error -= 1
    actions.user.ui_elements_set_text("error", error)

parrot_config = {
    "pop":        ("increment success", increment_success),
    "palate":     ("increment error", increment_error),
    "cluck":      ("increment soft error", increment_soft_error),
    "ah":         ("back", lambda: actions.key("left")) ,
    'shush:th_200':("play/pause", lambda: actions.key("space")),
    "er":         ("exit mode", actions.user.parrot_mode_counter_disable),
}

def show_ui():
    global builder, success, error, soft_error
    (screen, div, text, css) = actions.user.ui_elements(["screen", "div", "text", "css"])

    box_css = css(
        align_items="flex_start",
        flex_direction="column",
        gap=32,
        padding=16 ,
        background_color="000000AA"
     )

    (cmds, acts) = actions.user.parrot_config_format_display(parrot_config)

    builder = screen(align_items="center", justify_content="center")[
        div(**box_css)[
            div(flex_direction="row", gap=32)[
                text(f"{success}", id="success", color="green", font_size=36, font_weight="bold"),
                text(f"{error}", id="error", color="red", font_size=36, font_weight="bold"),
                text(f"{soft_error}", id="soft_error", color="87CEEB", font_size=36, font_weight="bold")
            ],
            div(flex_direction="row", gap=16)[
                div(gap=8)[
                    text("sound", font_weight="bold"),
                     *(text(command) for command in cmds)
                ],
                div(gap=8)[
                    text("action", font_weight="bold"),
                    *(text(action) for action in acts)
                ]
            ]
        ]
    ]

    builder.show()

def hide_ui():
    global builder
    builder.hide()

@mod.action_class
class Actions:
    def parrot_mode_counter_enable():
        """Enable the parrot counter mode"""
        global success, error, soft_error
        actions.mode.enable("user.parrot_counter")
        actions.mode.disable("command")
        success = 0
        error = 0
        soft_error = 0
        show_ui()

    def parrot_mode_counter_disable():
        """Enable the parrot counter mode"""
        actions.mode.disable("user.parrot_counter")
        actions.mode.enable("command")
        hide_ui()

@ctx.action_class("user")
class Actions :
    def parrot_config():
        return parrot_config
