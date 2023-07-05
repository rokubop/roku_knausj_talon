from threading import Lock
from user.roku_knausj_talon.core.modes.game_mode.GameModeHelper import GameModeHelper
from talon import Module, Context, actions, noise, settings

mod = Module()
mod.list("game_noises")
mod.list("game_noise_controls")

ctx = Context()
noises = ("pop", "hiss")
ctx.lists["user.game_noises"] = noises
noise_action_names = {
    "jump": "jump",
    "move": "move",
    "dodge": "dodge",
    "aim toggle": "aim toggle",
    "long dodge": "long dodge",
    "use": "use",
    "long use": "long use",
    "touch": "click",
    "click": "click",
    "duke": "double click",
    "double click": "double click",
    "long click": "long click",
    "middle click": "middle click",
    "mid click": "middle click",
    "righty": "right click",
    "right click": "right click",
    "right long click": "right long click",
    "tar": "target lock toggle",
    "target lock toggle": "target lock toggle",
    "attack": "attack",
    "block toggle": "block toggle",
    "long attack": "long attack",
    "off": "off",
    "default": "default",
}
ctx.lists["user.game_noise_controls"] = noise_action_names

action_name_to_action = {
    "jump":
        lambda is_active: actions.user.game_jump(is_active),
    "move":
        lambda _: actions.user.switch_game_movement(),
    "dodge":
        lambda _: actions.user.game_dodge(),
    "long dodge":
        lambda _: actions.user.game_long_dodge(),
    "use":
        lambda _: actions.user.game_use(),
    "long use":
        lambda _: actions.user.game_long_use(),
    "click":
        lambda _: actions.user.game_click(0),
    "long click":
        lambda is_active: actions.user.game_press_mouse(button=0, down=is_active),
    "double click":
        lambda _: actions.user.game_click(0, 2),
    "right click":
        lambda _: actions.user.game_click(1),
    "right long click":
        lambda is_active: actions.user.game_press_mouse(button=1, down=is_active),
    "middle click":
        lambda _: actions.user.game_click(2),
    "target lock toggle":
        lambda _: actions.user.game_weapon_target_lock_toggle(),
    "attack":
        lambda _: actions.user.game_attack(),
    "long attack":
        lambda is_active: actions.user.game_attack(is_active),
    "block toggle":
        lambda _: actions.user.game_weapon_block_toggle(),
    "aim toggle":
        lambda _: actions.user.game_weapon_aim_toggle(),
}

hotswappable_binding: dict[str, str] = {"pop": "default", "hiss": "default"}
lock_binding = Lock()

setting_pop_default = mod.setting(
    "game_noise_pop_binding_default",
    type=str,
    default="click",
    desc="""Default pop binding for hot-swappable game mode noise controls.
        See the list of available bindings under user.game_noise_controls.""")

setting_hiss_default = mod.setting(
    "game_noise_hiss_binding_default",
    type=str,
    default="off",
    desc="""Default hiss binding for hot-swappable game mode noise controls.
        See the list of available bindings under user.game_noise_controls.""")

default_noise_settings = {"pop": setting_pop_default, "hiss": setting_hiss_default}


@mod.action_class
class GameNoiseActions:

    def game_before_on_pop() -> tuple[bool, bool]:
        """Customizable behavior. This action is called before the binding for pop is executed.
        Handy for quickly interrupting a game interaction that requires a more precise timing than
        talon is able to achieve with a simple voice command (noises are detected more quickly).

        Returns 2 bool values in a tuple:
            * the first tuple element: execute the action bound to pop if True,
                skip the execution of the bound action if False,
            * the second tuple element: execute game_after_on_pop if True,
                skip execution of game_after_on_pop if False.
        Both are True by default."""
        return (True, True)

    def game_after_on_pop():
        """Customizable behavior. This action is called after the binding for pop is executed
        only if game_before_on_pop returned True as the second element of the returned tuple.
        Doesn't do anything by default."""
        return 0

    def game_before_on_hiss() -> tuple[bool, bool]:
        """Customizable behavior.  This action is called before the binding for hiss is executed.
        Handy for quickly interrupting a game interaction that requires a more precise timing than
        talon is able to achieve with a simple voice command (noises are detected more quickly).

        Returns 2 bool values in a tuple:
            * the first tuple element: execute the action bound to hiss if True,
                skip the execution of the bound action if False,
            * the second tuple element: execute game_after_on_hiss if True,
                skip execution of game_after_on_hiss if False.
        Both are True by default."""
        return (True, True)

    def game_after_on_hiss():
        """Customizable behavior. This action is called after the binding for hiss is executed
        only if game_before_on_hiss returned True as the second element of the returned tuple.
        Doesn't do anything by default."""
        return 0

    def game_noise_control_reset():
        """reset to default"""
        global hotswappable_binding, lock_binding
        with lock_binding:
            hotswappable_binding = {"pop": "default", "hiss": "default"}

    def game_noise_control_switch(noise: str, control: str):
        """switch noise binding"""
        global noises, noise_action_names, hotswappable_binding, lock_binding

        if not (noise in noises and control in noise_action_names.values()):
            # print a warning or notify
            return

        with lock_binding:
            hotswappable_binding[noise] = control


def _execute_noise_binding(noise, is_active):
    global hotswappable_binding
    action_name = hotswappable_binding[noise]

    if action_name == "default":
        action_name = default_noise_settings[noise].get()
    if action_name == "off":
        return

    does_action_require_input = action_name in [
        "long click",
        "jump",
        "long attack",
        "right long click",
    ] or (action_name == "move" and noise == "hiss")

    if does_action_require_input:
        action_name_to_action[action_name](is_active)
    elif is_active:
        action_name_to_action[action_name](True)


def on_pop(_):
    global lock_binding

    if not GameModeHelper.is_game_mode():
        return

    with lock_binding:
        is_execute_binding, is_execute_after = actions.user.game_before_on_pop()
        if not settings.get("user.mouse_enable_pop_click") and is_execute_binding:
            _execute_noise_binding("pop", True)
        if is_execute_after:
            actions.user.game_after_on_pop()


def on_hiss(is_active):
    global lock_binding

    if not GameModeHelper.is_game_mode():
        return

    with lock_binding:
        is_execute_binding, is_execute_after = actions.user.game_before_on_hiss()
        if not settings.get("user.mouse_enable_hiss") and is_execute_binding:
            _execute_noise_binding("hiss", is_active)
        if is_execute_after:
            actions.user.game_after_on_hiss()


noise.register("pop", on_pop)
noise.register("hiss", on_hiss)