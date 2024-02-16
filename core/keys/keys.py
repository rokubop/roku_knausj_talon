from talon import Context, Module, actions, app

from ..user_settings import get_list_from_csv


def setup_default_alphabet():
    """set up common default alphabet.

    no need to modify this here, change your alphabet using alphabet.csv"""
    initial_default_alphabet = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split()
    initial_letters_string = "abcdefghijklmnopqrstuvwxyz"
    initial_default_alphabet_dict = dict(
        zip(initial_default_alphabet, initial_letters_string)
    )

    return initial_default_alphabet_dict


alphabet_list = get_list_from_csv(
    "alphabet.csv", ("Letter", "Spoken Form"), setup_default_alphabet()
)

# used for number keys & function keys respectively
digits = "zero one two three four five six seven eight nine".split()
f_digits = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("numpad_key", desc="All numpad keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")

@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key

@mod.capture(rule="{self.numpad_key}")
def numpad_key(m) -> str:
    "One numpad key"
    return m.numpad_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


ctx = Context()
modifier_keys = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    "alt": "alt",  #'alter': 'alt',
    "control": "ctrl",  #'troll':   'ctrl',
    "shift": "shift",  #'sky':     'shift',
    "super": "super",
}

# roku additions
modifier_keys.update({
    "king": "ctrl",
    "ship": "shift"
})

if app.platform == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"
ctx.lists["self.modifier_key"] = modifier_keys
ctx.lists["self.letter"] = alphabet_list

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
punctuation_words = {
    "back tick": "`",
    "comma": ",",
    "coma": ",",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
    "pound sign": "£",
}
symbol_key_words = {
    "dot": ".",
    "point": ".",
    "quote": "'",
    "apostrophe": "'",
    "square": "[",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "underscore": "_",
    "paren": "(",
    "brace": "{",
    "left brace": "{",
    "less than": "<",
    "rangle": ">",
    "greater than": ">",
    "star": "*",
    "hash": "#",
    "amper": "&",
    "pipe": "|",
    "dub quote": '"',
    "double quote": '"',
    "dollar": "$",
    "pound sign": "£",
}
# roku additions
symbol_key_words.update({
    "brick": "`",
    "stroke": "/",
    "backstroke": "\\",
    "equal": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "score": "_",
    "quest": "?",
    "single": "'",
    "curly single": "’",
    "double": '"',
    "leper": "(",
    "curve": "(",
    "repper": ")",
    "recurve": ")",
    "lacker": "[",
    "racker": "]",
    "lacer": "{",
    "racer": "}",
    "langle": "<",
    "wrangle": ">",
    "snow": "*",
    "pound": "#",
    "percy": "%",
    "tangle": "^",
    "amper": "&",
    "pipe": "|",
    "dollar": "$",
    "semi": ";",
    "stack": ":",
    "drip": ",",
})

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
ctx.lists["self.number_key"] = {name: str(i) for i, name in enumerate(digits)}
ctx.lists["self.arrow_key"] = {
    "south": "down",
    "tug": "left",
    "push": "right",
    "north": "up",
}

simple_keys = [
    "escape",
    "insert",
    "pagedown",
    "pageup",
    "space",
    "tab",
]

alternate_keys = {
    "delete": "backspace",
    "end key": "end",
    "home key": "home",
    "page up": "pageup",
    "page down": "pagedown",
    "yep": "enter",
    "drill": "delete",
    "scratch": "backspace",
    "scrape": "escape",
    "void": "space",
    "page up": "pageup",
    "page down": "pagedown",
    "menu key": "menu",
    "print screen": "printscr",
}

# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"fun {name}": f"f{i}" for i, name in enumerate(f_digits, start=1)
}
ctx.lists["self.numpad_key"] = {
    f"numpad {name}": f"keypad_{i}" for i, name in enumerate(digits, start=0)
}

@mod.action_class
class Actions:
    def move_cursor(s: str):
        """Given a sequence of directions, eg. 'left left up', moves the cursor accordingly using edit.{left,right,up,down}."""
        for d in s.split():
            if d in ("left", "right", "up", "down"):
                getattr(actions.edit, d)()
            else:
                raise RuntimeError(f"invalid arrow key: {d}")
