from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx_side_b = Context()

mod.tag("parrot_default", desc="Tag for default parrot mode")
ctx.matches = "tag: user.parrot_default"
ctx_side_b.matches = """
tag: user.parrot_default
and tag: user.parrot_side_b
"""

# def mode_disable():
#     return {
#         "name": 'mode disable',
#         "action": actions.user.parrot_mode_disable
#     }

# def repeater():
#     def action():
#         if actions.user.parrot_mode_has_tag('user.parrot_side_b'):
#             actions.user.palate_mode_toggle()
#             return
#         actions.core.repeat_phrase()

#     return {
#         "name": 'repeater',
#         "action": action
#     }

# def click_left_keep_mode():
#     return {
#         "name": 'click left keep mode',
#         "action": lambda: actions.user.parrot_mouse_click(0)
#     }

# def click_left_exit_mode():
#     def action():
#             actions.user.parrot_mouse_click(0)
#             actions.user.parrot_mode_disable()

#     return {
#         "name": 'click left exit mode',
#         "action": action
#     }

# def click_left_drag():
#     return {
#         "name": 'click left drag',
#         "action": lambda: actions.user.parrot_mouse_drag(0)
#     }

# def click_right():
#     return {
#         "name": 'click right',
#         "action": lambda: actions.user.parrot_mouse_click(1)
#     }

# def scroll_down():
#     return {
#         "name": 'scroll down',
#         "action": actions.user.parrot_scroll_down
#     }

# def scroll_down_stop():
#     return {
#         "name": 'scroll down stop',
#         "action": actions.user.parrot_scroll_stop_soft
#     }

# def scroll_up():
#     return {
#         "name": 'scroll up',
#         "action": actions.user.parrot_scroll_up
#     }

# def scroll_up_stop():
#     return {
#         "name": 'scroll up stop',
#         "action": actions.user.parrot_scroll_stop_soft
#     }

# def mod_shift_and_side_b():
#     def action():
#         actions.user.parrot_activate_side_b_briefly()
#         actions.user.parrot_set_modifier('shift')

#     return {
#         "name": 'shift/side b',
#         "action": action
#     }

# def mod_alt_and_side_c():
#     def action():
#         actions.user.parrot_activate_side_c_briefly()
#         actions.user.parrot_set_modifier('alt')

#     return {
#         "name": 'alt/side c',
#         "action": action
#     }

# def mod_ctrl_and_side_d():
#     def action():
#         actions.user.parrot_activate_side_d_briefly()
#         actions.user.parrot_set_modifier('ctrl')

#     return {
#         "name": 'ctrl/side d',
#         "action": action
#     }

# def stopper():
#     return {
#         "name": 'stopper',
#         "action": actions.user.parrot_mouse_and_scroll_stop
#     }

# def use_position_mode():
#     return {
#         "name": 'use position mode',
#         "action": actions.user.parrot_position_mode_enable
#     }

# def use_rpg_mouse_mode():
#     return {
#         "name": 'use rpg mouse mode',
#         "action": actions.user.parrot_rpg_mouse_mode_enable
#     }

# flex_profile = {
#     "name": "default",
#     "commands": {
#         "cluck": mode_disable,
#         "palate": repeater,
#         "nn": click_left_keep_mode,
#         "pop": click_left_exit_mode,
#         "ah": click_left_drag,
#         "oh": click_right,
#         "hiss": scroll_down,
#         "hiss stop": scroll_down_stop,
#         "shush": scroll_up,
#         "shush stop": scroll_up_stop,
#         "t": mod_shift_and_side_b,
#         "tut": mod_alt_and_side_c,
#         "guh": mod_ctrl_and_side_d,
#         "ee": stopper,
#         "eh": use_position_mode,
#         "er": use_rpg_mouse_mode
#     }
# }

@ctx.action_class("user")
class ParrotCommands:
    # def flex_profile():
    #     return flex_profile

    # wake/sleep
    def parrot_cluck(): actions.user.parrot_mode_disable()

    # repeat
    def parrot_palate():
        if actions.user.parrot_mode_has_tag('user.parrot_side_b'):
            actions.user.palate_mode_toggle()
            return
        actions.core.repeat_phrase()

    # mouse clicks
    def parrot_nn(): actions.user.parrot_mouse_click(0)
    def parrot_pop():
        actions.user.parrot_mouse_click(0)
        actions.user.parrot_mode_disable()
    def parrot_ah(): actions.user.parrot_mouse_drag(0)
    def parrot_oh(): actions.user.parrot_mouse_click(1)

    # mouse scroll
    def parrot_hiss(): actions.user.parrot_scroll_down()
    def parrot_hiss_stop(): actions.user.parrot_scroll_stop_soft()
    def parrot_shush(): actions.user.parrot_scroll_up()
    def parrot_shush_stop(): actions.user.parrot_scroll_stop_soft()

    # modifiers
    def parrot_t():
        actions.user.parrot_activate_side_b_briefly()
        actions.user.parrot_set_modifier('shift')
    def parrot_tut(): actions.user.parrot_set_modifier('alt')
    def parrot_guh(): actions.user.parrot_set_modifier('ctrl')

    # stopper
    def parrot_ee(): actions.user.parrot_mouse_and_scroll_stop()

    # modes
    def parrot_eh(): actions.user.parrot_position_mode_enable()
    def parrot_er(): actions.user.parrot_rpg_mouse_mode_enable()