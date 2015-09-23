import os
import lib.settings.settings

from os.path import expanduser

def scan():
    """
    Function to scan the directory from the home dir, or the repository given as parameter by the user
    """

    default_walk_from = os.walk(expanduser("~"))

    if lib.settings.settings.ARGS.dir_to_scan:
        default_walk_from = os.walk(lib.settings.settings.ARGS.dir_to_scan)

    for path, dirs, files in default_walk_from:
        for d in dirs:
            if d == ".git":
                print("{0}".format(os.path.join(path, d)))
