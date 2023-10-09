import os
import re
from itertools import islice
from pathlib import Path

from talon import Module, actions, app, ui

APPS_DIR = Path(__file__).parent.parent.parent / "apps"
GAMES_DIR = Path(__file__).parent.parent.parent / "games"

mod = Module()


@mod.action_class
class Actions:
    def talon_create_app_context(is_game: bool = False):
        """Create a new python context file for the current application"""
        active_app = ui.active_app()
        app_name = get_app_name(active_app.name)
        app_dir = APPS_DIR / app_name if not is_game else GAMES_DIR / app_name
        talon_file = app_dir / f"{app_name}.talon"
        python_file = app_dir / f"{get_platform_filename(app_name)}.py"

        talon_context = get_talon_context(app_name)
        python_context = get_python_context(active_app, app_name)

        if not app_dir.is_dir():
            os.mkdir(app_dir)

        talon_file_created = create_file(talon_file, talon_context)
        python_file_created = create_file(python_file, python_context)

        if talon_file_created or python_file_created:
            actions.user.file_manager_open_directory(str(app_dir))

    def talon_create_app_parrot_context(is_game: bool = False):
        """Create a new parrot python context file for the current application"""
        active_app = ui.active_app()
        app_name = get_app_name(active_app.name)
        app_dir = APPS_DIR / app_name if not is_game else GAMES_DIR / app_name
        python_file = app_dir / f"{get_platform_filename(app_name)}_parrot.py"

        python_context = get_parrot_python_context(active_app, app_name)

        if not app_dir.is_dir():
            os.mkdir(app_dir)

        python_file_created = create_file(python_file, python_context)

        if python_file_created:
            actions.user.file_manager_open_directory(str(app_dir))


def get_python_context(active_app: ui.App, app_name: str) -> str:
    return '''\
from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.apps.{app_name} = r"""
os: {os}
and {app_context}
"""
ctx.matches = r"""
os: {os}
app: {app_name}
"""
# @mod.action_class
# class Actions:
'''.format(
        app_name=app_name,
        os=app.platform,
        app_context=get_app_context(active_app),
    )

def get_parrot_python_context(active_app: ui.App, app_name: str) -> str:
    app_context = get_app_context(active_app)
    return f'''\
from talon import Module, Context, actions
mod = Module()
ctx = Context()
ctx_parrot = Context()
ctx_parrot_default = Context()

mod.apps.{app_name} = r"""
{app_context}
"""

ctx.matches = r"""
app: {app_name}
"""

ctx_parrot.matches = r"""
app: {app_name}
mode: user.parrot
"""

ctx_parrot_default.matches = r"""
app: {app_name}
tag: user.parrot_default
"""

# ctx_parrot.settings = {{
#     "user.parrot_rpg_increment_y": 75,
#     "user.parrot_rpg_increment_x": 75,
#     "user.parrot_rpg_interaction_axis_y_pos": 75,
# }}

# @ctx.action_class("user")
# class Actions:

# @ctx_parrot_default.action_class("user")
# class Actions:
'''


def get_talon_context(app_name: str) -> str:
    return f"""app: {app_name}
-
"""


def get_platform_filename(app_name: str) -> str:
    if app.platform == "mac":
        return f"{app_name}_{app.platform}"
    return app_name


def get_app_context(active_app: ui.App) -> str:
    if app.platform == "mac":
        return f"app.bundle: {active_app.bundle}"
    if app.platform == "windows":
        return f"app.exe: {active_app.exe.split(os.path.sep)[-1]}"
    return f"app.name: {active_app.name}"


def get_app_name(text: str, max_len=20) -> str:
    pattern = re.compile(r"[A-Z][a-z]*|[a-z]+|\d")
    return "_".join(
        list(islice(pattern.findall(text.replace(".exe", "")), max_len))
    ).lower()


def create_file(path: Path, content: str) -> bool:
    if path.is_file():
        actions.app.notify(f"Application context file '{path}' already exists")
        return False

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return True