from talon import Module, actions

mod = Module()

ui = None

@mod.action_class
class Actions:
    def test_ui():
        """test"""
        global ui
        (screen, div, text) = actions.user.ui_elements(["screen", "div", "text"])

        ui = screen()[div()[text("hello world")]]
        ui.show()

    def test_ui_hide():
        """test hide"""
        global ui
        ui.hide()
