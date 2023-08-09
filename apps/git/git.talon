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
git push force with lease:  "git push --force-with-lease\n"
git cherry pick continue:   "git cherry-pick --continue\n"
git init:                   "git init\n"
git commit amend:           "git commit --amend\n"
git clone:                  "git clone "
git switch:                 "git switch -\n"
git checkout:               "git checkout "
git checkout branch:        "git checkout -b "
git checkout branch <user.text>: "git checkout -b {text}\n"
git checkout master:        "git checkout master\n"
git checkout main:          "git checkout main\n"
git checkout <user.text>:   "git checkout {text}"
git add all:                "git add .\n"
git add [all] commit:       "git add .\ngit commit\n"
git log:                    "git log -n 20 | code -\n"
git ref log:                "git reflog -n 50| code -\n"
git log stat:               "git log -n 20 --stat | code -\n"
git log oneline:            "git log -n 20 --oneline | code -\n"
git log graph:              "git log -n 20 --graph | code -\n"
git log graph oneline:      "git log -n 20 --graph --oneline | code -\n"

git status:                 "git status\n"
git push:                   "git push\n"
git push upstream:
    insert("git rev-parse --abbrev-ref HEAD | clip.exe\n")
    insert("git push --set-upstream origin ")
    edit.paste()
git stash:                  "git stash\n"
git stash list:             "git stash list | code -\n"
git stash pop:              "git stash pop\n"
git stash apply:            "git stash apply\n"
git pull:                   "git pull\n"
git pull origin main:       "git pull origin main\n"
git pull origin master:     "git pull origin master\n"
git pull rebase:            "git pull --rebase\n"
git pull rebase origin main: "git pull --rebase origin main\n"
git pull rebase origin master: "git pull --rebase origin master\n"
get rebase origin main:     "git rebase origin/main\n"
git rebase upstream main:   "git rebase upstream/main\n"
git rebase continue:        "git rebase --continue\n"
git rebase abort:           "git rebase --abort\n"
git rebase interactive head <number_small>: "git rebase -i HEAD~{number_small}\n"
git reset hard:             "git reset --hard"
git fetch all:              "git fetch --all\n"
git fetch upstream:         "git fetch upstream\n"
git branch:                 "git branch | code -\n"
git branch (viv | vest):    "git branch -vv | code -\n"
git branch halt:            "git branch"
git branch list all:        "git branch --list --all | code -\n"
git diff tool:              "git difftool\n"
git merge tool:             "git mergetool\n"
git config list:            "git config --list | code -\n"
git config list global:     "git config --list --global | code -\n"
gh repo:                    "gh repo\n"
gh repo create:             "gh repo create\n"
git remote (vest | viv):    "git remote -v\n"
git remote add:             "git remote add "
git remote add upstream :   "git remote add upstream\n"
git remote set ural:        "git remote set-url "
git remote set ural upstream:        "git remote set-url upstream "
git reset:                  "git reset\n"
git reset head <number_small>: "git reset HEAD~{number_small}\n"
yarn build:                 "yarn build\n"
git status$:                "git status\n"
git add patch$:             "git add --patch\n"
git show head$:             "git show HEAD\n"
git diff$:                  "git diff\n"
git diff (cached | cashed)$: "git diff --cached\n"

# Convenience
git clone (clip | paste):
    insert("git clone ")
    edit.paste()
    key(enter)
git diff highlighted:
    edit.copy()
    insert("git diff ")
    edit.paste()
    key(enter)
git diff (clip | paste):
    insert("git diff ")
    edit.paste()
    key(enter)
git add highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    key(enter)
git add (clip | paste):
    insert("git add ")
    edit.paste()
    key(enter)
git commit highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    insert("\ngit commit\n")
