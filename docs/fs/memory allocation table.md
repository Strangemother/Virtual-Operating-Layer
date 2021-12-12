memory allocation table

A Particle refers to a tiny chunk of sequential data (bytes) held in a memory location such as ram, disk or other abstract stores.

The size is arbitrary but may be allocated and _locked_ for runtime usage. Many particles produce a Grain. Many Grains produce an Aggregate. Most high level functionality will utilise a coalesced aggregate.

At its base each Particle may size of any _width_ and subject to the restrictions of the stroage medium. Therefore will populating the particle with bytes a limitation will force the stream continuation to another particle (of the same width). We can call this

A particle may have a start and end pointer as an arbitrary width. The particle information will spill into consequtive particles until all data is digested as a tabular like reference. As an example of a storage location of 100Kb, we'd need up to 100k adressess or `0..0xFFFFF`. Each address has a sibling address.
