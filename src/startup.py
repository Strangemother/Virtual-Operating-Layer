"""The intial script to boot a start environment"""
print("... VOL boot (0, 0, 1) Kerbechet")
import bios
import system
import head
# Assign for an instance head - At this point all configurations, global functions
# and first layer functionality is assigned.
system.configure(head, bios, globals)
