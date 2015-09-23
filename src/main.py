import argparse
import lib.settings.settings

def main():

    parser = argparse.ArgumentParser(description="Program to visualize any changes about .git projects")

    parser.add_argument("--scan", "-s", help="Scan your home directory to find any .git projects", action="store_true")
    parser.add_argument("--check", "-c", help="Check the hidden configuration file - if any .git project is not referenced, it will be deleted", action="store_true")
    parser.add_argument("--debug", "-d", help="Debug mod - for developer only", action="store_true")
    parser.add_argument("--version", "-v", help="Version of the program", action="store_true")

    lib.settings.settings.init()

    lib.settings.settings.ARGS = parser.parse_args()

    lib.settings.settings.CONFIG_FILE_PATH = "{0}/{1}".format(expanduser('~'), lib.settings.settings.CONFIG_FILE_NAME)

if __name__ == '__main__':
    main()
