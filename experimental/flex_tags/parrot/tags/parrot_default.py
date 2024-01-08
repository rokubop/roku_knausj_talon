# from talon import Module, Context, actions, ctrl, cron, settings

# mod = Module()
# ctx = Context()

# mod.mode("parrot_default_v2", desc="Tag for default parrot mode v2")

# ctx.matches = """
# mode: user.parrot_default_v2
# """

# @ctx.action_class("user")
# class Actions:
#     def on_mode_enable(tag: str):
#         actions.user.add_color_cursor("f22160")

#     def on_mode_disable(tag: str):
#         actions.user.clear_screen_regions()
