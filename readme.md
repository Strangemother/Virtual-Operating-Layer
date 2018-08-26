JS desktop for nux.


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
