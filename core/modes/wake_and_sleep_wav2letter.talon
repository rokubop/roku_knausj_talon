mode: all
speech.engine: wav2letter
-
^go to sleep [<phrase>]$:   speech.disable()
^[<phrase>] (wake up)+$:    speech.enable()
