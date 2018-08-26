"""The intial script to boot a start environment"""

print("... VOL boot (0, 0, 1) Kerbechet")

keys = tuple(globals().keys())
# print(keys)
# for key in keys:
#     print('Deleting', key)
#     if key == '__builtins__':
#         globals()[key] = {}
#         continue
#     del globals()[key]

import bios
import system
# Assign for an instance head - At this point all confogurations, global functions
# and first layer functionality is assigned.
system.configure(bios, globals)
