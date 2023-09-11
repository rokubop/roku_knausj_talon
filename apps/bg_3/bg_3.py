from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.bg_3 = r"""
os: windows
and app.exe: bg3_dx11.exe
"""
mod.tag("parrot_bg_cam_movement", desc="Tag for enabling parrot_bg_cam_movement")
mod.tag("bg_zoom_tag", desc="Tag for enabling bg_zoom_tag")
ctx.matches = r"""
os: windows
app: bg_3
"""

@mod.action_class
class Actions:
    def enable_parrot_bg_cam_movement():
        """Activate camera movement"""
        actions.user.add_green_cursor()
        ctx.tags = ["user.parrot_bg_cam_movement"]

    def disable_parrot_bg_cam_movement():
        """Deactivate camera movement"""
        actions.user.clear_screen_regions()
        actions.user.add_red_cursor()
        # actions.user.parrot_mode_disable()
        ctx.tags = []

    def bg_zoom_tag_disable():
        """Disable zoom tag"""
        print("Disable zoom tag")
        actions.user.add_green_cursor()
        ctx.tags = ["user.parrot_bg_cam_movement"]

    def bg_zoom_tag_enable():
        """Enable zoom tag"""
        print("Enable zoom tag")
        actions.user.add_color_cursor('006666')
        ctx.tags = ["user.bg_zoom_tag"]
