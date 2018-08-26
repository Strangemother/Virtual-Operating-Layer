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

builtins.help = 'new help'

def POST():
    print('POST')
    return 1
