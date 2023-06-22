tag: terminal
and tag: user.git
not tag: terminal
and app: vscode
-

git {user.git_command} [<user.git_arguments>]:
    args = git_arguments or ""
    "git {git_command}{args} "
git commit [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git commit{args} --message '{message}", "'")
git stash [push] [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git stash push{args} --message '{message}", "'")

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
cd up$:                     "cd ..\n"
# <user.teleport> <user.text>: "z {text}\n"
get rebase origin main:     "git rebase origin/main\n"
git push force with lease:  "git push --force-with-lease\n"
git cherry pick continue:   "git cherry-pick --continue\n"
yarn build:                 "yarn build\n"
git status$:                "git status\n"
git add patch$:             "git add --patch\n"
git show head$:             "git show HEAD\n"
git diff$:                  "git diff\n"
git diff (cached | cashed)$: "git diff --cached\n"

# Convenience
git clone (clipboard | paste):
    insert("git clone ")
    edit.paste()
    key(enter)
git diff highlighted:
    edit.copy()
    insert("git diff ")
    edit.paste()
    key(enter)
git diff (clipboard | paste):
    insert("git diff ")
    edit.paste()
    key(enter)
git add highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    key(enter)
git add (clipboard | paste):
    insert("git add ")
    edit.paste()
    key(enter)
git commit highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    insert("\ngit commit\n")
