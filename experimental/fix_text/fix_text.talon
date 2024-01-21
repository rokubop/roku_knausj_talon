# Fix text by targeting the first and last letter of a word
# Performs operation on a "select all" scope
fix <user.letter> [<user.letter>]: user.fix_text_change(letter_1, letter_2 or "")
fix chuck <user.letter> [<user.letter>]: user.fix_text_chuck(letter_1, letter_2 or "")
fix pre <user.letter> [<user.letter>]: user.fix_text_pre(letter_1, letter_2 or "")
