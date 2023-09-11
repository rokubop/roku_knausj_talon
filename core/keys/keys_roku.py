from talon import Module, actions

mod = Module()

dir_key_lists = {
    'awsd': ["w", "a", "s", "d", "e", "q"],
    'arrows': ["up", "down", "left", "right"],
    # 'tilt': ["e", "q"]
}

@mod.action_class
class Actions:
    def hold_dir_key_mutually_exclusive(dir_key: str):
        """Hold a direction key and release its related keys"""
        keys_to_release = None

        for dir_keys in dir_key_lists.values():
            if dir_key in dir_keys:
                keys_to_release = dir_keys
                break

        if not keys_to_release:
            return

        for key in keys_to_release:
            if key != dir_key:
                actions.key(f"{key}:up")
        actions.key(f"{dir_key}:down")

    def release_dir_keys_all():
        """Release all direction keys"""
        for list_type in dir_key_lists.values():
            for dir_key in list_type:
                actions.key(f"{dir_key}:up")