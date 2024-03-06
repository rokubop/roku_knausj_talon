from talon import Module, Context, actions

mod = Module()
mod.tag("parrot_v5_tag_spots", desc="Parrot V5 tag spots")
# ctx = Context()
# ctx.matches = """
# mode: user.parrot_v5
# and mode: user.parrot_v5_default
# and tag: user.parrot_v5_tag_spots
# """

# @ctx.action_class("user")
# class Actions:
#     def on_parrot_v5_tag_enable():
#         actions.user.hud_add_log('success', '<*Note:/> Spots enabled')

#     def on_parrot_v5_tag_disable():
#         actions.user.hud_add_log('error', '<*Note:/> Mod enabled')
