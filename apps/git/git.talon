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
git init:                   "git init\n"
git commit amend:           "git commit --amend\n"
git clone:                  "git clone "
git switch:                 "git switch -\n"
git checkout:               "git checkout "
git checkout branch:        "git checkout -b "
git checkout branch <user.text>: "git checkout -b {text}\n"
# git checkout branch paste:      "git checkout -b <paste>\n"
# git checkout <%text%>:          "git checkout <%text%>\n"
# git checkout paste:             "git checkout <paste>\n"
git add all:                "git add .\n"
# git add all and commit:         user.insert_between("git add . && git commit -m '{message}", "'")
git add all and commit <user.text>: 'git add . && git commit -m "{text}"\n'
git log:                    "git log\n"
git status:                 "git status\n"
git push:                   "git push\n"
git stash:                  "git stash\n"
git stash apply:            "git stash apply\n"
git pull:                   "git pull\n"
git pull origin main:       "git pull origin main\n"
git pull origin master:     "git pull origin master\n"
git pull rebase:            "git pull --rebase\n"
git pull rebase origin main: "git pull --rebase origin main\n"
git pull rebase origin master: "git pull --rebase origin master\n"
git rebase continue:        "git rebase --continue\n"
git rebase abort:           "git rebase --abort\n"
git reset hard:             "git reset --hard\n"
git fetch all:              "git fetch --all\n"
git branch:                 "git branch\n"
git branch list all:        "git branch --list --all\n"
git diff tool:              "git difftool\n"
# git diff tool head <%num%>:     "git difftool HEAD~<%num%>\n"
git merge tool:             "git mergetool\n"
git config list:            "git config --list\n"
git config list global:     "git config --list --global\n"
gh repo:                    "gh repo\n"
gh repo create:             "gh repo create\n"
# git rebase interactive head <%num%>: "git rebase -i HEAD~<%num%>\n"

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
