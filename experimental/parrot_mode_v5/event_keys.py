from talon import Module, actions
from collections import defaultdict

mod = Module()

def no_op():
    pass

keys_held = defaultdict(lambda: False)
modifier_keys_held = defaultdict(lambda: False)

@mod.action_class
class Actions:
    def event_key_modifier_toggle(key: str):
        """Start holding modifier key and fire on_event_modifier_key_toggle"""
        global modifier_keys_held
        should_hold = not modifier_keys_held[key]
        if should_hold:
            actions.user.event_key_modifier_enable(key)
        else:
            actions.user.event_key_modifier_disable(key)

    def event_key_modifier_disable_all():
        """Disable all modifier keys"""
        global modifier_keys_held
        for key in modifier_keys_held:
            actions.user.event_key_modifier_disable(key)

    def event_key_modifier_disable(key: str):
        """Disable modifier key"""
        global modifier_keys_held
        modifier_keys_held[key] = False
        actions.key(f"{key}:up")
        actions.user.on_event_key_modifier_disabled(key)

    def event_key_modifier_enable(key: str):
        """Enable modifier key"""
        global modifier_keys_held
        modifier_keys_held[key] = True
        actions.key(f"{key}:down")
        actions.user.on_event_key_modifier_enabled(key)

    def on_event_key_modifier_enabled(key: str):
        """Fired on event_modifier_key_down"""
        no_op()

    def on_event_key_modifier_disabled(key: str):
        """Fired on event_modifier_key_up"""
        no_op()

    def event_key_hold_start(key: str):
        """Start holding key"""
        global keys_held
        keys_held[key] = True
        actions.key(f"{key}:down")
        # actions.user.on_event_key_hold_start(key)

    def event_key_hold_stop(key: str):
        """Stop holding key"""
        global keys_held
        keys_held[key] = False
        actions.key(f"{key}:up")
        # actions.user.on_event_key_hold_stop(key)

    def event_key_hold_stop_all():
        """Stop holding all keys"""
        global keys_held
        for key in keys_held:
            actions.key(f"{key}:up")
        keys_held.clear()
        # actions.user.on_event_key_hold_stop_all()
