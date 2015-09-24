import os
import lib.settings.settings

from os.path import expanduser

from lib.config.config import open_config_file
from lib.config.config import add_new_path
from lib.config.config import close_config_file

def scan():
    """
    Function to scan the directory from the home dir, or the repository given as parameter by the user
    """

    #Update the field which contains all directories from the home dir of the user, or the directory to scan

    if lib.settings.settings.ARGS.scan == "~":
        default_walk_from = os.walk(expanduser("~"))
    else:
        default_walk_from = os.walk(lib.settings.settings.ARGS.scan)

    #Open the configuration file
    f = open_config_file()

    for path, dirs, files in default_walk_from:
        for d in dirs:
            if d == ".git":
                add_new_path(f, path)
                #If debug mod, print out the path file
                if lib.settings.settings.ARGS.debug:
                    print("{0}".format(os.path.join(path, d)))

    #Close the configuration file
    close_config_file(f)
