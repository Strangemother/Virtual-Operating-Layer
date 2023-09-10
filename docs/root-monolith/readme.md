# Root Monolith

Beneath the "os-runtime" a core suite of language and system tools provide a monolith of base functionality to interact with the HOST. The base _language_ assists the input prompt and base loadout of _bedrock tools_ such as multiprocessing, async execution, and REPL command entry.

Root core modules include:

+ root 'text' printing
+ UART and ping signal response
+ exception handling
+ The language pre processor
+ The REPL receiver
+ Websocket connections for root VOL REPL reading (with bytestreams)
+ multi-processor allocation and source execution.
+ runtime Module loadouts
+ early config management
+ graph methods
+ realtime clock integration and scheduler



## Startup

+ https://en.wikipedia.org/wiki/Cornerstone

The monolith is built with all source for the expected deployment. A single monolith
should exist on a target device, executing the "baked" startup sequence deployed as a finished _binary_ preparing the foundation of the VOL, ready for the 'cornerstone'.

Target Segments for the VOL include:

+ Raspberry Pi devices,
+ Wearable SoC
+ "container" for HOST systems; Linux and Windows
+ Mesh integration of HOST, DISPLAY and target.

As such the Monolith may include several sub-suites to build given the cornerstone construction. Alternative modules/RPC routines may be required per device.

---

During _startup_ the Monolith provides a root VOL for the incoming OS; essentially the Root of the root apps - including:

+ Display Text IO (and display drivers)
+ Base Graph functions
+ Testing suite for target-aware deployments.
+ Base configs


## Root Drivers

+ UDP COM for pre-cornerstone loadout (none websocket platforms)
+ Audio Beep
+ Core system (Foundation)
  + OS Runtime (Py core)
  + Schedule, IO Stream, errors, graph data (FS), configs


Initial

## input stream

The Root Monolith accepts a unending input stream for client REPL, storing the results into a walking register until the client terminates the issued statements. This is an from version _2_ where the input stream accepted single-shot commands only.


### Register

An input stream executes its moving pointer upon termination key sequence of characters within the register. Once the command has hit a threshold, the termination yields the next graph step, an execution, or an exception.

---

The input stream receives a live byte-set to either step the graph or execute statements within a digesting routine. These two distinct tasks are essentially the same function, for the _top level_ command layer accepts commands - of which step the graph to yield executables, to push data ..

This flow does not stop. At every point the input value is digested by the graph-stepper-yielder, or a executing function. At all times the system yields information through the output stream. A user should be subscribed to both (which should be the case with any standard TX/RX or bi-directional socket).

---

Every input stream has a locatable register point, of which a user is _inputting_ chars. Each char is stored and the input-session key is stepped; The REPL manager will action upon the result, sending a result to the output-stream and handling the node in the graph.


### Processing

The prepared edge graph of data and commands assign a literal stepping per input byte. Execution steps digest and yield asyncronously back to the client. Extremely similar to the existing REPL method. In this case each char input _steps_ the graph to the next graph-point, yielding a executable, or pushing data.

1. User inputs a char into the REPL
2. The Char is sent across an open socket to the stream receiver
3. The stream reader moves the graph key literal to the next step

At this point the graph yields and expected data, pointer, or executor. The yield receiver should act upon the continuation.

1. The user inputs a char, repeating step 2.
2. If the char is a terminator, the action yields a "command" completion,
3. The monolith digests the command as a complete expression.

---

As a conceptual example this acts similar to _forward typing_ in a suggest-box. For every key input, the char _steps_ the potential possibilities until a final value. In the VOL graph, every key input yields a key or executor for a command.

---

This is useful for data-resolution across spaces, but provides an initial method of realtime char entry for input streams.


## Graph Data

The data is hep as a flat graph and edge connection bridge the grains to form the readable bytes.

### Key age entropy

Data grains and particles store within the graph, connected through edges. A Particle should be pushed into a cold-store, off the RAM or main memory. This can be done through date access, allowing the grain and attached particles to _entropy_ away, being placed back into RAM when required.

---

Notable there is a lack of distinction at the top-level between RAM and Disk memory, as in future iterations this doesn't factor into the VOL methodology.


## Graph Key 0

Much like an operating system has a 'magic boot address' to execute the real OS after the bootloader segment has finished its load, the VOL has a 'start point' on the graph to initiate the root monolith config and module installation.

As the VOL primarily executes within a ready environment, and the memory method is a flat graph, ensuring we initiate the correct memory address is a case of _locking_ a graph ID.

Some ID's within the graph are read-only, reserved for internal operations.


## Output Streams

The core monolith is _headless_, maintaining no output method aside from the REPL debugger stream and any fundamental display drivers for text printing.

The monolith root output stream maintains a literal connection to the client in the form of byte read write. "Commands" execute within the monolith given core drivers, such as "terminate command response" and graph stepping tools.

The REPL debugger output provides the readout for the attached device, and may push additional data through the concurrent stream response, such as debug output regarding the input stream.


### Container

The built-in output stream presents the REPL response, Exceptions, and disassembler info. The first phase container maintains an explicit driver dedicated to the debug port and container renderer including:

+ The core text renderer (stdout)
+ The Debug printing
+ REPL output responses from input (throug stdout)
+ Additional command/response for graphics (graphics docs)

For the 1.0 debugger output, a container should connect to the VOL Core, provide cornerstone settings:

1. A Text repl
2. an input panel
3. Graph render
4. Register view
5. disassembler loads.
6. "top" info.
