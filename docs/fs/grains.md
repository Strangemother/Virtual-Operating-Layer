# Grains

A Grain maintains a header with references to many particles. The header is stored in a local graph for NAME asssociation with chunks. Pretty much a _file_ and its attributtes stored as a record.

The Header returns any local credentials to yield finished particles. The grain leverages the locally stored references and instaniates Particles. Each particle calls and resolves indepdentantly returning pointers to chunks.

> Although a Particle will work without a Grain, it may be unusable as the grain (and its header) keep a persistent graph of sibling to finalise an aggregate.

The Particle may exist on a seperate core, process or system - but within the user session. When ready it will return a waiting pointer given back the the main process (the grain).

At this point the grain holds many seeking pointers and will order iterate the particles for content. Each content stream is chunk seperated and distributed or aggregated into a final resource. The final resource will read the grain content.

