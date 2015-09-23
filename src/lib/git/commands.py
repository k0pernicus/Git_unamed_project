import lib.settings.settings
from git import *

def list_git_projects():
    print("List of git project:")
    #end="" -> avoid last '\n' character
    for entry in lib.settings.settings.CONFIG_FILE_CONTENT:
        if entry[-1] == '\n':
            entry = entry[:-1]
        repo = Repo(entry)
        if repo.is_dirty():
            current_status = "DIRTY"
        elif not "Your branch is up-to-date" in repo.git.status():
            current_status = "TO PUSH"
        else:
            current_status = "CLEAN"
        to_add = "--" if not lib.settings.settings.ARGS.stats else "-- {0} commits --".format(len(list(repo.iter_commits())))
        print("\t[{0}] {1} {2} {3} untracked files".format(current_status, entry, to_add, len(repo.untracked_files)))
