The OOP frontend and back maintain their own archiecture and comms.

1. Graphics representation exists independantly of a HOST


# Base Layer

+ Free input given through the transport layers.
+ Each layer is subscribable, creaed or recycled when required.
+ Inputs are piped from a HOST.
+ Each host manages their display accordingly.


A Layer applies the base output, a transport input and its own suite of code.
It may live as an service on the main host, but it design to be a self-service
visual. In a 'desktop' mode standard GL connection will override this to provide
a core experience, however on average all the graphical functionality should be driven remotely.

_IJT: Sort of like a website, where pre-composed units are sent to another VDU._

+ A layer is spawned or used by expectation of the owning HOST.
+ A Host will stream commands or executables through a subscribtion pipe.
+ The driver stream input stores and executes given commands, returning events and
  presenting changes.

For more complex drawing such as Direct Draw or GL, a driver to shortcut the remote
connection allows a user to leverage the Driver as root. Fundamentally if the graphic
unit is attached to the host device, a module-loadout should supply a stream pipe...

In addition the core system library supplies a GPU platform for computing and
standard graphics. Any more-complex units are _handed off_ to the HOST OS (if any - such as windows. )

+ Text Layer
  Acting like a stdout a text layer present lines to the UI. A HOST will stream
  to a subscribed text layer.

+ IO Layer
  The XLIB/HTML full implementation of an interactive suite, allowing a developer
  to write a platform. The interface is generated and managed through pre-built
  units.

+ Draw Layer
  A Graphical platform for extended drawing. Spawned normally, it allows complex
  drawing using a given API or custom module loadout.

  + 2D SVG, Pixel,
  + GL


# Core

The core library provides a base layer given my the os. For leveraging modules and drivers.

The `head` hosts the global root for all modules. Applying elements to the root allows cross module communication and base suite loading.



