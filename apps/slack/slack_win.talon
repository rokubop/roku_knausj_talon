os: windows
app: slack
-

show help: key(ctrl-/)

bar (show | hide) | (show | hide) bar:      key(ctrl-shift-d)
rack (show | hide) | (show | hide) rack:    key(ctrl-.)

<user.teleport> unreads:                 key(ctrl-shift-a)
<user.teleport> threads:                 user.slack_open_search_result("Threads")
<user.teleport> [direct] messages:       key(ctrl-shift-k)
<user.teleport> (mentions | reactions):  key(ctrl-shift-m)
<user.teleport> drafts:                  user.slack_open_search_result("Drafts")
<user.teleport> (server | workspace) [next]: key(ctrl-tab)
<user.teleport> (server | workspace) last: key(ctrl-shift-tab)
<user.teleport> last: key(alt-left)
<user.teleport> next: key(alt-right)

<user.find> [channel] [<user.text>]:
    key(ctrl-k)
    "{text or ''}"

<user.teleport> [channel] [<user.text>]:
    user.slack_open_search_result(text or "")

[<user.teleport>] server <number_small>: key("ctrl-{number_small}")

please [<user.text>]$:
    key(ctrl-k)
    sleep(100ms)
    edit.delete()
    sleep(100ms)
    "{text or ''}"

channel last:               key(alt-up)
channel next:               key(alt-down)
channel unread last:        key(alt-shift-up)
channel unread next:        key(alt-shift-down)
next unread:                key(alt-shift-down)

edit last:                  key(ctrl-up)
edit:                       key(e)

format code:                key(ctrl-shift-c)
format [code] block:        key(ctrl-alt-shift-c)
format quote:               key(ctrl-shift-9)
# tag(): user.messaging
# tag(): user.emoji
# # Workspaces
# workspace <number>: key("ctrl-{number}")
# # Channel
# (slack | lack) [channel] info: key(ctrl-shift-i)
# # Navigation
# focus (move | next): key(ctrl-`)
# (section | zone) [next]: key(f6)
# (section | zone) (previous | last): key(shift-f6)
# (slack | lack) [direct] messages: key(ctrl-shift-k)
# (slack | lack) threads: key(ctrl-shift-t)
# (slack | lack) (history [next] | back | backward): key(alt-left)
# (slack | lack) forward: key(alt-right)
# (element | bit) [next]: key(tab)
# (element | bit) (previous | last): key(shift-tab)
# (slack | lack) (my stuff | activity): key(ctrl-shift-m)
# (slack | lack) directory: key(ctrl-shift-e)
# (slack | lack) (starred [items] | stars): key(ctrl-shift-s)
# (slack | lack) unread [messages]: key(ctrl-shift-a)
# # Messaging
# grab left: key(shift-up)
# grab right: key(shift-down)
# add line: key(shift-enter)
# #"(slack | lack) (slap | slaw | slapper): [key(cmd-right) key(shift-enter")],
# (slack | lack) (react | reaction): key(ctrl-shift-\)
# (insert command | commandify): key(ctrl-shift-c)
# insert code: insert("```")
# (slack | lack) (bull | bullet | bulleted) [list]: key(ctrl-shift-8)
# (slack | lack) (number | numbered) [list]: key(ctrl-shift-7)
# (slack | lack) (quotes | quotation): key(ctrl-shift-9)
# bold: key(ctrl-b)
# (italic | italicize): key(ctrl-i)
# (strike | strikethrough): key(ctrl-shift-x)
# (slack | lack) snippet: key(ctrl-shift-enter)
# # Calls
# ([toggle] mute | unmute): key(m)
# (slack | lack) ([toggle] video): key(v)
# (slack | lack) invite: key(a)
# # Miscellaneous
# (slack | lack) shortcuts: key(ctrl-/)
# emote <user.text>: "{text}"
# toggle left sidebar: key(ctrl-shift-d)
# toggle right sidebar: key(ctrl-.)

# # DEPRECATED
# (move | next) focus:
#     app.notify("please use the voice command 'focus next' instead of 'next focus'")
#     key(ctrl-`)
# [next] (section | zone):
#     app.notify("please use the voice command 'section next' instead of 'next section'")
#     key(f6)
# (previous | last) (section | zone):
#     app.notify("please use the voice command 'section last' instead of 'last section'")
#     key(shift-f6)
# [next] (element | bit):
#     app.notify("please use the voice command 'element next' instead of 'next element'")
#     key(tab)
# (previous | last) (element | bit):
#     app.notify("please use the voice command 'element last' instead of 'last element'")
#     key(shift-tab)
