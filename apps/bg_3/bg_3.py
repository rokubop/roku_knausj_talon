from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.bg_3 = r"""
os: windows
and app.exe: bg3_dx11.exe
"""


mod.tag("parrot_fly", desc="Tag for enabling parrot_bg_cam_movement")
ctx.matches = r"""
os: windows
app: bg_3
"""

is_highlighted = False

@mod.action_class
class Actions:
    def parrot_mode_bg_fly_enable():
        """Activate camera movement"""
        actions.user.parrot_mode_enable()
        actions.user.add_green_cursor()
        ctx.tags = ["user.parrot_fly"]

    def parrot_mode_bg_fly_disable():
        """Deactivate camera movement"""
        actions.user.release_dir_keys_all()
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        # actions.user.parrot_mode_disable()
        ctx.tags = []

    def parrot_mode_bg_fly_toggle():
        """Toggle camera movement"""
        if "user.parrot_fly" in ctx.tags:
            actions.user.parrot_mode_bg_fly_disable()
        else:
            actions.user.parrot_mode_bg_fly_enable()

    def bg_toggle_highlight():
        """Toggle highlight mode"""
        global is_highlighted
        if is_highlighted:
            actions.key("alt:up")
            is_highlighted = False
        else:
            actions.key("alt:down")
            is_highlighted = True
