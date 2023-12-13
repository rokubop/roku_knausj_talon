from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.tag("parrot_browser", desc="Tag for browser parrot mode")
ctx.matches = """
tag: user.parrot_browser
and mode: user.parrot
"""

@ctx.action_class("user")
class ParrotCommands:
    def parrot_ah(): actions.browser.go_back()
    def parrot_oh(): actions.browser.go_forward()
    def parrot_tut(): actions.app.tab_close()
    def parrot_guh(): actions.key("enter")
