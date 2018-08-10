"""The "BIOS" is the core runtime given to the VOL at exection.
the self exectuting module is unpacked as a zim including any assets for a successful
base loadout.

In this case the bios includes a its settings, executable env write...

This file builds all the components for a ready deployable of a BIOS.
"""
import os
import shutil
import time
from distutils.dir_util import copy_tree

SETTINGS = None

kw = dict(
          # name of the 'boot' file, first file to access the VOL
          BOOT_NAME='boot',
          # src/{} location of the script to gcc compile
          C_PATH='boot-script',
          # output folder relative to src
          OUTPUT_PATH='build',
          # application to collect as env to copy
          RUNTIME_DIR='runtime-envs/stackless-3.6.4-amd64-thin',
          RUNTIME_LIBS='runtime-libs',
          # name of the folder within build containg the runnable env
          TARGET_ENV_NAME='bios_runtime',
        )


# dev machine tool
def main(settings=None):
    global SETTINGS
    SETTINGS = settings or {}
    for key in SETTINGS:
        kw[key] = SETTINGS[key]

    build_boot()
    copy_runtime()
    time.sleep(.5)
    alter_runtime()
    copy_libs()
    create_lib_map()
    write_startup_file()
    build_env_libs()


def build_boot():
    """
    """
    print(': Building boot exe.')
    kw['OUTPUT_PATH'] = os.path.abspath(kw['OUTPUT_PATH'])

    if os.path.exists(kw['OUTPUT_PATH']) is False:
        print('Making', kw['OUTPUT_PATH'])
        os.mkdir(kw['OUTPUT_PATH'])

    commands = (
        "gcc -shared -o {OUTPUT_PATH}\{BOOT_NAME}.so -fPIC {C_PATH}\{BOOT_NAME}.c".format(**kw),
        "gcc {C_PATH}\{BOOT_NAME}.c -o {OUTPUT_PATH}\{BOOT_NAME}.exe".format(**kw),
    )

    for c in commands:
        print(c)
        os.system(c)

    assert os.path.exists('{OUTPUT_PATH}\{BOOT_NAME}.so'.format(**kw))
    assert os.path.exists('{OUTPUT_PATH}\{BOOT_NAME}.exe'.format(**kw))


def copy_runtime():
    """Copy associated shared runtime resources for the target env.
    """

    env_dir = kw['RUNTIME_DIR']
    out_dir = "{OUTPUT_PATH}/{TARGET_ENV_NAME}".format(**kw)
    if os.path.isdir(out_dir) is False:
        print('copying env', env_dir, 'to', out_dir)
        shutil.copytree(env_dir, out_dir)
    else:
        print('Not copying env; target dest exists.')


def alter_runtime():
    """finalise the runtime files"""
    env_dir = kw['RUNTIME_DIR']
    out_dir = "{OUTPUT_PATH}/{TARGET_ENV_NAME}".format(**kw)

    for orig_name, new_name in SETTINGS['RUNTIME_NAMES']:
        orig_path = os.path.join(env_dir, out_dir, orig_name)
        new_path = os.path.join(env_dir, out_dir, new_name)
        print('Changing "{}" to "{}"'.format(orig_path, new_path))

        if os.path.exists(orig_path) is True:
            if os.path.exists(new_path) is True:
                print('Skipping file as it already exists: "{}"'.format(new_path))
            else:
                print('renaming', orig_name, 'to', new_path)
                os.rename(orig_path, new_path)
        else:
            print("Cannot rename {} to {}. File does not exist: {}".format(
                    orig_name, new_name, orig_path
                ))


def create_lib_map():
    """Create the path file associating the library with the runtime
    """
    out_dir = "{OUTPUT_PATH}/{TARGET_ENV_NAME}".format(**kw)
    filename = '{out_dir}/{RUNTIME_FILENAME}._pth'.format(out_dir=out_dir, **SETTINGS)

    # Add every top level in libs/
    libs_folder = "{OUTPUT_PATH}/{LIB_TARGET_NAME}".format(**kw)

    # Just the names of each folder or file in the
    entries = ()
    for dir_entry in os.scandir(libs_folder):
        if dir_entry.name in SETTINGS['LIB_FOLDERS']:
            entries += (dir_entry.name, )
        else:
            print('Ignoring lib folder "{}"'.format(dir_entry.name))

    for name in SETTINGS['LIB_FOLDERS_EXTRAS']:
        entries += (name, )

    print('\nWriting mapping: {} to "{}"'.format(entries, filename))

    # Path of libs/ relative to the runtime
    rel_lib = os.path.relpath(libs_folder, out_dir)

    # TODO: Fix ordering
    # write path entries relative to the runtime.exe
    with open(filename, 'w') as stream:
        for item in entries:
            fullpath = (os.path.join(rel_lib, item))
            line = "{}\n".format(fullpath)
            stream.write(line)


def copy_libs():
    """Copy associated shared library resources for the target env.
    """
    env_dir = kw['RUNTIME_LIBS']
    out_dir = "{OUTPUT_PATH}/{LIB_TARGET_NAME}".format(**kw)
    if os.path.exists(out_dir) is False:
        print('\nPerforming libs copy', env_dir, 'to', out_dir)

        for folder in SETTINGS['LIB_FOLDERS']:
            full_path = os.path.join(env_dir, folder)
            out_path = os.path.join(out_dir, folder)
            if os.path.exists(full_path):
                if os.path.exists(out_path) is True:
                    print('Did not copy "{}" - desination exist: "{}"'.format(full_path, out_path))
                else:
                    copy_tree(full_path, out_path)
                    print('copying "{}" to "{}"'.format(full_path, out_path))
    else:
        print('Skipping lib copy, directory exists: "{}"'.format(out_dir))


def is_tpy(src_path):
    return os.path.splitext(src_path)[1] == '.tpy'


def convert_tpy(src_path, dest_path=None, kwargs=None):
    """Convert a given tpy file to a standard py file. If the dest path
    is None, the src_path is used resulting in a tpy/py in the same directory
    """

    print('\nConverting py template file')
    content = ''
    with open(src_path, 'r') as stream:
        for line in stream:
            content += line

    data = kwargs or SETTINGS
    if dest_path is None:
        dirn, filen = os.path.split(src_path)
        name, ext = os.path.splitext(filen)
        pyfilen = "{}.py".format(name)
        dest_path = os.path.join(dirn, pyfilen)
        print('writing to "{}"'.format(dest_path))

    with open(dest_path, 'w') as stream:
        stream.write(content.format(**data))


def write_startup_file():
    """The startup file exists as the file ENV file ran by a BIOS runtime.
    It sets the parameters for the next step.
    Found as startup.tpy
    """
    src_path, end_path = SETTINGS['START_FILE']
    dest_filepath = "{OUTPUT_PATH}/{START_FILE[1]}".format(**kw)
    print('create startup file "{}"  to "{}"'.format(src_path, dest_filepath))

    if is_tpy(src_path):
        convert_tpy(src_path, dest_filepath)

    # if os.path.splitext(src_path)[1] == '.tpy':
    #     print('Converting py template file')
    #     content = ''
    #     with open(src_path, 'r') as stream:
    #         for line in stream:
    #             content += line

    #     with open(dest_filepath, 'w') as stream:
    #         stream.write(content.format(**SETTINGS))
    else:
        shutil.copy2(src_path, dest_filepath)


import sys
import build_libs


def build_env_libs():
    """Make the libs for the application

    Using the same setup.py file to boot install the dev code.
    """

    build_libs.main(SETTINGS)

if __name__ == '__main__':
    main()
