# Navigation
tug:                        edit.left()
drain:                      edit.word_left()
push:                       edit.right()
step:                       edit.word_right()
north:                      edit.up()
south:                      edit.down()
head:                       edit.line_start()
tail:                       edit.line_end()
scout:                      edit.find()
yep:                        key(enter)
scrape:                     key(escape)
pour | lap:                 edit.line_insert_down()
drink:                      edit.line_insert_up()
disk:                       edit.save()
new disk | disk new | new diss | disk as: user.save_as()
disk all:                   edit.save_all()
nope:                       edit.undo()
scratch:                    edit.delete()
drill:                      user.delete_right()
smart paste | show clip:    key(win-v)
scratcher: key(ctrl-backspace)
driller:
    edit.extend_word_right()
    edit.delete()

slapper | new graph:
    edit.line_insert_down()
    edit.line_insert_down()

# Navigation
scroll up:                  edit.page_up()
scroll down:                edit.page_down()
pre line:                   edit.line_start()
post line:                  edit.line_end()
pre file | go top:          edit.file_start()
post file | go bottom:      edit.file_end()
page up:                    edit.page_up()
page down:                  edit.page_down()

# Selecting
<user.select> lefter:              edit.extend_word_left()
<user.select> writer:              edit.extend_word_right()
# take head:                       edit.extend_line_start()
# take tail:                       edit.extend_line_end()
<user.select> (all| file):         edit.select_all()
<user.select> line:                edit.select_line()
<user.select> head [line]:         user.select_line_start()
<user.select> tail [line]:         user.select_line_end()
<user.select> left:                edit.extend_left()
<user.select> right:               edit.extend_right()
<user.select> up:                  edit.extend_line_up()
<user.select> down:                edit.extend_line_down()
<user.select> word:                edit.select_word()
<user.select> word left:           edit.extend_word_left()
<user.select> word right:          edit.extend_word_right()
<user.select> head file:           edit.extend_file_start()
<user.select> tail fine:           edit.extend_file_end()

# Indentation
indent [more] | indent this:              edit.indent_more()
(indent less | out dent | dedent this):   edit.indent_less()

# Delete
(clear | chuck) (all | file):         user.delete_all()
(clear | chuck) line:                 edit.delete_line()
(clear | chuck) line start:           user.delete_line_start()
(clear | chuck) line end:             user.delete_line_end()
clear left:                 edit.delete()
clear right:                user.delete_right()
clear up:
    edit.extend_line_up()
    edit.delete()
clear down:
    edit.extend_line_down()
    edit.delete()
clear word:                 edit.delete_word()
clear word left:
    edit.extend_word_left()
    edit.delete()
clear word right:
    edit.extend_word_right()
    edit.delete()
(clear | chuck) head [line]:
    edit.extend_line_start()
    edit.delete()
(clear | chuck) tail [line]:
    edit.extend_line_end()
    edit.delete()
(clear | chuck) head file:
    edit.extend_file_start()
    edit.delete()
(clear | chuck) tail file:
    edit.extend_file_end()
    edit.delete()
<user.delete> head:
    edit.extend_line_start()
    edit.delete()
<user.delete> tail:
    edit.extend_line_end()
    edit.delete()
<user.delete> all:
    edit.select_all()
    edit.delete()

# Copy
copy that:                  edit.copy()
copy (all | file):          user.copy_all()
copy line:                  user.copy_line()
copy line start:            user.copy_line_start()
copy line end:              user.copy_line_end()
copy word:                  user.copy_word()
copy word left:             user.copy_word_left()
copy word right:            user.copy_word_right()
copy head:
    edit.extend_line_start()
    edit.copy()
copy tail:
    edit.extend_line_end()
    edit.copy()
copy head file:
    edit.extend_file_start()
    edit.copy()
copy tail file:
    edit.extend_file_end()
    edit.copy()
copy lefter:
    edit.extend_word_left()
    edit.copy()
copy righter:
    edit.extend_word_right()
    edit.copy()

# Cut
carve that:                   edit.cut()
carve (all | file):           user.cut_all()
carve line:                   user.cut_line()
carve line start:             user.cut_line_start()
carve line end:               user.cut_line_end()
carve word:                   user.cut_word()
carve word left:              user.cut_word_left()
carve word right:             user.cut_word_right()
carve lefter:
    edit.extend_word_left()
    edit.cut()
carve righter:
    edit.extend_word_right()
    edit.cut()
carve head [line]:
    edit.extend_line_start()
    edit.cut()
carve tail [line]:
    edit.extend_line_end()
    edit.cut()
carve head file:
    edit.extend_file_start()
    edit.cut()
carve tail file:
    edit.extend_file_end()
    edit.cut()

# Paste
(pace | paste) that:        edit.paste()
(pace | paste) yep:
    edit.paste()
    key(enter)
paste match:                edit.paste_match_style()
(pace | paste) all:         user.paste_all()
(pace | paste) line:        user.paste_line()
(pace | paste) line start:  user.paste_line_start()
(pace | paste) line end:    user.paste_line_end()
(pace | paste) word:        user.paste_word()

# Duplication
clone that:                 edit.selection_clone()
clone line:                 edit.line_clone()

# Insert new line
new line above:             edit.line_insert_up()
new line [below] | slap:    edit.line_insert_down()

# Insert padding with optional symbols
(pad | padding):            user.insert_between(" ", " ")
(pad | padding) <user.symbol_key>+:
    insert(" ")
    user.insert_many(symbol_key_list)
    insert(" ")

# Undo/redo
undo that:                  edit.undo()
redo that:                  edit.redo()

# Save
file save:                  edit.save()
file save all:              edit.save_all()

copy paste:                 key(ctrl-c ctrl-v)

tab yep:
    key(tab)
    key(enter)
south yep:
    key(down)
    key(enter)
north yep:
    key(up)
    key(enter)

<user.operator> stack:      ": "
<user.operator> dash:       " - "
<user.operator> item:       "- "
<user.operator> task:       "- [ ] "
<user.operator> code:
    "``"
    edit.left()
<user.operator> code block: "```\n"