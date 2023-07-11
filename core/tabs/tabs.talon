tag: user.tabs
-

tab last:                   app.tab_previous()
tab next:                   app.tab_next()
tab <number_small>:         user.tab_jump(number_small)
tab minus <number_small>:   user.tab_jump_from_back(number_small)
tab final:                  user.tab_final()
tab back:                   user.tab_back()
tab left:                   user.tab_move_left()
tab right:                  user.tab_move_right()
tab (new | make):           app.tab_open()
tab clone:                  user.tab_duplicate()
tab reopen:                 app.tab_reopen()
tab pop:                    app.tab_detach()

tab close:                  app.tab_close()
tab close [other | others]: user.tab_close_all_others()
tab close (other | others) [in] group: user.tab_close_others()
tab close (all | oliver):   user.tab_close_all()
tab close left:             user.tab_close_left()
tab close right:            user.tab_close_right()
tab close first:            user.tab_close_first()
tab last close:
    app.tab_previous()
    sleep(50ms)
    app.tab_close()
tab next close:
    app.tab_next()
    sleep(50ms)
    app.tab_close()
tab <number_small> close:
    user.tab_jump(number_small)
    sleep(50ms)
    app.tab_close()
tab close final:
    user.tab_final()
    sleep(50ms)
    app.tab_close()
