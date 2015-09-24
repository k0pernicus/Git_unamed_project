import argparse
import lib.settings.settings
import os

from os.path import expanduser

from lib.git.commands import list_git_projects
from lib.scan import scan

from lib.config.config import open_config_file
from lib.config.config import clean_config_file
from lib.config.config import close_config_file

def load_paths_from_config_file():
    f = open_config_file()
    lib.settings.settings.CONFIG_FILE_CONTENT = f.readlines()
    close_config_file(f)

def main():

    parser = argparse.ArgumentParser(description="Program to visualize any changes about .git projects")

    #For files
    parser.add_argument("--scan", "-s", help="Scan from the argument directory to find any .git projects", default="~")
    parser.add_argument("--check", "-c", help="Check the hidden configuration file - if any .git project is not referenced, it will be deleted", action="store_true")

    #Action on git files
    parser.add_argument("--list", "-l", help="List all git projects", action="store_true")
    parser.add_argument("--stats", "-st", help="Get stats for each project", action="store_true")

    #Debug & version
    parser.add_argument("--debug", "-d", help="Debug mod - for developer only", action="store_true")
    parser.add_argument("--version", "-v", help="Version of the program", action="store_true")

    lib.settings.settings.init()

    lib.settings.settings.ARGS = parser.parse_args()

    lib.settings.settings.CONFIG_FILE_PATH = "{0}/{1}".format(expanduser('~'), lib.settings.settings.CONFIG_FILE_NAME)

    #Create an empty file if not exists
    if not os.path.exists(lib.settings.settings.CONFIG_FILE_PATH):
        os.mknod(lib.settings.settings.CONFIG_FILE_PATH)

    if lib.settings.settings.ARGS.check:
        f = open_config_file()
        clean_config_file(f)
        close_config_file(f)
        scan()

    load_paths_from_config_file()

    if lib.settings.settings.ARGS.scan:
        scan()

    if lib.settings.settings.ARGS.list:
        list_git_projects()

if __name__ == '__main__':
    main()
