A comprehensive list of actions to complete for the Root monolith to execute the base VOL.

Hopefully this helps me to plan out module order, and discover module _alpha_



+ Runtime
    The pre-defined functions loaded for _execution_ of statements in the working
    memory. In dev and "container" mode the runtime is a stripped version of the
    macro library (thin python) - with no global modules or functions.

    the predefined "os" module assigns a AOP class ready for building core units. This is loaded from the _baked_ core class, loaded by the bootstrap mount.

    +

+ VRAM
    The first allocation section for input data. A closed space for memory allocation
    Set in "pages" to facilitate data division, 65K per slice sounds normal.

    + Memory allocation functions
        + Byte array sequence reading
    + pointer reference set.
    + A base 'runtime'

+ echo printer
    The ability to emit messages from the base

+ Memory Modules (Store)
    A module for storage and root tools utilising the VOL dynamic module loader
    of `system`, `bios` etc... The memory module works once other dependencies perform any initiation - such as RAM, kernel config, and any other 'baked' binaries for access.

    + auto-executing module list
    + API for base imports
    + Dynamic module importer

+ Register (Pointer and Location)
    A config key base for memory pointers and register locations

    + Memory store

+ Graph Memory (Graph tools)
    Basic functions to read and write through the graph

    + Memory Store
    + A pointer register

+ Event Stack
    A System long queue to push execute steps and evaluate results. Just like a python event-loop however capturing the functional results from the (builtin) async executions. Requires:

    + Memory Register location
    + A Push Queue

+ Resource Reader
    An evaluator for the read execution, running functions and storing outputs into
    a register through the loop. Requires:

    + Event Stack
    + Command translator

+ interpreter
    The base eval receiver, accepting commands executing transactions

    + Value input (SoC UART Style)

+ Filesystem (Graph)
    Store data in a graph.

    + Graph Memory Read / Write
    + Driver selection

+ REPL
    A stream reader interpreter, with input and output stream readers. Requires:

    + Filesystem
    + A UDP/Socket IO
