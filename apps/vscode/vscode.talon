app: vscode
-
tag(): user.find
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.snippets
tag(): user.splits
tag(): user.tabs

settings():
    key_wait = 2

(focus | show) term:        user.vscode("workbench.action.terminal.focus")
(focus | show) files:       user.vscode("workbench.view.explorer")
(focus | show) extensions:  user.vscode("workbench.view.extensions")
(focus | show) outline:     user.vscode("outline.focus")
(focus | show) run:         user.vscode("workbench.view.debug")
(focus | show) search:      user.vscode("workbench.view.search")
(focus | show) changes:     user.vscode("workbench.view.scm")
(focus | show) test:        user.vscode("workbench.view.testing.focus")
(focus | show | hide | toggle) (bar | sidebar): user.vscode("workbench.action.toggleSidebarVisibility")

# Settings
show settings (json | jason):
    user.vscode("workbench.action.openSettingsJson")
show settings:
    user.vscode("workbench.action.openSettings2")
show settings <user.text>:
    user.vscode("workbench.action.openSettings2")
    sleep(200ms)
    "{text}"
show shortcuts:             user.vscode("workbench.action.openGlobalKeybindings")
show shortcuts json:        user.vscode("workbench.action.openGlobalKeybindingsFile")

# Teleport / Scout
<user.teleport> back:       user.vscode("workbench.action.openPreviousRecentlyUsedEditor")
<user.teleport> forward:    user.vscode("workbench.action.openNextRecentlyUsedEditor")

<user.teleport> last:
    user.vscode("workbench.action.openPreviousRecentlyUsedEditorInGroup")

<user.teleport> next:
    user.vscode("workbench.action.openNextRecentlyUsedEditorInGroup")

<user.teleport> [dock] <user.text> [{user.file_extension}] [halt]:
    user.vscode("workbench.action.quickOpen")
    sleep(100ms)
    insert(text or "")
    insert(file_extension or "")
    sleep(300ms)
    key(enter)
    sleep(150ms)

<user.teleport> dock:       user.vscode("workbench.action.openPreviousRecentlyUsedEditorInGroup")

(<user.show_list> dock | dock <user.show_list>):
    user.vscode("workbench.action.quickOpen")

<user.show_list> [dock] [<user.text>] [{user.file_extension}] [halt]:
    user.vscode("workbench.action.quickOpen")
    sleep(100ms)
    insert(text or "")
    insert(file_extension or "")
    sleep(300ms)

<user.show_list> (sesh | session | workspace) [<user.text>] [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    user.insert_formatted(text or "", "DASH_SEPARATED,ALL_LOWERCASE")
    sleep(250ms)

<user.teleport> (sesh | session | workspace) [<user.text>] [halt]:
    user.vscode("workbench.action.openRecent")
    sleep(250ms)
    user.insert_formatted(text or "", "DASH_SEPARATED,ALL_LOWERCASE")
    key(enter)
    sleep(250ms)

<user.show_list> (win | window) [<user.text>]:
    user.vscode("workbench.action.switchWindow")
    sleep(250ms)
    insert(text or "")
    sleep(250ms)

<user.teleport> (win | window) [<user.text>]:
    user.vscode("workbench.action.switchWindow")
    sleep(50ms)
    insert(text or "")
    key(enter)
    sleep(250ms)

<user.teleport> sibling:
    user.find_sibling_file()
    sleep(150ms)
    key(enter)

<user.show_list> sibling:
    user.find_sibling_file()

doc split:                  user.vscode("workbench.action.splitEditor")

# Language features
jest:                       code.complete()
jest first:
    code.complete()
    key(tab)
jest param:                 user.vscode("editor.action.triggerParameterHints")
format document:            user.format_document()
refactor this:              user.vscode("editor.action.refactor")
open preview:               user.vscode("markdown.showPreviewToSide")

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
split up:                   user.vscode("workbench.action.moveEditorToAboveGroup")
split down:                 user.vscode("workbench.action.moveEditorToBelowGroup")
split left:                 user.vscode("workbench.action.moveEditorToLeftGroup")
split right:                user.vscode("workbench.action.moveEditorToRightGroup")
focus up:                   user.vscode("workbench.action.focusAboveGroup")
focus down:                 user.vscode("workbench.action.focusBelowGroup")
focus left:                 user.vscode("workbench.action.focusLeftGroup")
focus right:                user.vscode("workbench.action.focusRightGroup")
shrink width:               user.vscode("workbench.action.decreaseViewWidth")
shrink height:              user.vscode("workbench.action.decreaseViewHeight")
expand width:               user.vscode("workbench.action.increaseViewWidth")
expand height:              user.vscode("workbench.action.increaseViewHeight")
split flip:                 user.vscode("workbench.action.toggleEditorGroupLayout")
split clear:                user.vscode("workbench.action.joinTwoGroups")
split solo:                 user.vscode("workbench.action.editorLayoutSingle")
maximize:                   user.vscode("workbench.action.toggleEditorWidths")
bridge:                     user.vscode("workbench.action.focusNextGroup")

# Sidebar
bar (show | hide):          user.vscode("workbench.action.toggleSidebarVisibility")
bar explore:                user.vscode("workbench.view.explorer")
bar extensions:             user.vscode("workbench.view.extensions")
bar outline:                user.vscode("outline.focus")
bar debug:                  user.vscode("workbench.view.debug")
bar search:                 user.vscode("workbench.view.search")
bar source:                 user.vscode("workbench.view.scm")
bar file:                   user.vscode("workbench.files.action.showActiveFileInExplorer")
bar collapse:               user.vscode("workbench.files.action.collapseExplorerFolders")
ref last:                   user.vscode("references-view.prev")
ref next:                   user.vscode("references-view.next")

# Terminal
(show | hide) (term | base): user.vscode("workbench.action.togglePanel")
(term | base) (show | hide | dog ): user.vscode("workbench.action.togglePanel")
(term | base) (large | small): user.vscode("workbench.action.toggleMaximizedPanel")
(term | base) control:      user.vscode("workbench.panel.repl.view.focus")
(term | base) output:       user.vscode("workbench.panel.output.focus")
(term | base) problems:     user.vscode("workbench.panel.markers.view.focus")
((term | base) terminal | focus (term | base)): user.vscode("workbench.action.terminal.focus")
(term | base) debug:        user.vscode("workbench.debug.action.toggleRepl")
(term | base) clear:        user.vscode("workbench.debug.panel.action.clearReplAction")
(<user.teleport> term | term <user.teleport>) <user.text>: "z {text}\n"
(<user.show_list> term | term <user.show_list>) <user.text>: "z -l {text}\n"
(<user.teleport> term | term <user.teleport>) (last | switch): "z -\n"
term external:              user.vscode("workbench.action.terminal.openNativeConsole")
term new:                   user.vscode("workbench.action.terminal.new")
term next:                  user.vscode("workbench.action.terminal.focusNext")
term last:                  user.vscode("workbench.action.terminal.focusPrevious")
term split:                 user.vscode("workbench.action.terminal.split")
term zoom:                  user.vscode("workbench.action.toggleMaximizedPanel")
term trash:                 user.vscode("workbench.action.terminal.kill")
term scroll up:             user.vscode("workbench.action.terminal.scrollUp")
term scroll down:           user.vscode("workbench.action.terminal.scrollDown")
term <number_small>:        user.vscode_terminal(number_small)
katie:                      "cd "
katie up:                   "cd ..\n"
katie <user.text>:          "cd {text}\n"
try katie <user.text>:      "cd {text}\t\n"
katie try <user.text>:      "cd {text}\t\n"
lisa:                       "ls\n"
printer:                    "pwd\n"

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
file open folder:           user.vscode("revealFileInOS")
file reveal:                user.vscode("workbench.files.action.showActiveFileInExplorer")
file copy path:             user.vscode("copyFilePath")
file copy relative:         user.vscode("copyRelativeFilePath")
file copy name:             user.vscode("andreas.copyFilename")
file remove:                user.vscode("andreas.removeFile")
file move:                  user.vscode("andreas.moveFile")
file sibling [<user.filename>]:
    user.vscode("andreas.newFile", filename or "")
file rename [<user.filename>]:
    user.vscode("andreas.renameFile", filename or "")
file clone [<user.filename>]:
    user.vscode("andreas.duplicateFile", filename or "")


okay:                       user.vscode("editor.action.insertLineAfter")

# Git
git switch:                 "git switch -\n"
git log:                    "git log\n"
get rebase head <number_small>: "git rebase -i HEAD~{number_small}\n"
git difftool head <number_small>: "git difftool HEAD~{number_small}\n"
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
git add all:                user.vscode("git.stageAll")
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
git checkout {user.git_branch}: user.git_find_branch(git_branch)
git checkout [<user.text>]: user.git_find_branch(text or "")
git checkout branch [<user.text>]:
    user.vscode("git.branch")
    sleep(50ms)
    text = user.format_text(text or '', "SNAKE_CASE")
    "{text}"
git commit [<user.text>]:
    user.vscode("git.commit")
    sleep(300ms)
    text = user.format_text(text or "", "CAPITALIZE_FIRST_WORD")
    "{text}"

# Folding
fold recursive:             user.vscode("editor.foldRecursively")
unfold recursive:           user.vscode("editor.unfoldRecursively")
fold all:                   user.vscode("editor.foldAll")
unfold all:                 user.vscode("editor.unfoldAll")
fold comments:              user.vscode("editor.foldAllBlockComments")

# Navigation
go line <number>:           edit.jump_line(number)
focus editor:               user.vscode("workbench.action.focusActiveEditorGroup")

# Cursor
cursor back:                user.vscode("cursorUndo")
cursor forward:             user.vscode("cursorRedo")
cursor up:                  user.vscode("editor.action.insertCursorAbove")
cursor down:                user.vscode("editor.action.insertCursorBelow")
cursor lines:               user.vscode("editor.action.insertCursorAtEndOfEachLineSelected")
cursor expand:              user.vscode("editor.action.smartSelect.expand")
cursor shrink:              user.vscode("editor.action.smartSelect.shrink")
cursor next:                user.vscode("editor.action.addSelectionToNextFindMatch")
cursor last:                user.vscode("editor.action.addSelectionToPreviousFindMatch")
cursor (breed | all):       user.vscode("editor.action.selectHighlights")
cursor skip:                user.vscode("editor.action.moveSelectionToNextFindMatch")

# Debug and run
build program:              user.vscode("workbench.action.tasks.build")
run program:                user.vscode("workbench.action.debug.run")
debug start:                user.vscode("workbench.action.debug.start")
breakpoint:                 user.vscode("editor.debug.action.toggleBreakpoint")
continue:                   user.vscode("workbench.action.debug.continue")
step over:                  user.vscode("workbench.action.debug.stepOver")
step into:                  user.vscode("workbench.action.debug.stepInto")
step out:                   user.vscode("workbench.action.debug.stepOut")
debug restart:              user.vscode("workbench.action.debug.restart")
debug pause:                user.vscode("workbench.action.debug.pause")
debug stop:                 user.vscode("workbench.action.debug.stop")
debug select:               user.vscode("workbench.action.debug.selectandstart")
debug extension:
    user.vscode("workbench.action.debug.selectandstart")
    "run extension"
    key(enter)
debug test:
    user.vscode("workbench.action.debug.selectandstart")
    "extension tests"
    key(enter)
debug subset:
    user.vscode("workbench.action.debug.selectandstart")
    "run test subset"
    key(enter)
run task compile:
    user.vscode("workbench.action.tasks.runTask")
    "compile"
    sleep(200ms)
    key(enter)
run task [<user.text>]:
    user.vscode("workbench.action.tasks.runTask")
    "{text or ''}"
dev tools:                  user.vscode("workbench.action.toggleDevTools")
select element:             key(ctrl-shift-c)

# Find a symbol
<user.find> symbol [<user.text>]$:
    user.vscode("workbench.action.showAllSymbols")
    sleep(50ms)
    user.insert_formatted(text or "", "CAMEL_CASE")

# CSV
align columns:              user.vscode("rainbow-csv.Align")
shrink columns:             user.vscode("rainbow-csv.Shrink")

# Misc
install extension:          user.vscode("workbench.extensions.action.installVSIX")
window reload:              user.vscode("workbench.action.reloadWindow")
trim trailing:              user.vscode("editor.action.trimTrailingWhitespace")
inspect scope:              user.vscode("editor.action.inspectTMScopes")
disk raw:                   user.save_without_formatting()
disk files:                 user.vscode("workbench.action.files.saveFiles")
disclose:
    key(esc:5)
    edit.save()
    sleep(150ms)
    key(ctrl-w)

copy command id:            user.copy_command_id()
<user.find> again:          user.vscode("rerunSearchEditorSearch")
generate range [from <number_small>]:
    user.vscode("andreas.generateRange", number_small or 1)

snip last:                  user.vscode("jumpToPrevSnippetPlaceholder")
[snip] next:                user.vscode("jumpToNextSnippetPlaceholder")

change language {user.code_language}:
    user.change_language(code_language)
    key(enter)

change language [<user.text>]:
    user.change_language(text or "")

please [<user.text>]$:
    user.vscode("workbench.action.showCommands")
    "{user.text or ''}"

wrap dog:                   user.vscode("editor.action.toggleWordWrap")

# copilot
pilot jest:                 user.vscode("editor.action.inlineSuggest.trigger")
pilot next:                 user.vscode("editor.action.inlineSuggest.showNext")
pilot last:                 user.vscode("editor.action.inlineSuggest.showPrevious")
[pilot] yes:                user.vscode("editor.action.inlineSuggest.commit")
pilot word:                 user.vscode("editor.action.inlineSuggest.acceptNextWord")
pilot nope:                 user.vscode("editor.action.inlineSuggest.undo")
pilot cancel:               user.vscode("editor.action.inlineSuggest.hide")
pilot (dog | toggle | off | on):
    user.vscode("github.copilot.toggleCopilot")
    mouse_move(1683, 954)
    sleep(300ms)
    mouse_click(0)
