"""
Stores terms that are used in many different places
"""
from talon import Module

mod = Module()

SELECT = "take"
TELEPORT = "pop"
OPERATOR = "make | add"
DELETE = "chuck"
FIND = "scout"
SHOW_LIST = "list"
CLIP = "clip"

@mod.capture(rule=SELECT)
def select(m) -> str:
    """Term for select"""
    return str(m)


@mod.capture(rule=TELEPORT)
def teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    print("teleport")
    return str(m)


@mod.capture(rule=OPERATOR)
def operator(m) -> str:
    """Prefix for operators"""
    return str(m)


@mod.capture(rule=DELETE)
def delete(m) -> str:
    """Verb to use for commands that delete things"""
    return str(m)


@mod.capture(rule=FIND)
def find(m) -> str:
    """Verb to use for commands that find things"""
    return str(m)


@mod.capture(rule=SHOW_LIST)
def show_list(m) -> str:
    """Verb to use for commands that show lists"""
    return str(m)

@mod.capture(rule=CLIP)
def clip(m) -> str:
    """Name of the clipboard"""
    return str(m)
