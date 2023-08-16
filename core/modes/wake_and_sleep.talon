#defines the commands that sleep/wake Talon
mode: all
-
^(welcome back)+$:
    user.mouse_wake()
    user.history_enable()
    user.talon_mode()
^(sleep all | drowse) [<phrase>]$:
    user.hud_publish_mouse_particle('float_up', '493fd9')
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^hard sleep [<phrase>]$:
    user.hud_publish_mouse_particle('float_up', '493fd9')
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
    user.set_hard_sleep()
^talon sleep [<phrase>]$:   speech.disable()
^(talon wake)+$:            speech.enable()

key(ctrl-f1):               speech.toggle()
# serenade (toggle | dog): user.serenade_toggle()
serenade (sleep | off):     user.serenade_sleep()
serenade (wake | on):       user.serenade_wake()
talon (wake | on):          user.talon_wake()
talon (sleep | off):        user.talon_sleep()
talon (toggle | dog):       user.talon_toggle()
toggle voice:               user.toggle_voice()
voice (toggle | dog):       user.toggle_voice()
go to sleep:                user.talon_sleep()
