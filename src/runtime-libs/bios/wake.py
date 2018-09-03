"""The First function within the bios boot.
The BIOS memoory is first assigned using a given hard-coded key.

Once assigned the wak _produces_ a memory allocation and assigns the first
key values to the BIOS memory slot.

The POST commands are read and the instructions load the next memory
slots for the enviroment.

    Open Mmap volatile TAPE.

        Any middleman information for the TAPE should write here. Such as
        bios RAM encryption layers.

    COLD or WARM boot.
    Write a print function.
    clean open space
    load memory references
    load base lib
    load memory config
    load state

BIOS RAM STATE
    0   unallocated / not installed
        Nothing in the ram, no protection mode, no instructions.

"""

import sys, builtins
import mmap, os
import time
import marshal


TAPE_EXISTS = -1
TAPE_MISSING = -2
BEEP = "\x07"


HEADER = { 'debug': None }


def c_mem_clear(string):
    import ctypes
    location = id(string) + 20
    size     = sys.getsizeof(string) - 20
    ''' msvcrt
        fclose
        fopen
        freopen
        fwrite
        kbhit
        memcmp
        memcpy
        memmove
        memset
        rand
        scanf
        sprintf
        srand
        system
        time
    '''
    memset =  ctypes.cdll.msvcrt.memset
    # For Linux, use the following. Change the 6 to whatever it is on your computer.
    # memset =  ctypes.CDLL("libc.so.6").memset

    puts( "Clearing 0x%08x size %i bytes" % (location, size))

    memset(location, 0, size)


puts = getattr(__builtins__, 'print')


"""A new ram tape file has:
    state   int for vol wakeup
    pointer - the filedescriptor pointer - stored and verified later
    uuid - For verification
    kernel -
"""

class Config:

    def find(self):
        if os.path.exists('HEADER'):
            puts('discovered configure "HEADER"')
            data = self.read('HEADER')
            return data

    def write(self, value):
        vv=compile('{}\n'.format(value), 'HEADER', 'eval')
        ff=open('HEADER', 'wb')
        marshal.dump(vv, ff)
        ff.close()

    def read(self, name):
        stream = open(name, 'rb')
        br = b''
        for line in stream.readlines():
            br += line
        result = eval(marshal.loads(br))
        stream.close()
        return result


def WAKE():
    global tape
    global HEADER

    io = IO()
    config = Config()
    # tape = BIOS_TAPE()
    HEADER = config.find()
    puts('WAKE')

# Import cold or warm state.
WAKE()
