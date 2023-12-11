from talon import Module, Context, actions, ui, skia
from talon.screen import Screen
from talon.canvas import Canvas, MouseEvent
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia import RoundRect
from talon.types import Rect, Point2d

mod = Module()
ctx = Context()

canvas: Canvas = None

def draw_center_text(c: SkiaCanvas, text: str, x: int, y: int):
    text_rect = c.paint.measure_text(text)[1]
    c.draw_text(
        text,
        x + text_rect.x - text_rect.width / 2,
        y - text_rect.y - text_rect.height / 2,
    )



def on_draw(c: SkiaCanvas):
    c.paint.color = "ffffff"
    c.paint.textsize = 15
    # for letter, coor in mod.lists["user.fl_track_positions"]:
    #     x, y = coor.split(",")
    #     draw_center_text(c, letter, x, y)

    draw_center_text(c, "a", 328, 180)
    draw_center_text(c, "b", 328, 220)
    draw_center_text(c, "c", 328, 260)
    draw_center_text(c, "d", 328, 300)
    draw_center_text(c, "e", 328, 340)
    draw_center_text(c, "f", 328, 380)
    draw_center_text(c, "g", 328, 420)
    draw_center_text(c, "h", 328, 460)
    draw_center_text(c, "i", 328, 500)
    draw_center_text(c, "k", 328, 540)
    draw_center_text(c, "l", 328, 580)

@mod.action_class
class Actions:
    def fl_canvas_show():
        """canvas_test_one"""
        global canvas
        screen: Screen = ui.main_screen()
        canvas = Canvas.from_screen(screen)
        canvas.register("draw", on_draw)

    def fl_canvas_hide():
        """canvas_test_stop"""
        global canvas
        if canvas:
            canvas.unregister("draw", on_draw)
            canvas.hide()
            canvas.close()

    def draw_something(text: str, x: int, y: int):
        """draw something"""
        global canvas
        text_rect = canvas.paint.measure_text(text)[1]
        canvas.draw_text(
            text,
            x + text_rect.x - text_rect.width / 2,
            y - text_rect.y - text_rect.height / 2,
        )

def on_app_switch(application):
    if application.name == "FL Studio":
        actions.user.fl_canvas_show()
    else:
        actions.user.fl_canvas_hide()

ui.register("app_activate", on_app_switch)
# os: windows
# and app.name: FL Studio
# os: windows
# and app.exe: FL64.exe
