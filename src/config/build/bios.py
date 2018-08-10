""" Settings file used at BUILD time to assist the build release.
Variables here are can be imported in build scripts. Any .tpy file
is parsed through these parameters - writing the literal value to the produced
by file.

This is a good place to store embeded secrets into the vol and using them
though the C-build.
"""

from os.path import join
import uuid, os

VERSION = dict(
    NAME = 'Kerbechet',
    REPR = (0, 0, 1,),
    CHAR = "\\u25BA",
    )

BOOT_NAME='boot'
# src/{} location of the script to gcc compile
C_PATH='boot-script'

_uuid = uuid.uuid4()
BIOS_UUID_STR = str(_uuid)
# A unique key for the build - used for encyption
BIOS_UUID = bytes(BIOS_UUID_STR, 'utf-8')
BIOS_UUID_BYTES = _uuid.bytes

# System flags for the bios init file on the host,
# https://msdn.microsoft.com/en-us/library/z0kc8e3z.aspx
BIOD_TAPE_ACCESS     = os.O_RDWR|os.O_RANDOM|os.O_BINARY|os.O_NOINHERIT
BIOD_TAPE_ACCESS_NEW = os.O_RDWR|os.O_RANDOM|os.O_BINARY|os.O_NOINHERIT|os.O_CREAT|os.O_EXCL
# Initial lib addresses written to the kernel for the first instance.
# This should point to all compiled libs for the bios
# and the first os functionality.
BIOS_LIBS = (
    "bios_os",
    # "builtin",
)

# output folder relative to src
OUTPUT_PATH='../build'
# application to collect as env to copy
RUNTIME_DIR='runtime-envs/MASTER'

# name of the folder within build containg the runnable env
TARGET_ENV_NAME='bios_runtime'

# Name of the folder within the build dir containing the
# c built libs to associate with the environment
TARGET_LIB_NAME = 'build_libs'

RUNTIME_FILENAME = 'vol_runtime'

# The initial value for the BIOS terminal prefix.
# unicode preferred.
TERMINAL_PREFIX = "\\u25BA"
TERMINAL_INTRO = "... VOL {BOOT_NAME} {REPR} {NAME}".format(**VERSION, **globals())

# Name of the folder within the source to copy to the LIB_TARGET_NAME
RUNTIME_LIBS='runtime-libs'

# path of the folder for runtime libraries within the build directory
LIB_TARGET_NAME = join(TARGET_ENV_NAME, 'libs')

# env startfile - src/{} to build/{target_env_name}/{} dest
START_FILE = (
        'startup.tpy',
        join(TARGET_ENV_NAME, 'startup')
    )


# TODO: Fix order- currently alphabetic

# Add library folders to the automatic path import.
# If an entry is missing from the output lib folder  "libs/" the path
# is not applied to the auto file.
LIB_FOLDERS = [
    'core',
    # Automatically apply a library suite here;
    # Alternatively allow the bios to discover
    # 'win-64',

    #'env_lib',
    ]

# Append arbitrary names to the lib path without parsing - but will be
# written as a relative path to the libs/
LIB_FOLDERS_EXTRAS = [
    TARGET_LIB_NAME,
]

# Compilation of a file into the env lib
COMPILE_FILES = (
    ("COMPILED.bios", [
            "runtime-libs/bios/bios.pyx",
        ]),
)


# Prep naming after compilation
RUNTIME_NAMES = (
    ('python36-stackless.exe', '{}.exe'.format(RUNTIME_FILENAME)),
    ('python36_w.exe', '{}_headless.exe'.format(RUNTIME_FILENAME)),
)
