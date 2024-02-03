from talon import Module, Context, actions, ui, skia, cron
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

counter = 0
global_text = ""

def draw_x(c: SkiaCanvas):
    global counter, global_text
    c.paint.color = "ffffff"
    c.paint.textsize = 30
    draw_center_text(c, global_text, 328, 180)

def update(text: str):
    global canvas, counter, global_text
    global_text = text
    if canvas:
        canvas.freeze()

@mod.action_class
class Actions:
    def game_v2_canvas_calibrate_x():
        """canvas_test_one"""
        global canvas
        actions.user.game_v2_canvas_hide()
        screen: Screen = ui.main_screen()
        canvas = Canvas.from_screen(screen)
        canvas.register("draw", draw_x)

    def game_v2_canvas_refresh(text: str):
        """Refresh canvas test1"""
        update(text)

    def game_v2_canvas_hide():
        """canvas_test_stop"""
        global canvas
        if canvas:
            canvas.unregister("draw", draw_x)
            canvas.hide()
            canvas.close()

    # def draw_something(text: str, x: int, y: int):
    #     """draw something"""
    #     global canvas
    #     text_rect = canvas.paint.measure_text(text)[1]
    #     canvas.draw_text(
    #         text,
    #         x + text_rect.x - text_rect.width / 2,
    #         y - text_rect.y - text_rect.height / 2,
    #     )

# def on_app_switch(application):
#     if application.name == "FL Studio":
#         actions.user.game_v2_canvas_calibrate_x()
#     else:
#         actions.user.game_v2_canvas_hide()

# ui.register("app_activate", on_app_switch)
# os: windows
# and app.name: FL Studio
# os: windows
# and app.exe: FL64.exe
