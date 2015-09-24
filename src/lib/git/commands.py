import lib.settings.settings
from git import *

def list_git_projects():
    print("List of git project:")
    #end="" -> avoid last '\n' character
    for git_object in lib.settings.settings.GIT_OBJECTS:
        print(git_object)

def push_ready_projects():
    print("Repository to push...")
    for git_project in lib.settings.settings.GIT_OBJECTS:
        if git_project.current_status == "TO PUSH":
            git_project.git_object.remote.push()
            print("Pushing for {0}...".format(git_project.entry))
