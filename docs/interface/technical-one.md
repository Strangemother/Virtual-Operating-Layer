# Technical (One)

In the first technical implementation, The goal is to decouple the UI from the graph layers - allowing segmented loadout (A _visual_ mesh) and the updates. This is done with a few considerations:

+ A textual piping strategy
+ A 'displayx' style management
+ layers and 'active displays'
+ update events (from back to front)

## Phase 1

Phase One builds an interface of HTML elements, in a custom frame. The backend sends 'updates' through a visual mesh, responsible for ferrying information from the back to the UI layers.

The initial flow allows for OS style 'layers' and components - to build upon a base of _windows_ and _panels_. The content within a layer (or _window_) is owned by a connected graph context.

An application may hook into the visual api and dispatch commands. Some being `box` or `text hello` for example.
An independant "display driver" manages API input and drives the connected display. More research is given within the 'graphics' docs - however target displays include _full fat_ or micro displays.


### Interface Updates

"anonymous cell hooking" integrates active API changes to a UI element, through an _anonymous_ connect, from the mesh API call - into the display.

A call to upate the UI may be _anything_. In this example we focus on push _some information_ to a prepred cell on the view. The interface maintains a _true path_ to the UI cell, such as `notepad_status == root > layer 2 > window 1 > appname > primary > status_bar > cell 3`. The calling property nominates a value into the cell, where the display driver may push the content into the live view.

The backend will fire many 'update' events through the view mesh, The driver will convert all into this pushed sequence.

### Stored Procedures

The 'display driver' may bind _stored procedures_, to perform baked-in actions. The procedure may be a simple "hello text" or perhaps a shader vertex fragement. The display driver graph pointer will know how to integrate the content into the working UI - A dev may call upon the procedures to _sandwich_ complex actions.


### Update pipes

An interface is updated through a range of connected _pipes_, built around any favourable protocol. In the first version:

+ Backend: Living on a CPU, clocking a _view_ graph
+ frontend: Existing on a system with a display and the correct display graph installed
+ pipes: A range of web-socktes, udp sockets/pipes

In the _HTML_ flavour javascript catures inbound api requests (e.g. through websockets) and performs update through a relative graph, existing on another thread and bound to the live view.


1. Backend requests an update `status_bar = 'ok'`
2. stream through visual mesh
3. captures by the UI machine
4. injected into the display driver;
5. JS convert to a real path
6. Update the view.


# Direct Display

Other cases require a direct to view update; such as video streams or other (windows style) DirectX windows. In this case the view graph should setup and release the stream directly to the associated owner graph. The owner may _program_ the visual slot according to the HOST OS and personal requirements.

In an example VLC video player produces a DirectDraw stream, for the developer to hook a display handle. The view _rectangle_ is updated according to the VLC dll, and the position of the cell is owned by the window manager.

The same should occur with VOL - where an _app_ requests a "direct draw procedure" and given the correct HOST integration, the application may act upon a _normal_ rendering service.

---

In future iteration the VOL binds live libraries, such as Vulkan (because it's easy to integrate and very pretty), And the view procedure will dispatch blocks of vulkan API procedures - of which handles a _window_ to its own spec.

The VOL should handle this process as a sandboxed "host app", where internal processing is mostly handed-off to the HOST OS and the graph procedures to execute the correct integration. Much of this functionality should exist within the core procedures - as part of the 'view graph'
