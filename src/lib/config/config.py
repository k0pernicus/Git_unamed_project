import lib.settings.settings

def open_config_file():
    return open(lib.settings.settings.CONFIG_FILE_PATH, "wr")

def close_config_file(f):
    try:
        f.close()
    except:
        print("The file {0} canno't be close".format(f.name))

def clean_config_file(f):
    try:
        f.truncate()
        f.close()
    except:
        print("The file {0} canno't be truncate, and close".format(f.name))

def add_new_path(f, path):
    try:
        f.write("{0}\n".format(path))
    except:
        print("The path {0} canno't be added to {1}".format(path, f.name))
