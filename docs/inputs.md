# Inputs

One of the features for VOL is agnostic awareness of HID or other input mouted devices.
VOL Shares connected resources aross the mesh without distinction and drives the IO of the device from any NODE.

An input may exist as a HOST driver object, the CORE Motherboard devices, GPIO, etc... Essentially any NODE in a VOL mesh.
Mounting an input can occur through a CONTAINER, Directly from a RUNTIME as a NODE or from the CORE itself.

A NODE may be designed to work as a computational leaf, therefore doesn't have any driver inputs.
It could be a simple CONTAINER (or some other VDU)

## Container

A CONTAINER maintains a _portal_ to view the VOL. Consider it like a desktop. In its raw form it can be thought-of as a website
reading all the settings from one CORE, but also helping as a NODE with visual decoding and presenting.

Inputs may flow through the container into the connected NODE and into the mesh. This could be finger presses or a webcam stream.
As the visual output is a flow of events from one or more RUNTIMEs on the mesh. A translator will work input (and output) data from the connected RUNTIME
into the correct format for the connected CONTAINER.


**Use Case**

As an example we have a linux CORE with a RUNTIME on a network running a waiting MESH.
Another NODE SOC (such as RASPI) has no container, but has a TRANSLATOR converting text to LED as morse-code flashes.
On a Windows system another RUNTIME and CONTAINER is connected to the waiting MESH through a previous SSH Key pairing.
The CONTAINER RUNTIME has an open-gl TRANSLATOR to simply _print_ keypressess to the CONTAINER view.
The RUNTIME on the windows system is pre-configured as a open-GL CONTAINER with keyboard and mouse inputs.
Once the new Windows CONTAINER is ready, the CORE will redirect all drawing events to the CONTAINER.
A user presses a key on the Windows system (within the container). This is sent as a MESH event
Hearing a keypress the CONTAINER will render the event. It may not rely on the network event as the event manifested in the local RUNTIME
The NODE will also hear the keypress event and will flash accordingly.

