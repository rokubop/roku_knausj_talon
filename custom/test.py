from talon import Module, actions, ui

mod = Module()

@mod.action_class
class Actions:
    def test_ui():
        """test"""
        global ui
        (screen, div, text, button, input_text) = actions.user.ui_elements(["screen", "div", "text", "button", "input_text"])

        ui = screen(justify_content="center", align_items="center")[
            div(background_color="222222", padding=16, border_radius=16)[
                text("hello world"),
                input_text(
                    id="the_input",
                    margin_top=16,
                    on_change=lambda e: print(f"input {e}")
                ),
                button("submit", margin_top=16, on_click=actions.user.test_ui_hide),
            ]]
        ui.show()

    def test_ui_hide():
        """test hide"""
        actions.user.ui_elements_hide_all()

    def test_ui_value():
        """test hide"""
        value = actions.user.ui_elements_get_value("the_input")
        print(value)
