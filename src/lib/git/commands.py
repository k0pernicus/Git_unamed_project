import lib.settings.settings

def list_git_projects():
    print("List of git project:")
    #end="" -> avoid last '\n' character
    for entry in lib.settings.settings.CONFIG_FILE_CONTENT:
        print("\t{0}".format(entry), end="")
