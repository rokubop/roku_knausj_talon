from talon import Module, Context, actions, ctrl
mod = Module()
ctx = Context()
mod.apps.qemu_system_x_8_6_6_4 = r"""
os: windows
and app.exe: qemu-system-x86_64.exe
"""
ctx.matches = r"""
os: windows
app: qemu_system_x_8_6_6_4
"""
@mod.action_class
class Actions:
    def android_scroll_down():
        """scroll down"""
        actions.mouse_drag(0);
        x, y = ctrl.mouse_pos()
        ctrl.mouse_move(x, y - 600)
        actions.sleep("100ms")
        actions.mouse_release(0);
        ctrl.mouse_move(x, y)

    def android_scroll_up():
        """scroll up"""
        actions.mouse_drag(0);
        x, y = ctrl.mouse_pos()
        ctrl.mouse_move(x, y + 600)
        actions.sleep("100ms")
        actions.mouse_release(0);
        ctrl.mouse_move(x, y)