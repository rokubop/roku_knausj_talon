from talon import Module, actions, ctrl

mod = Module()
mod.mode("parrot", "Parrot Mode for controlling mouse, modifiers, and scrolling")

is_dragging = False
modifiers = []

@mod.action_class
class ParrotModeActions:
    def parrot_mouse_drag(button: int):
        """Drag the mouse in a direction"""
        global is_dragging

        if not is_dragging:
            is_dragging = True
            for key in modifiers:
                actions.key(f"{key}:down")
            ctrl.mouse_click(button=button, down=True)

    def parrot_mouse_click(button: int, times: int = 1):
        """Click the mouse"""
        global is_dragging

        if is_dragging:
            actions.user.parrot_mouse_and_scroll_stop()
        else:
            for key in modifiers:
                actions.key(f"{key}:down")
            for i in range(times):
                ctrl.mouse_click(button=button, hold=16000)
            for key in modifiers:
                actions.key(f"{key}:up")

    def parrot_scroll_down():
        """Scroll the mouse down"""
        for key in modifiers:
            actions.key(f"{key}:down")
        actions.user.mouse_scroll_down();

    def parrot_scroll_up():
        """Scroll the mouse up"""
        for key in modifiers:
            actions.key(f"{key}:down")
        actions.user.mouse_scroll_up();

    def parrot_mouse_and_scroll_stop():
        """Stop mouse and scroll"""
        global is_dragging
        is_dragging = False
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)
        for key in modifiers:
            actions.key(f"{key}:up")
        actions.user.mouse_scroll_stop()
        modifiers.clear()

    def parrot_set_modifier(key: str):
        """Set the modifier"""
        if not is_dragging and key not in modifiers:
            modifiers.append(key)

    def parrot_cancel_modifiers():
        """Cancel modifiers"""
        for key in modifiers:
            actions.key(f"{key}:up")
        modifiers.clear()

    def parrot_trigger_virtual_key():
        """Trigger virtual key"""

mod = Module()
@mod.action_class
class UserActions:
    def parrot_mode_enable():
        """Enable parrot mode"""
        print("parrot mode enabled")
        actions.user.add_red_cursor()
        actions.mode.enable("user.parrot")
        actions.mode.disable("command")
        actions.mode.disable("dictation")

    def parrot_mode_disable():
        """Disable parrot mode"""
        print('parrot mode disabled')
        actions.user.clear_screen_regions()
        actions.user.parrot_mouse_and_scroll_stop()
        actions.mode.disable("user.parrot")
        actions.mode.enable("command")
        actions.mode.disable("dictation")