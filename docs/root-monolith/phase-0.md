# Start

The core system executes a _graph_ and pointers. The _loop_ actuates the motion of the walker. Each pointer execution yields changes within the persistent store.


## Graph Key 0

    Much like an operating system has a 'magic boot address' to execute the real OS after the bootloader segment has finished its load, the VOL has a 'start point' on the graph to initiate the root monolith config and module installation.

    As the VOL primarily executes within a ready environment, and the memory method is a flat graph, ensuring we initiate the correct memory address is a case of _locking_ a graph ID.

    Some ID's within the graph are read-only, reserved for internal operations.

    --- [./readme.md "Graph Key 0"] ---

> This information documents the process within VOL and doesn't account for HOST hoisting.


---

The first stage persists the _loop_. The VOL monolith requires a build blank space, and a process to load. The initial graph will likely be an empty loop, requesting a magic key (boot point).

Beneath the users loading magic key is phase-0 or graph key #0, protected and owned by the BIOD. This performs the phase-0 test, including power on features and core library loading.

## Reading #0

Read more kernel.md

The user settings are baked into the root tape and a (protected) memory store. Some fundamental libraries are:

+ Schedulers
+ Steppers
+ Pointer Executors

All this exists within a loop, stepped by the monotlith, through a graphing tree.

Within VOL terminology this requires a

+ (system core) monolith
+ a range of root internal membranes
+ The FS
+ _"Cells"_ connected to membranes (mesh.md)
