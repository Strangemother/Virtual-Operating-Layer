"""To release the package as a single bios unit every file assigned here is written to s single 'bios'
for import in the runtime.

Phases:
    WAKE - perform mandatory imports for bios libs and init with boot key.

        + receive boot key from hardwire value
        + import mandatory libraries
        + write intial env
        + start memory allocation
        + read write boot config
        + test state


wake, env create, read settings, load lib, offload events.
"""

import sys, builtins
import mmap, os
import time
import marshal
import sys

# file: bios.pyx

class Config:

    def find(self, name):
        if os.path.exists(name):
            puts('discovered configure {}'.format(name))
            data = self.read(name)
            return data

    def write(self, value, name):
        vv=compile('{}\n'.format(value), name, 'eval')
        ff=open(name, 'wb')
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


TAPE_EXISTS = -1
TAPE_MISSING = -2
BEEP = "\x07"


HEADER = {{ 'debug': None }}


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
def WAKE():
    global tape
    global HEADER

    #io = IO()
    config = Config()
    # tape = BIOS_TAPE()
    HEADER = config.find()
    puts('WAKE')

# Import cold or warm state.
WAKE()


"""Given a memory allocation key the environment reads access memory
and creates a an env given the paramers from the WAKE

Any mandatory instructions and extensions to the POST instuctions
provide procedures to run. Next step to CONFIGURE the base env for
the BIOS.

At this point output beffers are assigned, any host OS specific libraries are
applied and the allowed memory address is read to assign hosted read only
memory
"""


def ENVIRONMENT():
    puts('ENVIRONMENT')
    sys.ps1 = '{TERMINAL_PREFIX} '
    sys.ps2 = '... '
    sys.prefix = '/VOL/'
    # sys.builtin_module_names = ()
    # sys.exec_prefix = 'exec_prefix'
    # sys.base_prefix = 'base_prefix'
    sys.copyright = 'Apples'
    #sys.path = []
    # sys.modules = {{}}
    #sys.version = {VERSION[REPR]}
    builtins.help = 'new help'


def __import__(*a, **kw):
    print("BIOS IMPORT")

ENVIRONMENT()



def CONFIGURE():
    print('CONFIGURE')
    if os.path.exists('CONF'):
        puts('discovered configure CONF')


CONFIGURE()


"""bios.initialize functionality

The first function to start for any VOL,
imported by the runtime as default, the autostart calls
the intialize.

The init creates the base read writes and imports the correct
packages to import a kernel.
"""
#import os
#import sys
import builtins
from bios import puts, BEEP

builtins.help = 'new help'

def POST():
    print('POST')
    return 1


def execute_system(system, scope):
    puts(BEEP, '\n')
    if HEADER:
        puts(HEADER.get('welcome', 'New System'))
    else:
        puts("System HEADER does not exist.")
    puts('\n')

    setattr(scope, 'system', system)


# power on self test
POST()
