app: vscode
-
tag(): user.find
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.splits
tag(): user.tabs

settings():
    key_wait = 4
    insert_wait = 7

# Views
(show | focus) term | term (show | yes): user.vscode("workbench.action.terminal.focus")
hide term | term (hide | no | dog): user.vscode("workbench.action.togglePanel")
show (files | folders):
    user.vscode_focus_files()
    user.mouse_move_relative_window(197, 426)
show extensions:            user.vscode("workbench.view.extensions")
show outline:               user.vscode("outline.focus")
show run:                   user.vscode("workbench.view.debug")
show rack:                  user.vscode("workbench.action.toggleAuxiliaryBar")
focus search:               user.vscode("workbench.action.findInFiles")
focus exclude:              user.vscode("workbench.action.focusFilesToExclude")
focus include:              user.vscode("search.action.focusFilesToInclude")
show search:                user.vscode("workbench.view.search")
show changes:               user.vscode_focus_changes()
(show | focus) editor:      user.vscode("workbench.action.focusActiveEditorGroup")
(show | focus | hide | toggle) bar: user.vscode("workbench.action.toggleSidebarVisibility")

go view [<user.text>]:
    user.vscode("workbench.action.openView")
    insert(user.text or "")

window close: user.vscode("workbench.action.closeWindow")
#multiple_cursor.py support end

please [<user.text>]:
    user.vscode("workbench.action.showCommands")
    insert(user.text or "")

# Sidebar
bar (show | open | yes):
    user.vscode("workbench.action.toggleSidebarVisibility")
    user.mouse_move_relative_window(207, 425)
bar (hide | close | no):
    user.vscode("workbench.action.toggleSidebarVisibility")
bar explore:
    user.vscode("workbench.view.explorer")
    user.mouse_move_relative_window(207, 425)
bar extensions:
    user.vscode("workbench.view.extensions")
    user.mouse_move_relative_window(207, 425)
bar outline:
    user.vscode("outline.focus")
    user.mouse_move_relative_window(207, 425)
bar debug:
    user.vscode("workbench.view.debug")
    user.mouse_move_relative_window(207, 425)
bar source:
    user.vscode("workbench.view.scm")
    user.mouse_move_relative_window(207, 425)
bar file:
    user.vscode("workbench.files.action.showActiveFileInExplorer")
    user.mouse_move_relative_window(207, 425)
bar (grow | expand):        user.vscode("workbench.action.decreaseViewWidth")
bar shrink:                 user.vscode("workbench.action.increaseViewWidth")
(bar | explore) scout [{user.prose_formatter}] [<user.prose>]:
    user.vscode_focus_files()
    user.mouse_move_relative_window(263, 101)
    key("ctrl-f")
    user.insert_formatted(prose or "", prose_formatter or "NO_SPACES")
rack (show | open | yes):
    user.vscode("workbench.action.toggleAuxiliaryBar")
    user.mouse_move_relative_window(1752, 245)
rack (hide | close | no):
    user.vscode("workbench.action.toggleAuxiliaryBar")
(top | tabs | tab) (show | hide | yes | no): user.vscode("workbench.action.toggleTabsVisibility")
(file | files | bar) collapse: user.vscode("workbench.files.action.collapseExplorerFolders")

# Settings
show settings: user.vscode("workbench.action.openGlobalSettings")
show settings json: user.vscode("workbench.action.openSettingsJson")
show settings folder: user.vscode("workbench.action.openFolderSettings")
show settings folder json: user.vscode("workbench.action.openFolderSettingsFile")
show settings workspace: user.vscode("workbench.action.openWorkspaceSettings")
show settings workspace json: user.vscode("workbench.action.openWorkspaceSettingsFile")
show shortcuts: user.vscode("workbench.action.openGlobalKeybindings")
show shortcuts json: user.vscode("workbench.action.openGlobalKeybindingsFile")
show snippets: user.vscode("workbench.action.openSnippets")

show (markdown | preview):  user.vscode("markdown.showPreviewToSide")

# VSCode Snippets
snip (last | previous): user.vscode("jumpToPrevSnippetPlaceholder")
snip next: user.vscode("jumpToNextSnippetPlaceholder")

# Display
centered switch: user.vscode("workbench.action.toggleCenteredLayout")
fullscreen switch: user.vscode("workbench.action.toggleFullScreen")
theme switch: user.vscode("workbench.action.selectTheme")
wrap switch: user.vscode("editor.action.toggleWordWrap")
zen switch: user.vscode("workbench.action.toggleZenMode")

# Navigating files
^pop$:
    user.vscode("workbench.action.quickOpen")
    sleep(100ms)

pop <user.prose> [{user.file_extension}]:
    user.vscode("workbench.action.quickOpen")
    sleep(100ms)
    insert(prose)
    insert(file_extension or "")
    sleep(300ms)

pop sesh [<user.text>]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    user.insert_formatted(text or "", "DASH_SEPARATED,ALL_LOWERCASE")

pop (win | window) [<user.text>]:
    user.vscode("workbench.action.switchWindow")
    sleep(50ms)
    insert(text or "")

pop back:                   user.vscode("workbench.action.openPreviousRecentlyUsedEditor")
pop forward:                user.vscode("workbench.action.openNextRecentlyUsedEditor")
spring back:                user.vscode("workbench.action.navigateBack")
spring forward:             user.vscode("workbench.action.navigateForward")

pop last:
    user.vscode("workbench.action.openPreviousRecentlyUsedEditorInGroup")

pop next:
    user.vscode("workbench.action.openNextRecentlyUsedEditorInGroup")

(focus | show ) results:    user.vscode("search.action.focusSearchList")
search next:                user.vscode("search.action.focusNextSearchResult")
search last:                user.vscode("search.action.focusPreviousSearchResult")
change next:                user.vscode("workbench.action.compareEditor.nextChange")
change last:                user.vscode("workbench.action.compareEditor.previousChange")
change revert:              user.vscode("git.revertSelectedRanges")
spot last:                  user.vscode("workbench.action.navigatePreviousInEditLocations")
doc split:                  user.vscode("workbench.action.splitEditor")

# Language features
format document:            user.format_document()
refactor this:              user.vscode("editor.action.refactor")

# Problems
problem next:               user.vscode("editor.action.marker.nextInFiles")
problem last:               user.vscode("editor.action.marker.prevInFiles")
problem fix:                user.vscode("problems.action.showQuickFixes")
quick fix:                  user.vscode("editor.action.quickFix")

# Imports
imports organize:           user.vscode("editor.action.organizeImports")
imports add:                user.vscode_add_missing_imports()
imports fix:
    user.vscode_add_missing_imports()
    sleep(100ms)
    user.vscode("editor.action.organizeImports")

# Split
split left:                 user.vscode("workbench.action.moveEditorToLeftGroup")
split right:                user.vscode("workbench.action.moveEditorToRightGroup")
split up:                   user.vscode("workbench.action.moveEditorToAboveGroup")
split down:                 user.vscode("workbench.action.moveEditorToBelowGroup")

group up:                   user.vscode("workbench.action.focusAboveGroup")
group down:                 user.vscode("workbench.action.focusBelowGroup")
group (left | one):         user.vscode("workbench.action.focusLeftGroup")
group (right | two):        user.vscode("workbench.action.focusRightGroup")
group close:                user.vscode("workbench.action.closeEditorsAndGroup")
group close others:         user.vscode("workbench.action.closeEditorsInOtherGroups")
group (collapse | join | single): user.vscode("workbench.action.editorLayoutSingle")
group switch:               user.vscode("workbench.action.toggleEditorGroupLayout")
group reset:                user.vscode("workbench.action.evenEditorWidths")

term right:                 user.vscode("workbench.action.positionPanelRight")
term (bottom | low | down | bot): user.vscode("workbench.action.positionPanelBottom")
maximize | grow$:           user.vscode("workbench.action.toggleEditorWidths")
bridge:                     user.vscode("workbench.action.focusNextGroup")

# Terminal
term (max | min | zen | zen mode):
    user.vscode("workbench.action.alignPanelCenter")
    user.vscode("workbench.action.toggleMaximizedPanel")
term control:               user.vscode("workbench.panel.repl.view.focus")
term output:                user.vscode("workbench.panel.output.focus")
term problems:              user.vscode("workbench.panel.markers.view.focus")
term clear:                 key(ctrl-l)
(pop term | term pop) <user.text>: "z {text}\n"
(<user.show_list> term | term <user.show_list>) <user.text>: "z -l {text}\n"
(pop term | term pop) (last | switch): "z -\n"
term external:              user.vscode("workbench.action.terminal.openNativeConsole")
term new:                   user.vscode("workbench.action.terminal.new")
term next:                  user.vscode("workbench.action.terminal.focusNext")
term last:                  user.vscode("workbench.action.terminal.focusPrevious")
term split:                 user.vscode("workbench.action.terminal.split")
term zoom:                  user.vscode("workbench.action.toggleMaximizedPanel")
term trash:                 user.vscode("workbench.action.terminal.kill")
term scroll up:             user.vscode("workbench.action.terminal.scrollUp")
term scroll down:           user.vscode("workbench.action.terminal.scrollDown")
term grow:                  user.vscode("workbench.action.terminal.resizePaneUp")
term shrink:                user.vscode("workbench.action.terminal.resizePaneDown")
term bridge:                user.vscode("workbench.action.terminal.focusNextPane")
term <number_small>:        user.vscode_terminal(number_small)

katie:                      "cd "
katie up:                   "cd ..\n"
katie <user.text>:          "cd {text}\n"
try katie <user.text>:      "cd {text}\t\n"
katie try <user.text>:      "cd {text}\t\n"
lisa:                       "ls\n"
history [<number>]:         "history | tail -{number or 20} | tac | code -\n"

# Hide sidebar and panel
zen mode:
    user.vscode("workbench.action.closeSidebar")
    user.vscode("workbench.action.closePanel")
    user.vscode("closeFindWidget")

# Files / Folders
folder open:                user.vscode("workbench.action.files.openFolder")
folder add:                 user.vscode("workbench.action.addRootFolder")
folder new:                 user.vscode("explorer.newFolder")
file open:                  user.vscode("workbench.action.files.openFile")
file new [<user.filename>]:
    user.vscode("explorer.newFile")
    "{filename or ''}"
[file | folder] (show | reveal) in desktop: user.vscode("revealFileInOS")
file reveal:                user.vscode("workbench.files.action.showActiveFileInExplorer")
show explorer:              user.vscode("revealFileInOS")
file copy path:             user.vscode("copyFilePath")
file copy relative:         user.vscode("copyRelativeFilePath")
file copy name:             user.vscode("andreas.copyFilename")
file remove:                user.vscode("andreas.removeFile")
file move:                  user.vscode("andreas.moveFile")
file next:                  user.vscode_file_next()
file last:                  user.vscode_file_last()
file revert:                user.vscode("git.clean")
file sibling [<user.filename>]:
    user.vscode("andreas.newFile", filename or "")
file rename [<user.filename>]:
    user.vscode("andreas.renameFile", filename or "")
file clone [<user.filename>]:
    user.vscode("andreas.duplicateFile", filename or "")

# Git
# most git commands in git.talon
get rebase head <number_small>: "git rebase -i HEAD~{number_small}\n"
git difftool head <number_small>: "git difftool HEAD~{number_small}\n"
git difftool cached:        "git difftool --cached\n"
git open file:              user.git_open_remote_file_url(false, false)
git copy file:              user.git_copy_remote_file_url(false, false)
git open branch:            user.git_open_remote_file_url(false, true)
git copy branch:            user.git_copy_remote_file_url(false, true)
git repo:                   user.git_open_url("Repo")
git issues:                 user.git_open_url("Issues")
git new issue:              user.git_open_url("NewIssue")
git pull requests:          user.git_open_url("PullRequests")
git (changes | diff):       user.vscode("git.openChange")
git changed files:          user.vscode("git.openAllChanges")
git reset all:              user.vscode("git.unstageAll")
git pull:                   user.vscode("git.pull")
git push:                   user.vscode("git.push")
git create tag:             user.vscode("git.createTag")
git push tags:              user.vscode("git.pushTags")
git open:                   user.vscode("git.openFile")
git stash:                  user.vscode("git.stash")
git pop stash:              user.vscode("git.stashPop")
git merge:                  user.vscode("git.merge")
git merge {user.git_branch}:
    user.vscode("git.merge")
    sleep(50ms)
    "{git_branch}"

git checkout clip:
    "git checkout {clip.text()}\n"

git cherry pick clip:
    "git cherry-pick {clip.text()}\n"

git commit [<user.text>]:
    user.vscode("git.commit")
    sleep(300ms)
    text = user.format_text(text or "", "CAPITALIZE_FIRST_WORD")
    "{text}"

git close:
    app.tab_close()
    user.vscode("workbench.action.terminal.focus")

# Folding
fold recursive:             user.vscode("editor.foldRecursively")
unfold recursive:           user.vscode("editor.unfoldRecursively")
fold all:                   user.vscode("editor.foldAll")
unfold all:                 user.vscode("editor.unfoldAll")
fold comments:              user.vscode("editor.foldAllBlockComments")

# Find a symbol
scout symbol [<user.text>]$:
    user.vscode("workbench.action.showAllSymbols")
    sleep(50ms)
    user.insert_formatted(text or "", "PRIVATE_CAMEL_CASE")

# CSV
align columns:              user.vscode("rainbow-csv.Align")
shrink columns:             user.vscode("rainbow-csv.Shrink")

# Misc
window reload:              user.vscode("workbench.action.reloadWindow")
disk raw:                   user.save_without_formatting()
disk files:                 user.vscode("workbench.action.files.saveFiles")

diswap:
    edit.save()
    key(alt:down)
    key(tab)
    sleep(50ms)
    key(alt:up)
    sleep(300ms)

disclose:
    key(esc:5)
    edit.save()
    sleep(300ms)
    key(ctrl-w)

wrap dog:                   user.vscode("editor.action.toggleWordWrap")

copy command id:            user.copy_command_id()
scout again:                user.vscode("rerunSearchEditorSearch")
generate range [from <number_small>]:
    user.vscode("andreas.generateRange", number_small or 1)

snip last:                  user.vscode("jumpToPrevSnippetPlaceholder")
[snip] next:                user.vscode("jumpToNextSnippetPlaceholder")

change language [<user.text>]:
    user.change_language(text or "")

please [<user.text>]$:
    user.vscode("workbench.action.showCommands")
    "{user.text or ''}"

jest:                       code.complete()
jest <user.cursorless_target>:
    user.cursorless_command("setSelectionAfter", cursorless_target)
    code.complete()
log <user.cursorless_target>:
    user.insert_snippet_with_cursorless_target("printFullStatement", "0", cursorless_target)
break:
    user.vscode("hideSuggestWidget")
    key("enter")

dismiss:
    user.vscode("notifications.hideList")
    user.vscode("notifications.hideToasts")
    user.vscode("workbench.action.terminal.hideSuggestWidget")
    user.vscode("hideSuggestWidget")

# Tabs
tab keep:                   user.vscode("workbench.action.keepEditor")
tab {self.letter} [{self.letter}]:
    user.run_rpc_command("andreas.focusTab", "{letter_1}{letter_2 or ''}")
tab yep:
    key(tab)
    sleep(50ms)
    key(enter)

# Save and restore tabs extension
tab group (disk | save):    user.vscode("saveRestoreEditors.cleanRestoreEditors")
tab group update:           user.vscode("saveRestoreEditors.resaveEditors")
tab group (open | pop | load | list) [<user.text>]:
    user.vscode("saveRestoreEditors.restoreEditors")
    sleep(100ms)
    insert(text or "")
tab group delete:           user.vscode("saveRestoreEditors.cleanPopSavedEditors")

# chuck bounding gust
# and fine

# take three tokens gust
# and fine

# chuck block gust
# and fine

# ^and <cursorless_target>:
#     user.cursorless_command("setSelectionAfter", cursorless_target)