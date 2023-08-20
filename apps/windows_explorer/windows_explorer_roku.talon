app: windows_explorer
-
tag(): user.tabs
tag(): user.find
tag(): user.file_manager


view (large | big | largest): key(ctrl-shift-1)
view (medium | mid):        key(ctrl-shift-2)
view small:                 key(ctrl-shift-3)
view smallest:              key(ctrl-shift-4)
view list:                  key(ctrl-shift-5)
view details:               key(ctrl-shift-6)

focus path | path focus:                      key(ctrl-l)
copy path | path copy:
    key(ctrl-l)
    key(ctrl-c)
view [<user.text>]:
    key(ctrl-l)
    key(delete)
    key(down)
    insert(user.text or "")

window clone:               key(ctrl-n)
folder (new | make):        key(ctrl-shift-n)

tab clone | path clone | clone path | clone tab:
    key(ctrl-l)
    key(ctrl-c)
    key(ctrl-t)
    key(ctrl-l)
    key(ctrl-v)
    key(enter)

open in powershell:
    key(ctrl-l)
    insert("powershell")
    key(enter)

open in prompt:
    key(ctrl-l)
    insert("cmd")
    key(enter)

open (in | with) (wsl | ubuntu): user.open_explorer_path_in_wsl()
