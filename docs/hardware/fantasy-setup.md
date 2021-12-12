For a  VOL core, the "synthetic architecture" groups all units under one asset
controller (the core) and its sibling kernels. CPU's are parallel and multicore, connected through their own bus, and the master message bus.

As an example, a central core of 1Ghz 2core drives the initial protected kernel, its drivers and bus protocols. The multicore steps and drives one CPU and as sibling to the core (near protected).

Other CPUs attach through direct lines and/or the message pipes - of which all CPU's connect - through a network mesh. The protocol is unimportant, noting that it'll likely be a pipes (or sockets) method - and local CPUs gain shared memory and locks.

Other CPU's may be of lesser power or alternative archecture, such as a 2040 crystal ossolator for realtime events, coupled with a 140htz micro cpu for sleep event management. All group within the core manager, communicating through a built-in "pipes".

All CPU's may be connected to others, in a star-like connection. Messages are piped by graph understanding, calculated on a main or _complex_ core.
