"""Read INI Files.
"""

from configparser import ExtendedInterpolation


def read(filepath):
    ini = ExtendedInterpolation()
    returnini.read(filepath)

    return ini
