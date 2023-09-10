# Phase 0

The initial stages currently required for the monolith readification into _base OS_ mode, where the OS may handle standard operations. In the monolith stage this is the very first step to building the base OS, then hand-off to basic operations such as the forever loop for REPL and "applications"

+ "wake" from the magicnumber hand-off or a simulated power-on event
    The handoff occurs with an address pointer to spawn the exe process.
+ (currently undefined) perform power on, any pin tests, or register tests
    monlith functionality to ensure the root binary can load

The monolith is the runtime root of the VOL. One monolith should cater for a cluster of device types.

+ run 'root binary' and setup the blank space for the incoming functions (wipe runtime)
+ create root language, core method and class setup
    These build upon the underlying runtime calls for _type_, _ints_ and a pointer _object_, producing the root accessible functions of "system", "registers" etc...
+ load virtual-ram functions for writing to memory
+ Enable/install enforced code - such as first-load AOP extensions and updates.
    the information is baked within the monolith and may be updated through protected changes during system events. Fundamentally this exists as a byte array of code objects loaded as extra lib packages leveraging an API to adapt root functionality.
+ load text print, disk tools, and other fundamental functions
+ read and register store 'house' events, such as _wake state_ or pin interuptts.
+ Perform last call changes given memory, root tools, and an 'init config' in the register
+ given the new (empty runtime) suite first user 'tape' into memory
    This is likely a bin file from the HOST directory on storage such as:

    + Flash SD cards
    + Network calls
    + 'baked' data within the bin or loaded graphs
    + A _real_ file in the HOST directory
    + at a register position (with length)

    It contains system relevent startup, user config and any _last state_ actions

+ read functions and continue tape loadout


Once the full user tape is loaded into memory the core functionality is prepped - with call functions and data ready for access. The next stage is loading more complex tools for the OS, such as:

+ Event Stack + Scheduler
+ Filesystem
+ Graph based memory
+ multiprocessing
+ REPL

etc... Once these monolith products are ready, the user OS tools are initiated for the GUI.
