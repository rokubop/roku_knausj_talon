"""
Fix text by targeting the first and last character of a word
Performs operation on a "select all" scope
"""
import re
from talon import Module, Context, actions

mod = Module()

ctx_chrome = Context()

def find_first_last_char_based_token(tokens: list[str], letter_1: str, letter_2: str = None):
    target_token = None
    tokens_lowercase = [x.lower().strip() for x in tokens]
    index = None

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

def split_tokens_approach_from_left(string: str):
    pattern = r"([\w']+|\.|,|\?)\s*"
    return [match.group(0) for match in re.finditer(pattern, string)]

@mod.action_class
class Actions:
    def fix_text_change(letter_1: str, letter_2: str = ""):
        """Fix text"""
        actions.edit.select_all()
        selected_text = actions.edit.selected_text()

        tokens = split_tokens_approach_from_left(selected_text)
        token, index = find_first_last_char_based_token(tokens, letter_1, letter_2)

        actions.edit.file_start()
        # word_right won't behave correctly if it starts with a space
        if selected_text.startswith(" "):
            actions.key("delete")

        # Put cursor before word
        for i in range(index):
            actions.edit.word_right()

        # Check if it selected white space the way we intended and delete
        actions.edit.extend_word_right()
        actual_token = actions.edit.selected_text()
        if actual_token == token:
            actions.edit.delete()
        else:
            actions.insert(" ")
            if actual_token.endswith(" "):
                actions.edit.left()

    def fix_text_pre(letter_1: str, letter_2: str = ""):
        """Fix text pre"""
        actions.edit.select_all()
        selected_text = actions.edit.selected_text()

        tokens = split_tokens_approach_from_left(selected_text)
        token, index = find_first_last_char_based_token(tokens, letter_1, letter_2)

        actions.edit.file_start()
        # word_right won't behave correctly if it starts with a space
        if selected_text.startswith(" "):
            actions.key("delete")

        # Put cursor before word
        for i in range(index):
            actions.edit.word_right()

    def fix_text_chuck(letter_1: str, letter_2: str = ""):
        """Fix text chuck"""
        actions.edit.select_all()
        selected_text = actions.edit.selected_text()
        tokens = selected_text.split(' ')
        target_token, index = find_first_last_char_based_token(tokens, letter_1, letter_2)
        new_text = tokens[:index] + tokens[index + 1:]
        actions.user.paste(" ".join(new_text))