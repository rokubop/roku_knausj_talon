having a base_profile I think is the key
<!-- world_profile = {
        "name": "world",
        'on_start': on_start,
        "commands": {
            "pop": flex_action_click,
            "clock": flex_action_jump
        }
    }
    actions.user.flex_use_profile(world_profile)

    profile = {
        "name": "game_menu",
        "base_profile": actions.user.flex_profile_default,
        'on_start': on_start,
        'on_stop': on_stop,
        "commands": {
            "er": flex_action_jump
        }
    }

    "commands": {
        "cluck cluck": {
            "timeout": "1s",
            "name": "exit",
            "action": actions.user.flex_mode_disable
        },
        "t": toggle_world_or_room_profile
    }

    "overrides": {
        "global": {
            "nn":
        },
    } -->