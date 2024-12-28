import csv
import os
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("git_command", desc="Git commands.")
mod.list("git_argument", desc="Command-line git options and arguments.")
mod.list("git_branch", desc="Git branch")

ctx.lists["self.git_branch"] = ["main", "master", "dev"]


@mod.capture(rule="{user.git_argument}+")
def git_arguments(m) -> str:
    """A non-empty sequence of git command arguments, preceded by a space."""
    return " " + " ".join(m.git_argument_list)
