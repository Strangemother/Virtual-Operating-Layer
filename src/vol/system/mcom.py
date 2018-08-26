"""A module to communicate through mmap file descripter
without writing a file in standard bytes.

This is pretty cool - the ability to read/write to an anonymous
file, seeking to points within the file.

Primarily utilized for auto bios IO and memory communication
through stnd-alone processes.
"""

import mmap

ACCESS_COPY = mmap.ACCESS_COPY
ACCESS_READ = mmap.ACCESS_READ
ACCESS_WRITE = mmap.ACCESS_WRITE
ALLOCATIONGRANULARITY = mmap.ALLOCATIONGRANULARITY
PAGESIZE = mmap.PAGESIZE


def open(name, byte_length, fileno=-1, access=ACCESS_WRITE):
    """Open a descriptor with a given name. and a length in bytes.
    if no fileno is given open an anonymous handler
    """
    _map = mmap.mmap(fileno, byte_length, name, access)
    return _map


class Handle(object):
    """An mcom.Handle provides an easy abstraction to the mmap commands
    and instance management.

    Providing a uuid on both sides of a com, the handle read will invoke the
    correct responses for the read write phase. This is handled within the
    class.
    """
