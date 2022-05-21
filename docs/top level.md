# Top level imports

Starting at the RING 0 or layer zero of the VOL terminal the base libraries for core operation.


## HOSTLESS (ROOT OS)

The less pressured option is a 100% VOL kernel, maintaining all the operations of the given HOST. This involves building an OS from scratch - and I won't do a better job than the existing.

Therefore akin to all other operating systems, a VOL kernel wraps busybox or another linux kernel.
A this point the low procedure calls (or inter process communication) are handled safely, allowing the selection of an alternative CPU runtime such as RTOS.

The bootloader is pretty cheap to make with copy/paste from the internet, but a better loader such as GRUB exists.


## HOST

For a Virtual Operating Layer the HOST provides a layer of OS abstraction. Given any host operating system a VOL will perform upon the same runtime, providing a layer of agnosticism for incoming services.

An optimal HOST defines an Operating System compatible with the given C _exeutable_. Compilation already caters for:

+ AMD 64bit windows (EXE, COM)
+ AMD 64bit linux (SO)

Other expected targets are:

+ ARM Android
+ Apple iOS, second gen+ (2 CPU core+) minor and major platforms
+ Intel 64/32bit Windows/Linux


Fundamentally with a Linux kernel core as a HOST the deployment options are limited to the compiler. Therefore overall the expected beta should work upon:

+ Linux Kernel: Tinycore/Busybox; other majors
+ Andriod, Linux, Windows
+ 64bit 32bit platforms


Pretty much all the major platforms.


## TERMINAL

Once _deployed_ the BIOS, System and base runtime exist within a separate thread. Communication through a federated pipe owned by the system.

At this level there are no services or actions, the base operating modules are applied given a hand-off from the `system.configure`. The initial interface maintains its own CLI - being _non_-headless. Once deployed - it's a consideration to provide a headless VOL VM.

Base `TYPES` are set such as `int`, `float`, `chr` along with basic class construction methods such as `type`, `staticmethod` ... Exotic types for BIOS operation are set such as `oct`, `Exception`, `raise` etc...

The core BIOS terminal is Turing complete, given enough framework from C.

The runtime terminal can run HEADLESS or with an interpreter. It provides access to the available imports and master configuration. Given the ZERO state of the machine at this point - there is little to speak about permissions or services. Fundamentally the system configures then sits for input.

Once the `system` has configured the `head` using the `scope` from the `bios` the entire session is deleted, leaving no variables in memory.

At this point a user may take control - providing instructions as Layer 0.

The first routine to import should be a `configuration` of some sort. Loading runtime core services and essentially _starting_ an operating interface.


# Imports

Within an active runtime the system routes all imports through the BIOS. The runtime should _event_ this and continue with imports. At pre-initialization of Level 0, no core system libraries or routines exist for access. They should be imported and installed.

_Fundamental operations are in-progress_


Each defined article is a system core service _(*routine?)_ for base runtime. These fundamental components abstract OS essentials for Level 1+ the GUI.


## Root Types

A range or root system types to work within the turing Layer 0. If your a C or Python developer you may notice something fishy with my _new_ root types...


runtime `root types` are compiled into the runtime.

+ simple type
+ complex types
+ abstracted complex types
+ root math
+ string types
+ root classing
+ root methods
+ root interrupt


A root var may be one of a `simple type`:

    int
    float
    bool
    True
    False
    None


`complex types` manage simple types:

    tuple
    set
    list


`abstracted complex types` provide a OOP layer for `complex types`

    object
    dict


abstracted complex types are `system` managed. An abstract complex provides some other types not listed.

`root math` functions:

    complex
    abs
    max
    min
    divmod
    pow
    range
    round
    sum


`string types` for basic string character manipulation:

    ascii
    ord
    bin
    chr
    str


Complex class structures build upon the given `abstracted complex types`.

`root classing` for OOP design:

    type
    super
    classmethod
    frozenset
    callable
    property
    isinstance
    issubclass
    staticmethod


Methods for class and memory references. The `root methods`:

    setattr
    getattr
    delattr
    hasattr
    hash
    id
    len


Runtime ` root interrupt` types:

    Exception
    KeyboardInterrupt
    NotImplemented
    StopIteration
    GeneratorExit
    StopAsyncIteration
    SystemExit
    TaskletExit

---

HAHA gotcha! Indeed these are _burnt into_ the runtime with all the concepts collected from existing C and python libraries. They may the same lib or a stolen name - in either case I thank the open-source community for naming my variables and writing some code for me.

The incoming modules define _these_ top-level appliances utilizing the `root types`.


## filesystem


The base IO for persistent data stored locally within freely addressable memory. Dubbed a VFS for "Virtual [Operating Layer] File System" _(*another name?)_ with CLI pinched from C standard STDIO

+ `open`, `close`... and other base operations
+ Encryption, Decryption, Auto hashing.

Extending further than traditional file data. A example _file_ consists of some meta data, a data dictionary and data segments defined as hash managed blocks of bytes.

As a quick overview:

+ A _file_ is a random access dictionary of addresses to uneven chunks of bytes within memory
+ Each _file_ maintains a recorded hash of the current state calculated upon each write to a file structure.
+ The `filesystem` maintains an open hash until a file is closed writing to _file_ meta
+ meta of a file holds VOL persistent information of the _file_ data dictionary such as local name and immediate hash.

The data segments exist without an associated file loaning addresses through a linear dictionary only accessible through the `filesystem`. A virtually allocated memory table persists a record of real memory location to a given hash address.

This serves as a safety mechanism for overwriting addresses. Moving data segments is not required; as a file does not maintain a _linear_ address list. Therefore a data segment does not need to live with a _file_

    filesystem
        open
        close


    fileio -> write byte --> put to MEM on assigned ADDRESS -> spill to new segments
                         |
                         |-> calculate persistent hash
     -> save close       |-> write hash to meta -> put floating segments to persistent -> clean mem



## CPU (threading)

The CPU module and importable provides a CPU Task management and threading control to distribute work across a systems given hardware threads. the wake, sleep feature for any given task is mostly handled manually although thread locking and noise control should the handled by the VOL

    cpu
        spawn
        exec
        _close_

There is a lot more to be applied here. However the given api will provide a user with:

+ Immediate stateless tasks
+ Headless or non-headless spawning of tasks and long-process schedules
+ Lockless CPU threading (no suck thing as a thread lock)
+ scheduling; cooperative and preemptive
+ automated interprocess communication with pipes or data-segment hand-off
+ True runtime detachment (allowing run-away zombies) with atomic execution across tasks
+ microthreading; self-serving processes for short periods?!
+ OS independent tasks


## network

A top level module dedicated to all things inbound and outbound. All ports, and devices are managed through this. Without the `network` module elements such as _mounting a LAN card_ is not possible.

Catering to personal requirements and anything I can think of with regards to packages for networking some items will overlap with other top level modules

    network
        devices
            local (lan)
                ... intel
            wide (wan)
                ... intel
            wireless (wlan)
                ... broadcom
        ipfs
            ... ipfs mounting


## compile

A compiler built into the runtime serves for live assembly of class code. A unit is compiled into the HOST or VFS type to run faster as an optimized C conversion. At the moment this is `gcc` wrapped into the code with enough bits to run for compiling VOL modules. This will change to TinyC hopefully.

+ receive a VFS or HOST source to compile as a VOL module

    compile
        source


## assembly

An assembly tool built into the runtime serves for live assembly of \*NASM? code and read executable instructions generated by the compiler. This is used for user API and internal debugging.

    assembly
        read(source/package)
        compile
        disassemble
        ...


## interface

A majority of the UI is offset to other hardware - such as VGA / GDI or direct to GPU using a suite of given service drivers for interfacing with major cards.
I feel the easiest (and smoothest) route through OPENGL or GL in general can leverage web and desk with the same API. To serve on the desk through a HOST using a gl engine.

By designing a translation language for device to GL to transport across networks. Essentially this is RDP so utilizing DirectShow and Xserver seem like the best option for HOST served VOLs


## Health

A doctor/anti-virus/defragger/verifier management unit for keeping a the system health. Primarily I see it as a sandbox task verifying background services and testing files.

+ ran in a sibling task isolated from the main VOL
+ performs the file-hash checking for change verification
+ A thread monitor for services - as a firewall for rogue apps

