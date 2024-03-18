from talon import Module, Context, actions, ui, skia, cron
from dataclasses import dataclass
from talon.screen import Screen
from talon.canvas import Canvas, MouseEvent
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia import RoundRect
from talon.types import Rect, Point2d

mod = Module()

canvas_textarea = None
textarea_title = None
textarea_list = []
textarea_bg_color = None
textarea_text_color = None
textarea_font_size = 16
text_gap = 9
padding = 20

def measure_textarea(text_list, paint):
    global text_gap, textarea_font_size
    normalized_text_height = textarea_font_size
    max_width = 0
    total_height = 0
    for text in text_list:
        text_rect = paint.measure_text(text)[1]
        width = text_rect.width
        if width > max_width:
            max_width = width
        total_height += normalized_text_height + text_gap
    return (max_width, total_height - text_gap)

def on_textarea_update(c: SkiaCanvas):
    global textarea_list, textarea_title, textarea_font_size, textarea_bg_color, padding, text_gap
    c.paint.textsize = textarea_font_size
    (width, height) = measure_textarea(textarea_list, c.paint)
    normalized_text_height = textarea_font_size
    if textarea_title:
        rect_title = c.paint.measure_text(textarea_title)[1]
        if rect_title.width > width:
            width = rect_title.width
        height += normalized_text_height + text_gap * 2
    width_padded = width + padding * 2
    height_padded = height + padding * 2
    x = 1920 - width_padded
    y = 1080 / 2 - height_padded / 2

    c.paint.color = f"{textarea_bg_color}aa"
    c.paint.style = c.paint.Style.FILL
    c.draw_rrect(RoundRect.from_rect(Rect(x, y, width_padded, height_padded)))

    c.paint.color = "ffffff"
    x += padding
    y += padding
    if textarea_title:
        c.draw_text(textarea_title, x, y + normalized_text_height)
        y += normalized_text_height + text_gap
        c.draw_line(x, y, x + width, y)
        y += text_gap
    for command in textarea_list:
        c.draw_text(command, x, y + normalized_text_height)
        y += normalized_text_height + text_gap

@mod.action_class
class Actions:
    def ui_textarea_show(options: dict):
        """Show the textarea"""
        global canvas_textarea, textarea_title, textarea_list, textarea_bg_color, textarea_text_color
        if not canvas_textarea:
            screen: Screen = ui.main_screen()
            canvas_textarea = Canvas.from_screen(screen)
            canvas_textarea.register("draw", on_textarea_update)

        textarea_title = options.get("title", "")
        textarea_list = options.get("text_lines", [])
        textarea_bg_color = options.get("bg_color", "222666")
        canvas_textarea.freeze()

    def ui_textarea_hide():
        """Show the textarea"""
        global canvas_textarea
        if canvas_textarea:
            canvas_textarea.unregister("draw", on_textarea_update)
            canvas_textarea.hide()
            canvas_textarea.close()
            canvas_textarea = None
