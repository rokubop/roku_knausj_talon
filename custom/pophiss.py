# # from talon import Module, actions, noise, scope
# import os

# from talon import Module, actions, app, clip, cron, ctrl, imgui, noise, ui, Context
# from talon_plugins import eye_mouse, eye_zoom_mouse
# from talon_plugins.eye_mouse import config, toggle_camera_overlay, toggle_control


# def on_pop(active):
#     if (actions.speech.enabled()):
#         ctrl.mouse_click(button=0, hold=16000)

# noise.register("pop", on_pop)

# def on_hiss(active):
#     # print(ctx.matches)
#     actions.core.repeat_command()

# noise.register("hiss", on_hiss)