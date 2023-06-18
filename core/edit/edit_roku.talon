# Navigation
tug:                        edit.left()
drain:                      edit.word_left()
push:                       edit.right()
step:                       edit.word_right()
north:                      edit.up()
south:                      edit.down()
head:                       edit.line_start()
tail:                       edit.line_end()

# Selecting
<user.select> lefter:       edit.extend_word_left()
<user.select> writer:       edit.extend_word_right()
take head:                  edit.extend_line_start()
take tail:                  edit.extend_line_end()

# Delete
scratch:                    edit.delete()
drill:                      user.delete_right()
scratcher:
    edit.extend_word_left()
    edit.delete()
swallow:
    edit.extend_word_right()
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

# Copy commands
copy lefter:
    edit.extend_word_left()
    edit.copy()

copy righter:
    edit.extend_word_right()
    edit.copy()

#cut commands
cut lefter:
    edit.extend_word_left()
    edit.cut()

cut righter:
    edit.extend_word_right()
    edit.cut()

# Other
pour:                       edit.line_insert_down()
drink:                      edit.line_insert_up()
disk:                       edit.save()
disk all:                   edit.save_all()
nope:                       edit.undo()
