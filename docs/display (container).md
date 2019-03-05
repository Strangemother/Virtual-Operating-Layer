# The display layer

The componentry dedicated to presenting render strings from one or more VOL.

the container maintains an interface to a local or remote VOL utilising a
special driver for local digestion

The container runs as a self hosted web view with a local service decoding
a stream from one or more VOLs to render in the live view.


# Ocipital Cortex

The occipital lobe is the visual processing center. The cortex is the outer surface of the cerebrum and is composed of gray matter. The motor areas are located in both hemispheres of the cerebral cortex.

The Ocipital Cortex is a topological view of the interior information, presented though data streams to a visual pipeline - abstracted and rendered through a visual container.


## Container

The rendering container is one of the 'mounted' components for the VOL as _display_ driver. It's designed to receive streams or single-shot render commands, presenting them within the rendering context. Similar to an xdisplay driver within a standard UI but couples a graphics callback suite and centralised rendering pipeline, allowing bi-directional graphics streams to more than one HOST unit.

Fundamentally the setup defines HOST > VOL > DRIVER > CONTAINER > RENDER. 'Driver' and 'render' being psuedo concepts. the container offloads all the graphical rendering of the VOL into a self-contained unit. Connecting to one VOL results in all rendering dedicated to one system. For larger platforms, many VOLs can communicate to a single container pipeline - for multiplexing and shared graphical drawing.

_To Quantify my personal goal; allow many seperate apps and systems access the same graphical unit, through the same pipeline without distinction. Text and graphical layers are applied  through an application level, not a system level._

A Container hosts a set of libraries to leverage the deploted platform as a graphics layer. The front-end implementation will naturally provide the following contexts:

+ Text
+ vector
+ Pixel
+ GL

Applied to this is the overall _styling_ and os theme. In addition you have the raw access container layer to manipulate.

---

A Container may do more than present visual content, such as bridge hardware or return data from inputs and inspections.

+ Audio
+ Hardware input (Peripherals)
+ Software input (RPC feedback / session info)

---

All this is served through a JS HTML CSS Implementation; compiled into the container as a _design_ platform. The graphics suite is a dumb architecture with the ability to _hoist_ routines into its core runtime.

Base layers provide a subset of ready libraries to manage the core contexts provided.


## General Manager

The graphical management is griven by a number of position directors with the VOL and container. They will have a number of roles, namely ensuring an incoming stream or shard of content is displayed in the correct layer.

## Layer Acquisition and assignment

If an app/VOL or utility owns the entire rendering procedure for container content, the owner application manages a set of ID assigned layers to present any content.

A Layer assignment defines a draw layer and a display hook for the application, to access through the RPC render pipeline.

## Text

The most-default for representing content given by a VOL is basic encoded text. This is given in the form of raw strings. The container accepts a raw string and applies it to a text rendering layer similar to standard out of a HOST. If a draw layer isn't chosen, a default layer for text is given. This is for VOL Boot rendering and other stdout wrapping.


## Vector

A Turtle draw routine for vector drawing.


## Pixel

Generic pixel layers allowing composite (canvas like) per pixel drawing. Notably these will be absolute based.

## GL

Using OpenGL/WebGL or a translation of GL in a full-depth suite catering for complex 3d graphics, shaders.


## Offload rendering

In cases where VOL should utilise the HOST, a 'offload' panel provides a rendering layer _outside_ the general manager and standard layers, but within the container rednering pipeline. Such as a DirectX window within a Windows 7 HOST.

Presenting content such as video requires a DirectX or DirectShow HOST window. Initially this is not rendered by the container. Instead the container maintains an alien thread and _transparent_ portal to the HOST drawing later. This allows a container to manage the lifecycle of an rendering panel with an external loci.

In true form, the _transparent_ window will exist "on-top-of" the VOL contatiner, some work is required to ensure the layers correctly index - ie a 'frame' renders as an overlay of a video.

In other cases this includes:

+ HOST Applications (any application started through a VOL)
+ External Game engines or direct rendering units
+ 'cut outs' for unique screen shapes (and the new-world issue of notches)


# Base

For each layer a free encapsultion given by the VOL provides easy leverage of the layers without accessing the _deeper_ api.


## Text

For any standard text layer the styling is naturally applied by the system. Elements include:

+ Font family, write-mode settings
+ sizing, scaling and rendering factors
+ color or general design

In a new world, VOL provides technical appliances offset by a container, such as text wrapping, advanced rendering modes - all given through a blink renderer. In an ideal world an advanced text layer consists of a 'design submission' and a recurring text steam. The text is dispatched to the relative layers(s) through ID assignment. All complex is offset to the VOL container layer design.


### Vector

A default vector base provides drawing capabilities and update routines to live draw SVG style content to a VOL.


### Pixel

The core pixel layers or 'canvas' style drawing provides a middle-tier to scalar drawing and full GL implementation. With the core features, all standard pen 'draw' methods allow a developer to draw without limitation. There will be cross-over with other layers - such as presenting text, Lines, Primitives etc - but the choice of layer type is designed by the app.


### GL and 3D

Given as full-fat access to the GL draw layer, the HOST will maintain most of the driving capbailities of the 3D engine. Therefore system integration should be clean.
With the _base_ routines for leveraging a 3d layer, a complete 3D environment should be available. Access like a simple 3D engine - built into the VOL container.

All the expected features of a 2D/3D framework will be included. Definig the very basics:

+ Lighting and all primitives
+ Rendering loops and animation routines
+ Usual host of a capable env: HDR, textures, poly reduction, physics etc..

This can be used for data-rendering, vr and games.
