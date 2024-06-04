import json
import os
from talon import Context, Module, actions, app, clip
import re
from typing import Any

PATTERN_RE = re.compile(r"Untitled-\d$")

is_mac = app.platform == "mac"
vscode = actions.user.vscode

ctx = Context()
mac_ctx = Context()
mod = Module()
mod.apps.vscode = """
os: mac
and app.bundle: com.microsoft.VSCode
os: mac
and app.bundle: com.microsoft.VSCodeInsiders
os: mac
and app.bundle: com.visualstudio.code.oss
"""
mod.apps.vscode = """
os: linux
and app.name: Code
os: linux
and app.name: code-oss
os: linux
and app.name: code-insiders
os: linux
and app.name: VSCodium
os: linux
and app.name: Codium
"""
mod.apps.vscode = """
os: windows
and app.name: Visual Studio Code
os: windows
and app.name: Visual Studio Code Insiders
os: windows
and app.name: Visual Studio Code - Insiders
os: windows
and app.exe: Code.exe
os: windows
and app.exe: Code-Insiders.exe
os: windows
and app.name: VSCodium
os: windows
and app.exe: VSCodium.exe
"""

ctx.matches = r"""
app: vscode
"""
mac_ctx.matches = r"""
os: mac
app: vscode
"""


@ctx.action_class("app")
class AppActions:
    # talon app actions
    def tab_open():
        actions.user.vscode("workbench.action.files.newUntitledFile")

    def tab_close():
        actions.user.vscode("workbench.action.closeActiveEditor")

    def tab_next():
        actions.user.vscode("workbench.action.nextEditorInGroup")

    def tab_previous():
        actions.user.vscode("workbench.action.previousEditorInGroup")

    def tab_reopen():
        actions.user.vscode("workbench.action.reopenClosedEditor")

    def window_close():
        actions.user.vscode("workbench.action.closeWindow")

    def window_open():
        actions.user.vscode("workbench.action.newWindow")


@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment():
        actions.user.vscode("editor.action.commentLine")

    def complete():
        vscode("editor.action.triggerSuggest")

    def language() -> str:
        # New untitled files are markdown in vscode
        if is_untitled(actions.win.filename()):
            return "markdown"
        return actions.next()


@ctx.action_class("edit")
class EditActions:
    # talon edit actions
    def indent_more():
        actions.user.vscode("editor.action.indentLines")

    def indent_less():
        actions.user.vscode("editor.action.outdentLines")

    def save_all():
        actions.user.vscode("workbench.action.files.saveAll")

    def find(text=None):
        if is_mac:
            actions.key("cmd-f")
        else:
            actions.key("ctrl-f")
        if text is not None:
            actions.insert(text)

    def line_swap_up():
        actions.key("alt-up")

    def line_swap_down():
        actions.key("alt-down")

    def line_clone():
        actions.key("shift-alt-down")

    def line_insert_down():
        actions.user.vscode("editor.action.insertLineAfter")

    def line_insert_up():
        actions.user.vscode("editor.action.insertLineBefore")

    def jump_line(n: int):
        actions.user.vscode("workbench.action.gotoLine")
        actions.insert(str(n))
        actions.key("enter")
        actions.edit.line_start()


@ctx.action_class("win")
class WinActions:
    def filename():
        title = actions.win.title()
        # this doesn't seem to be necessary on VSCode for Mac
        # if title == "":
        #    title = ui.active_window().doc

        if is_mac:
            result = title.split(" — ")[0]
        else:
            result = title.split(" - ")[0]

        if "." in result:
            return result

        return ""


vscode_view = "files"

@mod.action_class
class Actions:
    def insert_snippet_with_cursorless_target(
        name: str, variable_name: str, target: Any
    ):
        """Insert snippet <name> with cursorless target <target>"""
        actions.user.insert_snippet_by_name(
            name,
            {variable_name: actions.user.cursorless_get_text(target)},
        )

    def vscode_log_full(text: str):
        """console log"""
        actions.user.paste(f"console.log('{text}', {text});")

    def vscode_terminal(number: int):
        """Activate a terminal by number"""
        actions.user.vscode(f"workbench.action.terminal.focusAtIndex{number}")

    def command_palette():
        """Show command palette"""
        actions.key("ctrl-shift-p")

    def save_without_formatting():
        """Save current document without formatting"""
        actions.user.vscode("hideSuggestWidget")
        actions.user.vscode("workbench.action.files.saveWithoutFormatting")

    def tab_force_close():
        """Forces the current tab to close"""
        actions.user.vscode("workbench.action.revertAndCloseActiveEditor")

    def vscode_focus_files():
        """Focus files"""
        global vscode_view
        vscode_view = "files"
        actions.user.vscode("workbench.explorer.fileView.focus")

    def vscode_focus_changes():
        """Focus changes"""
        global vscode_view
        vscode_view = "scm"
        actions.user.vscode("workbench.view.scm")

    def get_teleport_destination(text: str):
        """Get teleport destination"""
        # title = actions.win.title()
        title = actions.user.vscode("copyFilePath")
        if re.search("roku_talon", title):
            print("I got it")

        # actions.user.vscode("workbench.action.quickOpen")
        # actions.sleep("100ms")
        # actions.insert(",")
        # actions.insert(text or "")
        # # actions.insert(file_extension or "")
        # actions.sleep("400ms")
        # actions.key("enter")
        # actions.sleep("150ms")

    def vscode_file_next():
        """Go to next file"""
        if vscode_view == "scm":
            actions.user.vscode("workbench.scm.focus")
        else:
            actions.user.vscode("workbench.files.action.focusFilesExplorer")
        actions.key("down space")

    def vscode_file_last():
        """Go to last file"""
        if vscode_view == "scm":
            actions.user.vscode("workbench.scm.focus")
        else:
            actions.user.vscode("workbench.files.action.focusFilesExplorer")
        actions.key("up space")

    # argument for passing a file type is not working
    # def find_sibling_file(file_type: str = None):
    #     """Find sibling file based on file name"""
    #     full_name = actions.user.vscode_get("andreas.getFilename")
    #     index = full_name.rfind(".")
    #     print("full_name", full_name)
    #     if index < 0:
    #         return
    #     short_name = full_name[:index]

    #     # not working
    #     if file_type:
    #         sibling_extension = file_type
    #     else:
    #         extension = full_name[index + 1 :]
    #         sibling_extension = actions.user.get_extension_sibling(extension)
    #         if not sibling_extension:
    #             return

    #     sibling_full_name = f"{short_name}.{sibling_extension}"
    #     actions.user.find_file(sibling_full_name)

    def copy_command_id():
        """Copy the command id of the focused menu item"""
        actions.key("tab:2 enter")
        actions.sleep("750ms")
        json_text = actions.edit.selected_text()
        command_id = json.loads(json_text)["command"]
        actions.app.tab_close()
        clip.set_text(command_id)

    def transform_path_for_search(path: str, first_x: int, last_y: int, append_word: str):
        """Transform a path for searching"""
        components = path.replace("\\","/").split("/")

        if len(components) < first_x + last_y:
            raise ValueError('Not enough components in the path to remove')

        components = components[first_x:-last_y]
        components.append(append_word)
        modified_path = os.sep.join(components)

        return modified_path

    def find_sibling_file(text: str = None, first_x: int = 0, last_y: int = 1):
        """Find sibling file based on file name"""
        actions.user.vscode("copyFilePath")
        new_path = actions.user.transform_path_for_search(clip.text(), first_x, last_y, text or "")
        actions.user.find_file(new_path)

    def vscode_add_missing_imports():
        """Add all missing imports"""
        actions.user.vscode_with_plugin(
            "editor.action.sourceAction",
            {"kind": "source.addMissingImports", "apply": "first"},
        )

@mac_ctx.action_class("user")
class MacUserActions:
    def command_palette():
        actions.key("cmd-shift-p")


@ctx.action_class("user")
class UserActions:
    # splits.py support begin
    def split_clear_all():
        actions.user.vscode("workbench.action.editorLayoutSingle")

    def split_clear():
        actions.user.vscode("workbench.action.joinTwoGroups")

    def split_flip():
        actions.user.vscode("workbench.action.toggleEditorGroupLayout")

    def split_maximize():
        actions.user.vscode("workbench.action.maximizeEditor")

    def split_reset():
        actions.user.vscode("workbench.action.evenEditorWidths")

    def split_last():
        actions.user.vscode("workbench.action.focusLeftGroup")

    def split_next():
        actions.user.vscode_and_wait("workbench.action.focusRightGroup")

    def split_window_down():
        actions.user.vscode("workbench.action.moveEditorToBelowGroup")

    def split_window_horizontally():
        actions.user.vscode("workbench.action.splitEditorOrthogonal")

    def split_window_left():
        actions.user.vscode("workbench.action.moveEditorToLeftGroup")

    def split_window_right():
        actions.user.vscode("workbench.action.moveEditorToRightGroup")

    def split_window_up():
        actions.user.vscode("workbench.action.moveEditorToAboveGroup")

    def split_window_vertically():
        actions.user.vscode("workbench.action.splitEditor")

    def split_window():
        actions.user.vscode("workbench.action.splitEditor")

    # splits.py support end

    # multiple_cursor.py support begin
    # note: vscode has no explicit mode for multiple cursors
    def multi_cursor_add_above():
        actions.user.vscode("editor.action.insertCursorAbove")

    def multi_cursor_add_below():
        actions.user.vscode("editor.action.insertCursorBelow")

    def multi_cursor_add_to_line_ends():
        actions.user.vscode("editor.action.insertCursorAtEndOfEachLineSelected")

    def multi_cursor_disable():
        actions.key("escape")

    def multi_cursor_enable():
        actions.skip()

    def multi_cursor_select_all_occurrences():
        actions.user.vscode("editor.action.selectHighlights")

    def multi_cursor_select_fewer_occurrences():
        actions.user.vscode("cursorUndo")

    def multi_cursor_select_more_occurrences():
        actions.user.vscode("editor.action.addSelectionToNextFindMatch")

    def multi_cursor_skip_occurrence():
        actions.user.vscode("editor.action.moveSelectionToNextFindMatch")

    def tab_jump(number: int):
        actions.user.vscode(f"workbench.action.openEditorAtIndex{number}")

    def tab_back():
        actions.user.vscode("workbench.action.openPreviousRecentlyUsedEditorInGroup")

    def tab_final():
        if is_mac:
            actions.user.vscode("workbench.action.lastEditorInGroup")
        else:
            actions.key("alt-0")

    def tab_close_all():
        actions.user.vscode("workbench.action.closeAllEditors")

    def tab_close_others():
        actions.user.vscode("workbench.action.closeOtherEditors")


    def tab_close_all_others():
        actions.user.vscode("workbench.action.closeEditorsInOtherGroups")
        actions.user.vscode("workbench.action.closeOtherEditors")

    def tab_duplicate():
        actions.user.vscode("workbench.action.splitEditor")


    # splits.py support begin
    def split_number(index: int):
        """Navigates to a the specified split"""
        if index < 9:
            if is_mac:
                actions.key(f"cmd-{index}")
            else:
                actions.key(f"ctrl-{index}")

    # splits.py support end

    # find_and_replace.py support begin

    def find(text: str):
        """Triggers find in current editor"""
        if is_mac:
            actions.key("cmd-f")
        else:
            actions.key("ctrl-f")
        if text:
            actions.insert(text)

    def find_next():
        actions.user.vscode("editor.action.nextMatchFindAction")

    def find_previous():
        actions.user.vscode("editor.action.previousMatchFindAction")

    def find_everywhere(text: str):
        """Triggers find across project"""
        if is_mac:
            actions.key("cmd-shift-f")
        else:
            actions.key("ctrl-shift-f")

        if text:
            actions.insert(text)

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""
        if is_mac:
            actions.key("alt-cmd-c")
        else:
            actions.key("alt-c")

    def find_file(text: str = None):
        vscode("workbench.action.quickOpen")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""
        if is_mac:
            actions.key("cmd-alt-w")
        else:
            actions.key("alt-w")

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""
        if is_mac:
            actions.key("cmd-alt-r")
        else:
            actions.key("alt-r")

    def find_replace_toggle_preserve_case():
        actions.key("alt-p")

    def find_replace_confirm():
        actions.key("enter")

    def find_replace_confirm_all():
        actions.key("ctrl-alt-enter")

    def replace(text: str):
        """Search and replaces in the active editor"""
        if is_mac:
            actions.key("alt-cmd-f")
        else:
            actions.key("ctrl-h")

        if text:
            actions.insert(text)

    def replace_everywhere(text: str):
        """Search and replaces in the entire project"""
        if is_mac:
            actions.key("cmd-shift-h")
        else:
            actions.key("ctrl-shift-h")

        if text:
            actions.insert(text)

    def replace_confirm():
        """Confirm replace at current position"""
        if is_mac:
            actions.key("shift-cmd-1")
        else:
            actions.key("ctrl-shift-1")

    def replace_confirm_all():
        """Confirm replace all"""
        if is_mac:
            actions.key("cmd-enter")
        else:
            actions.key("ctrl-alt-enter")

    def select_previous_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("shift-enter esc")

    def select_next_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("esc")

    def insert_snippet(body: str):
        actions.user.run_rpc_command("editor.action.insertSnippet", {"snippet": body})

def is_untitled(filename: str):
    return PATTERN_RE.search(filename) is not None