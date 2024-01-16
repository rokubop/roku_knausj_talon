import re
from talon import Module, Context, actions

mod = Module()
mod.tag("first_last_char_targets", desc="yep")

ctx_chrome = Context()
ctx_chrome.matches = """
app: chrome
"""

def find_target_token(tokens: list[str], letter_1: str, letter_2: str = None):
    target_token = None
    print(f"Looking for token starting with '{letter_1}' and ending with '{letter_2}'")
    tokens_lowercase = [x.lower() for x in tokens]
    index = None

    print(f"tokens: {tokens}")
    print(f"tokens_lowercase: {tokens_lowercase}")

    if not letter_2:
        for i, word in enumerate(tokens_lowercase):
            if len(word) == 1 and word[0] == letter_1:
                target_token = tokens[i]
                index = i
                break
        if index == None:
            for i, word in enumerate(tokens_lowercase):
                if word[0] == letter_1:
                    target_token = tokens[i]
                    index = i
                    break
    else:
        for i, word in enumerate(tokens_lowercase):
            if len(word) > 1 and word[0] == letter_1 and word[-1] == letter_2:
                target_token = tokens[i]
                index = i
                break

    return (target_token, index)

def find_token_in_select_all(letter_1: str, letter_2: str = ""):
    actions.edit.select_all()
    selected_text = actions.edit.selected_text()
    pattern = r"\b[\w']+\b"
    tokens = re.findall(pattern, selected_text)

    target_token, index = find_target_token(tokens, letter_1, letter_2)
    return target_token, index

@mod.action_class
class Actions:
    def first_last_char_targets_pre(letter_1: str, letter_2: str = ""):
        """Pre text"""
        token, index = find_token_in_select_all(letter_1, letter_2)
        actions.edit.line_start()
        actions.edit.word_right()
        for i in range(index):
            actions.edit.word_right()
        actions.edit.word_left()

    def first_last_char_targets_post(letter_1: str, letter_2: str = ""):
        """Post text"""
        token, index = find_token_in_select_all(letter_1, letter_2)
        actions.edit.line_start()
        actions.edit.word_right()
        for i in range(index):
            actions.edit.word_right()

    def first_last_char_targets_clear(letter_1: str, letter_2: str = ""):
        """Clear/change text"""
        token, index = find_token_in_select_all(letter_1, letter_2)
        actions.edit.line_start()
        actions.edit.word_right()
        for i in range(index):
            actions.edit.word_right()
        actions.edit.delete_word()

    def first_last_char_targets_chuck(letter_1: str, letter_2: str = ""):
        """Chuck text"""
        actions.edit.select_all()
        selected_text = actions.edit.selected_text()
        tokens = selected_text.split(' ')
        target_token, index = find_target_token(tokens, letter_1, letter_2)
        new_text = tokens[:index] + tokens[index + 1:]
        actions.user.paste(" ".join(new_text))

@ctx_chrome.action_class("user")
class Actions:
    def first_last_char_targets_clear(letter_1: str, letter_2: str = ""):
        """Clear/change text"""
        token, index = find_token_in_select_all(letter_1, letter_2)
        actions.edit.line_start()
        # if index != 0:
        for i in range(index):
            actions.edit.word_right()
        actions.edit.delete_word()

    def first_last_char_targets_pre(letter_1: str, letter_2: str = ""):
        """Pre text"""
        token, index = find_token_in_select_all(letter_1, letter_2)
        actions.edit.line_start()
        actions.edit.word_right()
        for i in range(index):
            actions.edit.word_right()
        actions.edit.word_left()

    def first_last_char_targets_post(letter_1: str, letter_2: str = ""):
        """Post text"""
        token, index = find_token_in_select_all(letter_1, letter_2)
        actions.edit.line_start()
        actions.edit.word_right()
        for i in range(index):
            actions.edit.word_right()
        actions.edit.left()

    def first_last_char_targets_chuck(letter_1: str, letter_2: str = ""):
        """Chuck text"""
        actions.edit.select_all()
        selected_text = actions.edit.selected_text()
        tokens = selected_text.split(' ')
        target_token, index = find_target_token(tokens, letter_1, letter_2)
        new_text = tokens[:index] + tokens[index + 1:]
        actions.user.paste(" ".join(new_text))