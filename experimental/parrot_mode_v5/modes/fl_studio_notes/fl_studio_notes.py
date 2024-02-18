from talon import Module, Context, actions, settings, ctrl

mod = Module()
mod.mode("parrot_v5_fl_studio_notes", "Mode for FL Studio notes")
ctx = Context()

ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_fl_studio_notes
"""

@mod.action_class
class Actions:
    def parrot_v5_fl_studio_notes_disable():
        """Disable FL Studio notes"""
        actions.user.event_key_hold_stop_all()
        actions.user.parrot_v5_ui_clear()
        actions.user.parrot_v5_mode_disable()

    def parrot_v5_fl_studio_notes_enable():
        """Enable FL Studio notes"""
        actions.user.parrot_v5_mode_enable("user.parrot_v5_fl_studio_notes")
        actions.user.parrot_v5_ui_cursor_blue()
        actions.user.parrot_v5_ui_bar("ah: 1 | eh: 2 | oh: 3 | hiss: 4 | shush: 5 | t: 6 | tut: 7 | guh: 8")

    def parrot_v5_fl_studio_note_1():
        """FL Studio note 1"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("z")

    def parrot_v5_fl_studio_note_2():
        """FL Studio note 2"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("x")

    def parrot_v5_fl_studio_note_3():
        """FL Studio note 3"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("c")

    def parrot_v5_fl_studio_note_4():
        """FL Studio note 4"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("v")

    def parrot_v5_fl_studio_note_5():
        """FL Studio note 5"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("b")

    def parrot_v5_fl_studio_note_6():
        """FL Studio note 6"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("n")

    def parrot_v5_fl_studio_note_7():
        """FL Studio note 7"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("m")

    def parrot_v5_fl_studio_note_8():
        """FL Studio note 8"""
        actions.user.event_key_hold_stop_all()
        actions.user.event_key_hold_start("q")

    def parrot_v5_fl_studio_notes_toggle_play():
        """FL Studio note toggle"""
        actions.user.event_key_hold_stop_all()
        # actions.user.event_key_hold_start("q")
