open {user.website}: user.open_url(website)
{user.search_engine} <user.find> <user.text>$:
    user.search_with_search_engine(search_engine, user.text)
{user.search_engine} [<user.find>] (that | this):
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)

# roku additions
{user.search_engine} [<user.find>] <user.clip>:
    text = clip.text()
    user.search_with_search_engine(search_engine, text)

ask chat <user.text>$:
    user.search_with_chat_gpt(user.text)
ask chat <user.clip>$:
    text = clip.text()
    user.search_with_chat_gpt(user.text)
ask chat (that | this)$:
    text = edit.selected_text()
    user.search_with_chat_gpt(user.text)