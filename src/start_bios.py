"""Mimic the initialization of a bios runtime
"""
import sys

sys.path = []
print('Appending runtime-libs/')
sys.path.append('./runtime-libs')
sys.path.append('./runtime-libs/core')
sys.path.append('./runtime-libs/win-64')
sys.path.append('./runtime-libs/env_lib')

path = "../build/bios_runtime/libs/build_libs"
print('Importing built C libs "{}"'.format(path))
#sys.path.insert(0, path)

import bios
print(bios)
