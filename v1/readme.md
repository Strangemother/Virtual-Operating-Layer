
# Readme (2)

Heh. This project is a sleeper.

## Intro

The VOL is a personal project to define my own custom operating system, graphical layer and distributed computing system - All rolled into one
thin extremely customisable layer to _boot_ a fully integrated operating layer for a software platform.

It combines the concepts of an operating system without the shackles of the existing paradigm by providing a logical (and graphical) implementation for modern machinery.
Personally side-stepping the 'operating system' identity I feel it's banded-about on any slightly custom version of Linux. That isn't an OS - it's a new desktop...

As such this project does implement its own bootloader, a unique filesystem (in progress), CPU management and distinctive features for the core operating commands and running platform. It also implements a Linux kernel and C based MCU/CPU instructions. As these elements evolve I can eventually call this an OS.

In its current roadmap the VOL applies a working concept for the initial platform. The next stage will destroy all this for a better build-out.

## VOL Runtime

The base IO machine maintaining all logic. It is an EXE or SO - evolving to a SYS or _linux_ core SO driver. The core defines the REPL for the CPU and FS routines.
Some throw-back terminology exists for the core libraries - such as `bios`. But they mostly facilitate a conceptual connection to the _current_ relatively named software layer.
Such cases as `bios`, `fs`, `runtime` and so on - may be do impossible things in a VOL.

+ Stackless one-language routine - Linux comparble: Schedular/runtime
+ Integrated REPL and Turing complete base IO
+ Platform agnostic - runnable as an 'exe' on any system
+ ... But is natively comfortable in a VOL core OS build  - such as busybox.

## Vol Core

Noting two use-cases, the `VOL-core` consists of a custom linux kernel and base routine VOL software. Development dictates a VM and crappy machinery but it should run _tiny_ in any environment. A personal feature of running directly off the disc, in RAM or GPU.

Currently the VOL runs as a standard EXE - booted by a C loader directly into a raw repl. Essentially booting into a _blank space_.

## Features

Working progress - but the intended platform defines the entire operating suite - down to the assembly - with all features of a normal OS. In addition

+ It should be small - hopefully fitting within an respectable amount of RAM or GPU - but also tiny disc
+ BIOS, Self sandbox VM load suite.
+ Optionally Encrypted
+ Custom FS Routines
+ A fully integrated graphical platform
    + Vector
    + Pixel
    + GL
+ Headless/Graphical
+ User management
+ Remote / distributed / agnostic
+ Optional CPU Realtime with IOT compatible routines
+ Built in system-wide state machine
+ Mesh / cloud native
+ AI compatible machinery
+ Self-documenting?
+ Native DB key value store - with pluggable machinery such as offline-clones; graph DB.


## Fundamental

Stripping a computer to its core and owning every byte has been my personal challenge since I met a BBC micro.
A lot happens within a computer we don't understand. Knowing what happens on the metal should not be a privilege.

This project serves a personal goal for continuity of development, in a platform I can entirely trust because every layer is open-access.
Some key features:

+ Integrated core graphics
+ Works _on top of_ another OS within a purpose built custom VM
+ Utilising any open source and dropping any legacy


## Platforms

Rendering to any platform is really just saying having the correct wrapper for the target system. Obviously the target system is Linux - and then a custom flavour of the kernel.
But other considerations apply extra layers to the overall core featureset:


### Android

dual-booting android isn't possible for all platforms. VOL should should on any old system - resurrecting a draw full of old devices.
Therefore if dual booting isn't possible the 'container as a deeply integrated app should suffice - with a 'take-over' routine.

Native integration with hardware will be required; but I'm hoping as a _VM_ container, the wrapper should maintain the `HOST` hardware and drivers


### Windows

Windows gets a lot of hate but it's pretty accessible to the core. The initial deployment is a deeply integrated _VM_ container, with a `HOST` allowing throughout.
Although dual-boot is possible, it's not necessary to facilitate a happy VOL environment.


### Linux

The `core` is built on a Linux kernel. Therefore there are no limitations. A custom form of the kernel is fun.
Additionally Ubuntu Core looks like a great deployment option.


#### Mac (iPhone/iPad)

It's a bit tricker deploying freely to an Apple device without jumping through some hoops.
But modern devices will run the VOL runtime as an application - albeit hosted within an 'app'.

As older devices installation of a signed app may not be an option. _(my old devices are disconnected from the eco system)_.
However the VOL runtime may run remotely _(headless)_, providing a UI as a GL or web app.

Running as a HOST device may not be an option but in it's third state the device may run a `NODE` for computation and device access -
yielding arbitrary values from a connected device.
_This is mentioned as VOL will persist a OS mesh - interrogating devices and utilising leaf nodes as computation point._


## Concepts

Removing much of the core functionality sounds ridiculous as it's been a near 50 years of history for `print()`. So it's more an entire wrap-up of all the feature points of an operating system. Leading to an agnostic platform leveraging the HOST device. The goal to _mesh_ all connected device under your own distributed OS needs an interface. I don't feel it's possible to note all concepts in a single sitting. I feel start from the top - I.E the users perspective is the fastest approach.


We're currently grounded by yesterdays analogies and limitations. Todays technology has organically formed our routines and we accept them but every-so-often we all perplex over _"why is called a 'desktop'" or _"Why 8/16 bit"_.

Now we have blockchains, hardware AI, GPU and massive data throughput distribution. Not to mention silly-cheap memory. A lot of which is a bolt on to an existing suite of software. We don't need to do this anymore. So this project is a definition of visual and technical continuity for the modern human. Ignoring the requirements of yesteryear.

How is that (any where nearly possibly) achieved? By only picking the predominant technologies of today and building a thin framework to extend later.
Being extensively open and self-evident the sub components are switched quickly. Starting with a _no platform platform_ it starts to sound like an operating system.


### Desktop

A slight abuse of the terminology 'desktop' as the current analogy of our visual interface for the chosen OS; but for VOL there won't be one. Or at least initially - a discernible core interface to 'look at' on one system.

The core runtime exists as a subset of many nodes existing in a pre-approved mesh of devices. Given the correct hardware an interface can be summoned through a graphical container or driver renderer. As these features are not part of the _core_ routine, there is no 'desktop'.

---

To replace the core UI, the VOL has three base graphical implementations. A 'driver' will translate VOL changes to one of the GIU. This is leveraged by a container renderer.
The `container` lives on a HOST and may display graphics. With the correct drivers for the container, a translator converts machine states to the VOL GUI.

#### Usecase


In an example case I have VOL on Windows, interacting through a container watching a (DirectX or DirectShow*) VLC mkv within a 'window' - the remaining interface is the 'desktop background'.
The VLC HOST application or HOST<>container driver connection presents a video stream leveraging windows DIRECTX video layer. All the logical computation is offset to the HOST and VLC.
The VOL container hosts a _portal_ to the Windows leveraged content with the remaining desktop rendering Vector, Pixel, GL _background_ layers.

In this case the background layers are rendered by a HTML translation in the container using SVG/[WEB/OPEN]GL/CANVAS graphically.
The VOL runtime or CORE may be hosted on this example Windows machine, tagging it as 'local' or 'remote'. The container interacts through _some_ visual presentation protocol, receiving graphical procedures. _So I guess I've just explained Remote Desktop or any pixel driver._

Moving to another interface does not destroy this runtime session. The container may cease rendering but in the distributed mesh will continue the session. The Windows HOST running application may not continue.




# Running

The `run_vol.bat` will boot a local instance using the local env3

For a very thin container:

    python container/cef.py

For the full VOL suite:

    python vol

this should boot the container, a system thread and the UI in the CEF container

## Usage

the VOL package should be everything you need [Not implemented]:

    $ vol -h


When working with the base runtime or developing compilations you can run the source using python or the built-in runners

1. Run the 'build/boot.exe' or `boot.so` - booting a runtime in a cli.
2. Boot a headless 'BIOS' - which is effectively a ugly version of _python_.
3. Run a startup env; capturing utilizing a runner env (Will change). This is essentially useless though and will yield a useless prompt.

        # in the runtime folder.
        cmd /V /C "set PYTHONSTARTUP=startup&&vol_runtime.exe -SsqOO"



## Build

Much of the work is C and python. Focused towards a windows builder at the moment; because I'm deving on windows and it takes less effort to compile on linux.

Requires GCC and a python 3.6 env - the VOL and BIOS Runtime has its own binaries
within runtime-envs.

Run `build.bat` from the src folder. This will use all the `build-script` to create a `build/` directory sibling to the `src/`.

### Partial build:


Build the extensions outside the builder:

    python setup.py build_ext --inplace --build-temp TEMP


Build the boot exe alone using `gcc`

    gcc -shared -o [FULLPATH]\build\boot.so -fPIC boot-script\boot.c
    gcc boot-script\boot.c -o [FULLPATH]\build\boot.exe


# Changes

The first boot process is done entirely client-side in the JS. This was a chosen driven by portability, allowing the _UI_ to run on anything independently. However I didn't factor in the complexity of writing a BOID protocol directly in JS. The alternative to remove all core application work from JS and rely upon better messaging.

This allows for a better, cleaner development of BIOS processes. All target devices can run python in some fashion. UI work is offset to a messaging process of commands for a UI build.
This is in accordance to VR and 3D platforms

In addition the newly finished Graph DB and AI layers are built in python.

Therefore the entire JS system will be rewritten to a python version with dependancies upon other non-python modules such as Nim and C.
The python is later recompiled to C based and the JS through Typescript - again compiling up from ES6.


# Assets

Load core assets for the desktop framework

# Features

+ Multi screen though websockets and protobuff
+ Abstract Syntax Tree

    Analyse/rewrite/porting of the core application through a built-in abstract
    reader

+ Auto docs.
+ Multithreading to the core.
    + fully Off-thread for main features
    + multi-core through server connection and additional threads
+ Class tree renderer
+ ASM
+ Class baking
+ Persistent data through graph database

# Noted Appliance

+ full CEF app

The full application of the core desktop extends into the CEF container. Producing
a complete platform with native integration.

The "VOL" (Virtual Operating Layer) is a GUI for rendering an app, designed [above]
with iso-morphic extensions for bridging core code into UI code.

With python, JS and a lot of clever the container (python local) serves a CEF
with an app driving the full implementation (JS, HTML). Applying bi-directional
application programming and layering all the concepts wanted.

+ (VOL) Python backend
+ (CEF) Middle tier
+ ES6 frontend
+ (GFS) filestorage
+ (Hyperdex, PROJECTNAME) Hyperspace distributed data layer
+ (Code) Cloud connection

# Purpose

A well-presented full UI layer to the scatter nux project. It will implement
all features for distributed application development, with a UI layer for
integrated environments and extended graphical development.

A UI deployable on any interface:

    + VOL CEF container for desktop localisation
    + Browser based
    + API UI Integration base (like screen VNC)
    + Mobile through remote coms


## Funz.

The core feature-set implements all the researched components for the Nux project.
Providing an open-source architecture for desktop-like applications on
a homogeneous platform.


# Structure

+ ES6
+ Assets

The interface has no layer of rendering owning rto its distributed nature. An interface is a feed of UI components fed through rendering pipelines from a GL interface, websocket instructions or another thread.
