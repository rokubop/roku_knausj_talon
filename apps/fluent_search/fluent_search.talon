os: windows
-
# In settings turn "Advanced On" in the top left
# Go to "Screen"
# Turn on "keep mouse position after a click"
# numb 4 red plex: right click ax target
^ax$: user.fluent_search_show_labels_window()

^ax screen$: user.fluent_search_show_labels_screen()

# ^ax all [<user.text>]: user.fluent_search(text or "")
^search <user.text>:
    user.fluent_search(text or "")
    sleep(0.1)
    # key(enter)

# ^ax [<user.text>]$:
#     user.fluent_search_in_app(text or "", fals