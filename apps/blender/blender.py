from talon import Module, Context, actions, ctrl, cron
mod = Module()
ctx = Context()
ctx_interactive = Context()
mod.apps.blender = r"""
os: windows
and app.exe: blender.exe
"""
ctx.matches = r"""
os: windows
app: blender
and app.exe: blender.exe
"""
ctx_interactive.matches = r"""
os: windows
app: blender
and tag: user.parrot_default_interactive
and mode: user.parrot
"""

move_mode = False
rotate_mode = False
rotate_value = 0
special = False
debounce = None

def clear_debounce():
    global debounce
    if debounce:
        cron.cancel(debounce)
        debounce = None

def deactivate_special():
    global special
    special = False

def activate_special_briefly():
    global special
    special = True
    cron.after("300ms", deactivate_special)

def clear_modes():
    global move_mode, special, rotate_mode, rotate_value
    move_mode = False
    rotate_mode = False
    special = False
    rotate_value = 0

@mod.action_class
class Actions:
    def blender_activate_cam_fly_mode():
        """Activate camera fly mode"""
        actions.key("shift-`")
        actions.user.parrot_mode_enable()
        actions.user.parrot_mode_enable_tag("user.parrot_fps")

    def blender_parrot_debounced_move_key(key: str):
        """Move blender key in parrot mode"""
        global debounce, special
        if not debounce:
            debounce = cron.after("300ms", clear_debounce)
            if special: actions.key("shift:down")
            actions.key(key)
            if special:
                actions.key("shift:up")
                special = False

@ctx_interactive.action_class("user")
class ParrotInteractiveActions:
    def parrot_guh():
        print("guh from blender")
        global rotate_mode, move_mode
        actions.key("g")
        move_mode = True

    def parrot_er():
        global special, rotate_mode
        if special:
            actions.next()
        else:
            actions.key("r")
            rotate_mode = True
            special = False

    def parrot_ah():
        print("ah from blender")
        global move_mode, rotate_mode
        if move_mode or rotate_mode:
            actions.user.blender_parrot_debounced_move_key("x")
        else:
            actions.next()

    def parrot_oh():
        print("oh from blender")
        global move_mode, rotate_mode
        if move_mode or rotate_mode:
            actions.user.blender_parrot_debounced_move_key("y")
        else:
            actions.next()

    def parrot_hiss():
        print("hiss from blender")
        global move_mode, rotate_mode
        if move_mode or rotate_mode:
            actions.user.blender_parrot_debounced_move_key("z")
        else:
            actions.next()

    def parrot_nn():
        print("nn from blender")
        global move_mode, rotate_mode
        activate_special_briefly()
        if not move_mode and not rotate_mode:
            actions.next()

    def parrot_pop():
        clear_modes()
        actions.next()

    def parrot_ee():
        clear_modes()
        actions.next()

    def parrot_tut():
        global rotate_value, rotate_mode
        if rotate_mode:
            rotate_value += -90
            actions.key("ctrl-backspace")
            actions.insert(rotate_value)
        else:
            clear_modes()
            actions.next()

    def parrot_palate():
        global rotate_value, rotate_mode
        if rotate_mode:
            rotate_value += 90
            actions.key("ctrl-backspace")
            actions.insert(rotate_value)
        else:
            actions.next()

    def parrot_t():
        """Focus selected object"""
        actions.key("keypad_decimal")
        # print('kingfisher click from blender')
        # actions.user.kingfisher_parrot_trigger_virtual_key()

@ctx.action_class("user")
class UserActions:
    def parrot_tut():
        global move_mode, rotate_value, rotate_mode
        if rotate_mode:
            rotate_value += -90
            actions.key("ctrl-backspace")
            actions.insert(rotate_value)
        else:
            clear_modes()
            actions.mouse_click(1)


    def save_as():
        actions.key("ctrl-shift-s")
        actions.sleep("200ms")
        actions.mouse_move(684, 794)
        actions.mouse_click()
        actions.edit.left()
        actions.edit.word_right()

    def virtual_region_one():
        print('region one from blender')

    def virtual_region_two():
        print('region two')

    def virtual_region_three():
        print('region three')

    def virtual_region_four():
        print('region four')

    def virtual_region_five():
        print('region five')

    def virtual_region_six():
        print('region six')

    def virtual_region_seven():
        print('region seven')

    def virtual_region_eight():
        print('region eight')

    def virtual_region_nine():
        print('region nine')
