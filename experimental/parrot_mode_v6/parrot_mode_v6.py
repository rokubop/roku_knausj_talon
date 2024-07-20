# from talon import Module, Context, actions

# mod = Module()
# mod.mode("parrot_v6", "parrot mode v6")

# ctx = Context()
# ctx.matches = r"""
# mode: user.parrot_v6
# """

# parrot_config = {
#     "pop": ("click", lambda: actions.mouse_click(0)),
#     "ah": ("hello", lambda: actions.insert("hello")),
#     "nn": ("ax", actions.user.fluent_search_show_labels_window),
#     "er": ("exit mode", actions.user.parrot_mode_v6_disable),
# }

# @ctx.action_class("user")
# class Actions:
#     def parrot_config():
#         return parrot_config

# builder = None

# @mod.action_class
# class Actions:
#     def parrot_mode_v6_enable():
#         """Enable parrot mode v6"""
#         global builder
#         actions.mode.enable("user.parrot_v6")
#         actions.mode.disable("command")
#         builder = actions.user.ui_elements_screen(id="parrot_mode_v6")
#         box = builder.add_div()
#         box.add_text("Parrot Mode V6")
#         builder.show()

#     def parrot_mode_v6_disable():
#         """Disable parrot mode v6"""
#         global builder
#         actions.mode.disable("user.parrot_v6")
#         actions.mode.enable("command")
#         builder.hide()
