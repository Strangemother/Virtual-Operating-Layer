# Masters and Nodes

Naturally The VOL wants to tandem its work across 2 or more platforms. Ideally the CORE ran independently to the CONTAINER but in some cases running a CORE linux setup isn't possible.
Alternative options may be recompiling the CORE with a new kernel (such as windows) or starting the RUNTIME outside a CORE and implementing as a NODE.


# Master

The term isn't used much throughput a VOL or the documentation as it doesn't really exist. The project intention defines complete distribution with natural failsafe and sharding.
However running a single CORE with one RUNTIME and you have a single computer. Coupled with a range of CONTAINERs and other NODE inputs, the CORE may be referenced as a Master to contextual simplicity.


# Node

Simply put a node is one RUNTIME without a CONTAINER or some other direct view. It exists as a computational unit for the VOL and may define a specific task such as UART device monitoring or data backups across a network.

When starting a RUNTIME it may mesh into an existing VOL with an existing SESSION and its own RUNTIME. A Node may send display information for _a_ CONTAINER to capture.
VOL will capture the any new nodes and integrate them to the MESH as a role governed by the capabilities of the new RUNTIME.

In an example case the new NODE may be a Windows machine with an active CONTAINER. The linux based CORE will capture the capabilities and start the relevant translator. As such the newly formed mesh consists of a Linux CORE, a Windows RUNTIME and CONTAINER - managed by a SESSION shared across the CORE and RUNTIME. The CORE maintains the working core such as session apps and data persistence

