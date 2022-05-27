# Space

+ _concept_

When a user fetches to appends to the file system, an initial call to initiate a space
evokes services to process data. A 'space' defines a single entity or resource to
use as a store location, containing the required parameters to enact the service and
its storage procotol. For example a service may by FTP or S3 for a 'space'
configuration to apply egress protocols. Once a user has integrated the chosen service
they may access service procotols through the space configuration.

A space and its configuration exist _below_ the user session, optionally as the
core filesystem. Therefore the connection to a service should be seemless.

A range of default spaces exist of the user and the base system. They include
local file storage (standard bits and bytes), network storage and FTP etc -
generally _easy-to-load_ standards. After an initial configuration the chosen
services should naturally on-board or _grow_ as the FS expands. Additional hardware
will _spread_ a user session to a larger space, by leveraging additional storage
locations automatically.

The end-result will provide a single persistent layer of ambient storage devices,
connected through a membrane and actions via space configurations. Each space unit
exists independently and selected through general rules and magic.

Instigate a space for the user to apply particle content. This should
factor the user, sessiom, thread - essentially everything to facilitate
a write to the particle chain.

The next call to the return entity is likely a 'write'. Consider:

+ user session
+ system variables
+ membrane
+ permissions
+ thread
+ remoteness (HOST?)

result = {}
print('Discover user space')


The space discovery is offset to the main machine, into the kernel to
reference allowed spaces. If the user session space bridge is not defined
a new one should be generated - assuming such events as NEW system or WAKE
a session for example.


+ get user session
+ Check secret asset location for any previous caches
+ check permissions for access
+ through system globals to access the membrane
+ Communicate across the membrane for valid services
+ check threads and remotes for viable locations
+ select the best space through magic inspection of spaces and name.
+ return a space writer; a manager for file passing.
