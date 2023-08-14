app: windows_explorer
-
tag(): user.tabs
tag(): user.find
tag(): user.file_manager

(show | hide | toggle) hints: key(alt-;)
hints | hint (show | hide | yes | no): key(alt-;)

view (large | big | largest): key(ctrl-shift-1)
view (medium | mid):        key(ctrl-shift-2)
view small:                 key(ctrl-shift-3)
view smallest:              key(ctrl-shift-4)
view list:                  key(ctrl-shift-5)
view details:               key(ctrl-shift-6)

view [<user.text>]:
    key(ctrl-l)
    key(delete)
    key(down)
    insert(user.text or "")

window clone:               key(ctrl-n)
folder (new | make):        key(ctrl-shift-n)

tab clone:
    key(ctrl-l)
    key(ctrl-c)
    key(ctrl-t)
    key(ctrl-l)
    key(ctrl-v)
    key(enter)
