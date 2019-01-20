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


# file: bios.pyx
include "config_class.py"

include "tte.py"
include "environment.py"
include "configure.py"
include "initialize.py"
include "execute.py"

# power on self test
POST()
