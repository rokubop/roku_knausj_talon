from talon import Context, Module, actions

mod = Module()
ctx = Context()

modifiers = []
modifier_images = {
    "shift": "shift_down",
    "ctrl": "ctrl",
    "alt": "alt",
}

@mod.action_class
class Actions:
    def parrot_v4_set_modifier(modifier: str):
        """Set modifier"""
        print("hello from the starter modifier")
        actions.key(f"{modifier}:down")
        modifiers.append(modifier)
        actions.user.hud_add_ability('modifiers',
            image=modifier_images[modifier],
            enabled=True,
            colour='FFFFFF',
            activated=True)

@ctx.action_class("user")
class Events:
    def parrot_v4_on_stopper():
        print("hello from the stopper modifier")
        if modifiers:
            for key in modifiers:
                actions.key(f"{key}:up")
            actions.user.hud_add_ability('modifiers', image='shift_down', enabled=False, colour='FFFFFF',  activated=False)
            modifiers.clear()
            actions.next()

    # def parrot_v4_on_before_mouse_click():
    #     for key in modifiers:
    #             actions.key(f"{key}:down")

    # def parrot_v4_on_after_mouse_click():
    #     for key in modifiers:
    #             actions.key(f"{key}:up")

    # def parrot_v4_on_before_mouse_scroll():
    #     for key in modifiers:
    #             actions.key(f"{key}:down")

    # def parrot_v4_on_after_mouse_scroll():
    #     for key in modifiers:
    #             actions.key(f"{key}:up")