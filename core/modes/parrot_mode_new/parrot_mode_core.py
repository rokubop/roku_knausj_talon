from talon import Context, Module, actions

mod = Module()
ctx = Context()

logging_enabled = True

def log(msg: str):
    if logging_enabled:
        print(f"tag: {', '.join(ctx.tags)}, parrot: {msg}")

@mod.action_class
class ParrotMode:

    def parrot_mode_enable():
        """Enable parrot mode"""
        print("parrot mode enabled")
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        actions.mode.enable("user.parrot")
        ctx.tags = ["user.parrot_mode_default"]
        print(ctx.tags)
        actions.mode.disable("command")
        actions.mode.disable("dictation")

    def parrot_mode_disable():
        """Disable parrot mode"""
        print('parrot mode disabled')
        actions.user.parrot_scroll_stop_soft()
        actions.user.parrot_mouse_and_scroll_stop()
        actions.user.clear_screen_regions()
        actions.user.mouse_scroll_stop()
        ctx.tags = []
        actions.mode.disable("user.parrot")
        actions.mode.enable("command")
        actions.mode.disable("dictation")

    def parrot_mode_enable_tag(tag: str):
        """Enable parrot mode with tag"""
        print(f'enabling {tag}')
        ctx.tags = [tag]

    def parrot_mode_reset_tags():
        """Enable parrot mode reset tags"""
        ctx.tags = ["user.parrot_mode_default"]


@mod.action_class
class ParrotModeCommands:
    """Commands with fixed behaviors and logging. Shouldn't be overridden."""
    def parrot_mode_pop(): """Parrot mode pop - Do not reimplement"""; log('pop'); actions.user.parrot_pop()
    def parrot_mode_cluck(): """Parrot mode cluck - Do not reimplement"""; log('cluck'); actions.user.parrot_cluck()
    def parrot_mode_palate(): """Parrot mode palate - Do not reimplement"""; log('palate'); actions.user.parrot_palate()
    def parrot_mode_ah(): """Parrot mode ah - Do not reimplement"""; log('ah'); actions.user.parrot_ah()
    def parrot_mode_oh(): """Parrot mode oh - Do not reimplement"""; log('oh'); actions.user.parrot_oh()
    def parrot_mode_ee(): """Parrot mode ee - Do not reimplement"""; log('ee'); actions.user.parrot_ee()
    def parrot_mode_eh(): """Parrot mode eh - Do not reimplement"""; log('eh'); actions.user.parrot_eh()
    def parrot_mode_er(): """Parrot mode er - Do not reimplement"""; log('er'); actions.user.parrot_er()
    def parrot_mode_guh(): """Parrot mode guh - Do not reimplement"""; log('guh'); actions.user.parrot_guh()
    def parrot_mode_nn(): """Parrot mode nn - Do not reimplement"""; log('nn'); actions.user.parrot_nn()
    def parrot_mode_t(): """Parrot mode t - Do not reimplement"""; log('t'); actions.user.parrot_t()
    def parrot_mode_tut(): """Parrot mode tut - Do not reimplement"""; log('tut'); actions.user.parrot_tut()
    def parrot_mode_hiss(): """Parrot mode hiss - Do not reimplement"""; log('hiss'); actions.user.parrot_hiss()
    def parrot_mode_shush(): """Parrot mode shush - Do not reimplement"""; log('shush'); actions.user.parrot_shush()
    def parrot_mode_hiss_stop(): """Parrot mode hiss stop - Do not reimplement"""; log('hiss:stop'); actions.user.parrot_hiss_stop()
    def parrot_mode_shush_stop(): """Parrot mode shush stop - Do not reimplement"""; log('shush:stop'); actions.user.parrot_shush_stop()

@mod.action_class
class ParrotCommands:
    """Dynamic commands that can be changed based on context."""
    def parrot_pop(): """Parrot pop implementation"""; print("parrot_pop not implemented"); pass
    def parrot_cluck(): """Parrot cluck implementation"""; print("parrot_cluck not implemented"); pass
    def parrot_palate(): """Parrot palate implementation"""; print("parrot_palate not implemented"); pass
    def parrot_ah(): """Parrot ah implementation"""; print("parrot_ah not implemented"); pass
    def parrot_oh(): """Parrot oh implementation"""; print("parrot_oh not implemented"); pass
    def parrot_ee(): """Parrot ee implementation"""; print("parrot_ee not implemented"); pass
    def parrot_eh(): """Parrot eh implementation"""; print("parrot_eh not implemented"); pass
    def parrot_er(): """Parrot er implementation"""; print("parrot_er not implemented"); pass
    def parrot_guh(): """Parrot guh implementation"""; print("parrot_guh not implemented"); pass
    def parrot_nn(): """Parrot nn implementation"""; print("parrot_nn not implemented"); pass
    def parrot_t(): """Parrot t implementation"""; print("parrot_t not implemented"); pass
    def parrot_tut(): """Parrot tut implementation"""; print("parrot_tut not implemented"); pass
    def parrot_hiss(): """Parrot hiss implementation"""; print("parrot_hiss not implemented"); pass
    def parrot_shush(): """Parrot shush implementation"""; print("parrot_shush not implemented"); pass
    def parrot_hiss_stop(): """Parrot hiss stop implementation"""; print("parrot_hiss_stop not implemented"); pass
    def parrot_shush_stop(): """Parrot shush stop implementation"""; print("parrot_shush_stop not implemented"); pass