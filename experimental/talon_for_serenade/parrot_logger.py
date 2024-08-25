from talon import Module
from datetime import datetime

mod = Module()

@mod.action_class
class Actions:
    def log_parrot_io(text: str):
        """Log parrot for stream with Serenade"""
        # TODO: clear the file after some time
        # if it gets too big.
        with open('parrot.log', 'a') as file:
            file.write(f'{datetime.now()}{text}\n')