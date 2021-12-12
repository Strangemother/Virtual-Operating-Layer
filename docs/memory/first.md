# Memory Magma

"memory" is the first module to load - before or after the root install - allowing congitgious memory allocation and other 'block' memory usage. The top-level memory manifests as a graph mesh - with these base tools providing the raw access across other sythetic modules.

Each module may build its own memory mapped, Allocated to _itself_ and the _root_. The memoryview may also share across sources.

All memory needs a 'readonly' suite of bytes, governed by the root **only**. The initial boot-cpu may not by 'root' and as such the "protected" mode may not be locked to the open CPU.

1. A 'locked' memory space, containing none-user os bits
2. open congigious space, with facades for safe mapping


## Shared Bits

Some memory slots are assigned for the CPU only. They factor in the the first root bits.

+ ON State: 0 for initialised; 1 for secondary, 2 for protected state ...
+ initial time: The start time of VOl;
+ Internal offset: The _OS_ time, from as a delta
+ internal incrementals
    + two slots; #1 for _micro_ ticks, #2 for _master_ ticks for every micro overflow
+ Vector bits: for cross cpu vector clocks
+ Protect state:
    Maybe a bit to denote the _protection mode_?

## Protecting Spaces?

Currently unknown is "root space protection". Allowing the initial config of the system modules (memory, processes, sockets, etc...) to load within a _locked space_, with some sort of user-locking.

The "protected bit" is intially _off_ (or doesn't) because a blank memory. So the root installer should manipulate the memory.

1. "root" has its own congitgious byte range, with protected bits
2. Only access through the root may change the protected bits.
3. new security layers are applied until the root is in a fit state


## Address References

The memory module "bit registery" is available as congitgious addressable bytes, with facades to plateu memory addresses. The input address is masked through a virtual memory; allowing stepping through byte arrays with chained facades.

+ 0x00 > 0xFF : protected bits; expanded for more bits
+ 0xFF 0xN+ : mem addresses
+ 0xN+ : next congitgious spawns

Therefore mapping a facade:

```py
from memory import reference
# Bits(Major, Minor, Inc, Protected) == [3, 8, 1, 0]
prots = RootFacade(reference[0x00:0xFF])
prots.protected == reference[0x00] == 0

# Bits(Cpu_count, ...) == [2, ...]
prots = ShareMemoryFacade(reference[0xFF+1:0xFFF])
# Static memory mapping.
prots.registered_cpus == reference[0x00] == 2

```

## Data lock

Given a range of memory should be protected by internal and external bit flips, the system should actively (by request) monitor for unathorized bit flips within the protected memory.

1. All normal _writes_ are tested for protected auth
2. A contiguous byte test stores a _"CRC"_ of the current bits
3. A background clock tests for flips by asserting the stored CRC.

The CRC is stored within a 'protected block' of the congigious tools, - seperate from the main block, _below_ the `0x00 => 0xFF` protected bits - in the "negative" data space not accessible above the zero - root tools.

---

Further protecting this deep space requires:

+ MD5 store of the CRC whilst in RAM
+ Secondary CPU space without an entry - responding through sharedmemory bits
    This could also be a key response:
    + Open a new CPU process,
    + Connect to _initial root_ with a sharedmemory and unique name
    + The new CPU accesses the initial read back throug the unique key

    Each request to this secondary CPU should be initially authed through the shared mem socket.
