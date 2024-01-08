from talon import Module, Context, actions

mod = Module()

@mod.action_class
class Actions:
    def use_tag(ctx: Context, tag: str):
        """Use tag"""
        actions.user.on_tag_disabled()
        ctx.tags = [tag]
        actions.user.on_tag_enabled()

    def on_tag_enabled():
        """Triggered when a tag is enabled"""
        pass

    def on_tag_disabled():
        """Triggered when a tag is disabled"""
        pass
