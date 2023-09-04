os: windows
-
^ax$: key(alt-;)

^ax screen$: key(ctrl-alt-;)

^ax all [<user.text>]: user.fluent_search(text or "")
^swap <user.text>:
    user.fluent_search(text or "")
    sleep(0.1)
    key(enter)

^ax [<user.text>]$:
    user.fluent_search_in_app(text or "", false)