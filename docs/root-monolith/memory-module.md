At the root of the monolith the core modules load a pre-suite for incoming os application. The lower (first) order modules provide the root functionality of the monolith including memory allocation and yielding of base functions.

This may be considered a _kernel_ bootstrap loader - where the loadout governs the monolith build. After a memory module has loaded; its accessible through the open interface.

These modules should be self-loading - applied to the "start process" baked into the linear read of the monolith. This should manifest as a sequence of 'baked modules' within the kernal (the entity loading and running a monolith) source.

This may also be understand as a _driver driver_ for the monolith base apps, such as the filesystem and repl.

---

The VRAM rootest module contains a reference of the first memory bits to allow kernal loading. This unit allows the base read bit from the baked loadout to initialise the memory locations and allowed functional stores.

This also stores the _init bits_ for the cold or warm wake, followed by graph bit key identifiers, and the bit step.

---

A memory module has access to a memoryview byte array, given at a direct address to start reading; In turn this may also be served by a memoryview byte array.

Each Memoryview has an API callable exposure, yielding formatted results for the graph stepping digesting entity. Each reference in the memoryview points to another key reference
