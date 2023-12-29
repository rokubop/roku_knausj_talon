mode: all
speech.engine: wav2letter
-
^go to sleep [<phrase>]$:   speech.disable()
# ^wake up$:
#     speech.enable()
#     user.unset_hard_sleep()
#     user.hud_publish_mouse_particle('float_up', '36d96a')
