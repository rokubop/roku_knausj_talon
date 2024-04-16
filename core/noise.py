"""
Map noises (like pop) to actions so they can have contextually differing behavior
"""

from talon import Module, actions, cron, noise

mod = Module()
hiss_cron = None

current_hiss_action = "teleport"

def scroll_if_active(active: bool, direction: int):
    if active:
        if direction < 0:
            actions.user.mouse_scroll_down(3)
        else:
            actions.user.mouse_scroll_up(3)

hiss_actions = {
    "teleport": lambda active: teleport(active),
    "scroll_down": lambda active: scroll_if_active(active, -1),
    "scroll_up": lambda active: scroll_if_active(active, 1)
}

def teleport(active: bool):
    if active:
        actions.tracking.control_gaze_toggle(True)
        actions.tracking.control_head_toggle(False)
    else:
        actions.tracking.control_gaze_toggle(False)
        actions.tracking.control_head_toggle(False)

@mod.action_class
class Actions:
    def noise_set_action(action: str):
        """
        Set the action to be triggered by the hiss noise
        """
        global current_hiss_action
        if action in hiss_actions:
            current_hiss_action = action
        else:
            print(f"Action {action} not found")

    def noise_trigger_pop():
        """
        Called when the user makes a 'pop' noise. Listen to
        https://noise.talonvoice.com/static/previews/pop.mp3 for an
        example.
        """

    def noise_trigger_hiss(active: bool):
        """
        Called when the user makes a 'hiss' noise. Listen to
        https://noise.talonvoice.com/static/previews/hiss.mp3 for an
        example.
        """
        global current_hiss_action
        hiss_actions[current_hiss_action](active)


def noise_trigger_hiss_debounce(active: bool):
    """Since the hiss noise triggers while you're talking we need to debounce it"""
    global hiss_cron
    if active:
        hiss_cron = cron.after("100ms", lambda: actions.user.noise_trigger_hiss(active))
    else:
        cron.cancel(hiss_cron)
        actions.user.noise_trigger_hiss(active)


noise.register("pop", lambda _: actions.user.noise_trigger_pop())
noise.register("hiss", noise_trigger_hiss_debounce)
