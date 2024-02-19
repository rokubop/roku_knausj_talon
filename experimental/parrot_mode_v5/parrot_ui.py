from talon import Module, Context, actions, ui, skia, cron, ctrl
from talon.screen import Screen
from talon.canvas import Canvas, MouseEvent
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia import RoundRect
from talon.types import Rect, Point2d

mod = Module()

canvas_cursor = None
canvas_cursor_job = None
cursor_color = "FF0000"
modifiers = set()

canvas_bar = None
bar_text = ""

def on_cursor_update(c: SkiaCanvas):
    c.paint.color = cursor_color
    c.paint.style = c.paint.Style.FILL
    c.paint.textsize = 15
    (x, y) = ctrl.mouse_pos()
    c.draw_circle(x + 20, y + 20, 7)

    mod_x = 31
    if "shift" in modifiers:
        c.paint.color = "0490c9"
        c.draw_circle(x + mod_x, y + 30, 5)
        mod_x += 11
        # c.draw_text("s", x, y + 30)

    if "ctrl" in modifiers:
        c.paint.color = "84E773"
        c.draw_circle(x + mod_x, y + 30, 5)
        mod_x += 11
        # c.draw_text("c", x + 2, y + 30)

    if "alt" in modifiers:
        c.paint.color = "FF6DD9"
        # c.draw_text("a", x + 30, y + 30)
        c.draw_circle(x + mod_x, y + 30, 5)

def on_bar_update(c: SkiaCanvas):
    global bar_text
    c.paint.color = "FF0000"
    c.paint.style = c.paint.Style.FILL
    c.paint.textsize = 15
    c.draw_text(bar_text, 500, 1000)

def update_bar():
    if canvas_bar:
        canvas_bar.freeze()


def update_cursor():
    if canvas_cursor:
        canvas_cursor.freeze()

@mod.action_class
class GeneralUI:
    def parrot_v5_ui_clear():
        """Clear all ui"""
        actions.user.parrot_v5_ui_cursor_disable()
        actions.user.parrot_v5_ui_bar_disable()

@mod.action_class
class CursorUI:
    def parrot_v5_ui_cursor_enable():
        """Enable the cursor"""
        global canvas_cursor, canvas_cursor_job
        if not canvas_cursor:
            current_screen = actions.user.ui_get_current_screen()
            canvas_cursor = Canvas.from_screen(current_screen)
            canvas_cursor.register("draw", on_cursor_update)
            canvas_cursor_job = cron.interval("16ms", update_cursor)

    def parrot_v5_ui_cursor_disable():
        """Disable the cursor"""
        global canvas_cursor, canvas_cursor_job
        if canvas_cursor:
            canvas_cursor.unregister("draw", on_cursor_update)
            cron.cancel(canvas_cursor_job)
            canvas_cursor = None
            canvas_cursor_job = None

    def parrot_v5_ui_cursor_red():
        """Set the cursor to red"""
        global cursor_color
        cursor_color = "FF0000"
        actions.user.parrot_v5_ui_cursor_enable()

    def parrot_v5_ui_cursor_blue():
        """Set the cursor to blue"""
        global cursor_color
        cursor_color = "0490c9"
        actions.user.parrot_v5_ui_cursor_enable()

    def parrot_v5_ui_cursor_yellow():
        """Set the cursor to yellow"""
        global cursor_color
        cursor_color = "FFF000"
        actions.user.parrot_v5_ui_cursor_enable()

    def parrot_v5_ui_cursor_green():
        """Set the cursor to green"""
        global cursor_color
        cursor_color = "50C878"
        actions.user.parrot_v5_ui_cursor_enable()

    def parrot_v5_ui_cursor_custom_color(color: str):
        """Set the cursor to custom_color"""
        global cursor_color
        cursor_color = color
        actions.user.parrot_v5_ui_cursor_enable()

    def parrot_v5_ui_cursor_mod_enable(mod: str):
        """Enable the mod e.g. shift, ctrl, alt"""
        global modifiers
        modifiers.add(mod)

    def parrot_v5_ui_cursor_mod_disable(mod: str):
        """Disable the mod e.g. shift, ctrl, alt"""
        global modifiers
        modifiers.discard(mod)

@mod.action_class
class BarUI:
    def parrot_v5_ui_bar_enable():
        """Enable the bar"""
        global canvas_bar
        if not canvas_bar:
            screen: Screen = ui.main_screen()
            canvas_bar = Canvas.from_screen(screen)
            canvas_bar.register("draw", on_bar_update)
            update_bar()

    def parrot_v5_ui_bar_disable():
        """Disable the bar"""
        global canvas_bar
        if canvas_bar:
            canvas_bar.unregister("draw", on_bar_update)
            canvas_bar = None

    def parrot_v5_ui_bar(text: str):
        """Set bar"""
        global bar_text
        bar_text = text
        actions.user.parrot_v5_ui_bar_enable()
        update_bar()
