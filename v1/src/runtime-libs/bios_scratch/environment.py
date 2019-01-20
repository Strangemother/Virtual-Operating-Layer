"""Given a memory allocation key the environment reads access memory
and creates a an env given the paramers from the WAKE

Any mandatory instructions and extensions to the POST instuctions
provide procedures to run. Next step to CONFIGURE the base env for
the BIOS.

At this point output beffers are assigned, any host OS specific libraries are
applied and the allowed memory address is read to assign hosted read only
memory
"""

import sys

def ENVIRONMENT():
    puts('ENVIRONMENT')
    sys.ps1 = '\u25BA '
    sys.ps2 = '... '
    sys.prefix = '/VOL/'
    # sys.builtin_module_names = ()
    # sys.exec_prefix = 'exec_prefix'
    # sys.base_prefix = 'base_prefix'
    sys.copyright = 'Apples'
    #sys.path = []
    # sys.modules = {}
    #sys.version = (0, 0, 1)
    builtins.help = 'new help'


def __import__(*a, **kw):
    print("BIOS IMPORT")

ENVIRONMENT()
