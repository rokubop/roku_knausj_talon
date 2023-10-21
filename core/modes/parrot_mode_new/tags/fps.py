from talon import Context, Module, actions
import win32api, win32con

mod = Module()
ctx = Context()
ctx_parrot_side_b = Context()
ctx_parrot_pan = Context()

mod.tag("parrot_fps", desc="Tag for fps parrot mode")
ctx.matches = "tag: user.parrot_fps"
ctx_parrot_side_b.matches = """
tag: user.parrot_side_b
and tag: user.parrot_fps
"""
ctx_parrot_pan.matches = """
tag: user.parrot_pan
and tag: user.parrot_fps
and mode: user.parrot
"""
ctx.settings = {
    "key_hold": 64.0,
    "key_wait": 16.0,
}

@ctx.action_class("user")
class Actions:
    def parrot_cluck():
        actions.user.parrot_mode_disable()
        actions.user.genshin_stop_layer()
        actions.user.genshin_stop_layer()
    def parrot_pop():
        actions.key('e')
        actions.user.parrot_mouse_click(0)
        actions.user.genshin_stop_layer()
    # def parrot_t(): actions.skip()
    # def parrot_guh(): actions.skip()
    def parrot_tut(): actions.user.parrot_mouse_click(1)

    def parrot_hiss():
        actions.user.hold_dir_key_mutually_exclusive('w')
    def parrot_hiss_stop(): actions.skip()
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    def parrot_eh(): actions.user.hold_dir_key_mutually_exclusive('a')
    def parrot_er(): actions.user.hold_dir_key_mutually_exclusive('d')
    def parrot_shush(): actions.user.hold_dir_key_mutually_exclusive('s')
    def parrot_shush_stop(): actions.skip()
    def parrot_nn(): actions.user.parrot_activate_side_b_briefly()
    def parrot_ee(): actions.user.genshin_stop_layer()
    def parrot_palate():actions.user.fps_repeater()
    def parrot_t():actions.key("q")

@ctx_parrot_side_b.action_class("user")
class Actions:
    def parrot_cluck():
        if (actions.user.parrot_side_b_source_tag() == "user.parrot_fps"):
            actions.user.parrot_mode_append_tag("user.parrot_default")
            actions.user.parrot_mode_remove_tag("user.parrot_fps")
        else:
            actions.user.parrot_mode_reset_tags()
    def parrot_hiss():
        if (actions.user.parrot_side_b_source_tag() == "user.parrot_pan"):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('w')
        else:
            actions.user.parrot_mode_append_tag("user.parrot_pan")
            actions.user.add_color_cursor("FFA500")
            actions.user.mouse_move_native_down()
        actions.user.parrot_side_b_disable()
    def parrot_hiss_stop(): pass
    def parrot_shush():
        if (actions.user.parrot_side_b_source_tag() == "user.parrot_pan"):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('s')
        else:
            actions.user.parrot_mode_append_tag("user.parrot_pan")
            actions.user.add_color_cursor("FFA500")
            actions.user.mouse_move_native_up()
        actions.user.parrot_side_b_disable()
    def parrot_shush_stop(): pass
    def parrot_eh(): actions.user.parrot_position_mode_enable()
    def parrot_ee(): win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1200, 0)

@ctx_parrot_pan.action_class("user")
class Actions:
    def parrot_ah(): actions.user.mouse_move_native_left()
    def parrot_oh(): actions.user.mouse_move_native_right()
    def parrot_hiss():
        if (actions.user.parrot_mode_has_tag("user.parrot_side_b")):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('w')
        else:
            actions.user.mouse_move_native_down()
    def parrot_hiss_stop(): pass
    def parrot_shush():
        print("shush from pan")
        if (actions.user.parrot_mode_has_tag("user.parrot_side_b")):
            actions.user.parrot_pan_mode_disable()
            actions.user.hold_dir_key_mutually_exclusive('s')
        else:
            actions.user.mouse_move_native_up()
    def parrot_shush_stop(): pass
    def parrot_eh(): actions.user.hold_dir_key_mutually_exclusive('a')
    def parrot_er(): actions.user.hold_dir_key_mutually_exclusive('d')
    def parrot_nn(): actions.user.parrot_activate_side_b_briefly()