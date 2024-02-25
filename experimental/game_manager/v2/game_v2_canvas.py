from talon import Module, Context, actions, ui, skia, cron
from talon.screen import Screen
from talon.canvas import Canvas, MouseEvent
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia import RoundRect
from talon.types import Rect, Point2d

mod = Module()
ctx = Context()

canvas_info: Canvas = None
canvas_status: Canvas = None

def draw_center_text(c: SkiaCanvas, text: str, x: int, y: int):
    text_rect = c.paint.measure_text(text)[1]
    c.draw_text(
        text,
        x + text_rect.x - text_rect.width / 2,
        y - text_rect.y - text_rect.height / 2,
    )

counter = 0
global_text = ""
canvas_clear_job = None
statuses = {}
box_color = "222666"

def draw_x(c: SkiaCanvas):
    global counter, global_text
    c.paint.color = "ffffff"
    c.paint.textsize = 30
    draw_center_text(c, global_text, 328, 180)

def update(text: str):
    global canvas_info, counter, global_text
    global_text = text
    if canvas_info:
        canvas_info.freeze()

def on_status_update(c: SkiaCanvas):
    global statuses, box_color
    y = 600
    x = 1800
    c.paint.color = f"{box_color}dd"
    c.paint.style = c.paint.Style.FILL
    c.draw_rrect(RoundRect.from_rect(Rect(x - 20, y - 20, 200, 100)))

    for name, status in statuses.items():
        text = f"{name}: {status}"
        c.paint.color = "ffffff"
        c.paint.textsize = 16
        c.draw_text(text, x, y)
        # draw_center_text(c, text, x, y)
        y += 30

@mod.action_class
class Actions:
    def game_v2_canvas_calibrate_x():
        """canvas_test_one"""
        global canvas_info
        actions.user.game_v2_canvas_hide()
        screen: Screen = ui.main_screen()
        canvas_info = Canvas.from_screen(screen)
        canvas_info.register("draw", draw_x)

    def game_v2_canvas_refresh(text: str):
        """Refresh canvas test1"""
        update(text)
        global canvas_clear_job
        if canvas_clear_job:
            cron.cancel(canvas_clear_job)
        canvas_clear_job = cron.after("5s", actions.user.game_v2_canvas_hide)

    def game_v2_canvas_hide():
        """canvas_test_stop"""
        global canvas_info, canvas_clear_job
        if canvas_info:
            canvas_info.unregister("draw", draw_x)
            canvas_info.hide()
            canvas_info.close()
            canvas_info = None
            canvas_clear_job = None

    def game_v2_canvas_box_color(color: str):
        """The color of the canvas box"""
        global box_color
        box_color = color

    def game_v2_canvas_status_update(name: str, status: str):
        """Update status"""
        global statuses, canvas_status
        statuses[name] = status
        if canvas_status:
            canvas_status.freeze()

    def game_v2_canvas_status_enable():
        """Enable canvas that shows statuses"""
        global canvas_status
        actions.user.game_v2_canvas_hide()
        actions.user.game_v2_canvas_status_disable()
        screen: Screen = ui.main_screen()
        canvas_status = Canvas.from_screen(screen)
        canvas_status.register("draw", on_status_update)

    def game_v2_canvas_status_disable():
        """Disable canvas that shows statuses"""
        global canvas_status
        if canvas_status:
            canvas_status.unregister("draw", on_status_update)
            canvas_status.hide()
            canvas_status.close()
            canvas_status = None


    # def draw_something(text: str, x: int, y: int):
    #     """draw something"""
    #     global canvas_info
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
