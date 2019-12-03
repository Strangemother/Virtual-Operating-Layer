# View Driver Graphics

The connection between an active VOL an a gui of some sort. The graphics layer
generally translates commands from the VOL to the UI given loaded modules.
The modules consist of a translation and presentation layer but generally performs
throughput.

A module should be inherently bi-directional, allowing support for interface driven
input such as touch screen or client-side loaded hardware.


## Module

a single module may be loaded into the runtime to read and present information
given from a VOl. Consider it as a simple translator.

Initially the module loadout will support a html gui from one or more connected VOL.
Going further modules will support a range of input and output utilities. They
will not be strictly _graphical_, but will provide an analogous to data output.

### Back/Front Divide

A module will maintain a _backend_ and _frontend_ persistent layer for bridging
tooling across the two distinct units of work. The backend or VOL provides a
_standard-like_ compute layer to architect a view structure.

Predominatently a VOL holds ownership of a GUI layer to abuse as required (a standard VDU)
and will action CPU bound tasks to communicate to the _VDU_. This should occur
transparently with the _VDU_ or graphics layer communicating any information back.
This simbiant design is wrapped into a module unit to enact or inherit as required.

Fundamentally the VOL backend layer is independant of the GUI Frontend layer and
communication between feels native.


### Coms

The communciation between the two layers is bridged with a communications protocol.
This can be anything a module can be; Websocket, Binary, File IO etc...

A module has executable output values to present and entire _producedures_.
A procedure may be pre-loaded to action upon a structured message.

The translation layer converts the coms message to a GUI format


### Architecture Flow

The flow is simple enough. The most interesting component may be the module loadout.

A modules has:

1. draw functions, back/front exection layers - src code...
2. drawing artifacts and vendor assets
3. load statements and run tools

packaged in a module fashion.

When loaded:

1. The module assets are extracted.
2. Pre-compiled draw functions and compute methods are distributed
3. pre-installation and loadout for initial instansiation
4. Bridges are assigned and waited

Drawing routine:

1. A command from VOL to output in a format expected `TEXT 12`
2. Send to the draw function receiver - a pipe or standard call
3. translator receives, digests, compiles the correct command
4. distribution to the attached GUI/output devices for further digest.


The implementing layer will differ per device. For a standard HTML GUI

1. Receive prelimary write commands `TEXT 12` - in a format for the initial pipe receiver
2. Convert to expected output - write to screen at place
3. Render change


### Loadout layouts

Loading a prelimary module applies

+ tranport - send a message to and from a gui
+ tranlate - convert the message to a gui form from a trasport message
+ display - apply to the display utility
+ present - render in a format.



### Modules types range


#### HTML

A number of presenation modules dedicated to general VOL to GUI presentation.
They overlap with other requirements for a basic (HTML) output

+ Translator
+ Layers for tiles
+ Structure and ordering.

#### Text

coms text printer as a basic cli output and debug/develop interface.
The text should also replace a gui if required


### Input

The bi-directional pipe for a module serves for input from a vdu client type.
Conceptually we can consider the _View Driver_ as more of an presenation layer.

At a hardware level, it serves well to allow _long-distance_ componentry to mount
through a presentation interface. This serves as remote-ability and lag reduction
for user input devices such as leap motions and joypads.

A Perphieral device may shortcut to the presentation layer, utilitizing a modules
native display components, or simply communicate to the backend for VOL computation.

A passthough method to allow input devices to present draw commands; such as allowing
a joystick to action `MOVE CIRCLE` or something...

+ Perihperals
