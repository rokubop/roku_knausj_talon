from talon import Module, actions, ui

mod = Module()

ui = None

@mod.action_class
class Actions:
    def test_whatever():
        """w"""
        print(ui.active_app())

    def test_ui():
        """test"""
        global ui
        (screen, div, text, button) = actions.user.ui_elements(["screen", "div", "text", "button"])

        ui = screen(justify_content="center", align_items="center")[
            div(background_color="333333", padding=16, border_radius=16)[
                div(justify_content="flex_end", width=200, align_items="flex_end")[
                    button("X", border_radius=16, on_click=actions.user.test_ui_hide)
                ],
                text("hello world"),
                button("hello world", margin_top=16, on_click=actions.user.test_ui_hide),
            ]]
        ui.show()

    def test_ui_hide():
        """test hide"""
        global ui
        ui.hide()
