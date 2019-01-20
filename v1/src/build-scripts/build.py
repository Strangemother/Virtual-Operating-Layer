"""Build tool for instant call of other build processes.
"""
import os
import build_bios

SETTINGS = None


def load_settings_file(filename):
    """Load a python file and return the contents as a dictionary.
    """
    file_content = ''
    with open(filename) as stream:
        file_content = open(filename, "rb").read()
    g = {}
    exec(compile(file_content, filename, 'exec'), g)
    del g['__builtins__']
    return dict(g.items())


def load_settings():
    file = os.path.join(os.path.dirname(__file__), '..', 'config', 'build', 'bios.py')
    settings = load_settings_file(file)
    return settings


def convert_tpys():

    # if is_tpy(src_path):
    #     convert_tpy(src_path, dest_filepath)

    for x,y,files in os.walk('.'):
        for filename in files:
            if filename.endswith('tpy'):
                filepath = os.path.join(x, filename)
                build_bios.convert_tpy(filepath, kwargs=SETTINGS)


def main():
    global SETTINGS
    print("Build")
    SETTINGS = load_settings()
    convert_tpys()
    build_bios.main(SETTINGS)


if __name__ == '__main__':
    main()
