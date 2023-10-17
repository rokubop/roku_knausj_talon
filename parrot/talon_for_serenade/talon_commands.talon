# these commands will only be active when Talon is awake
mode: command
-
# parrot(pop): user.log_parrot_io('pop')
# parrot(hiss): user.log_parrot_io('hiss')

serenade (wake | sleep): key(alt-space)
voice toggle:
    key(alt-space)
    speech.disable()
# talon sleep: speech.disable()
