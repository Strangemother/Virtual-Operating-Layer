# Scaling

Scaling overlays Visual, Distribution and Hardware.

## Visual

Generally talking about screen size, the visual scaling should cater for a large range of interfaces and sizes
Starting at 1x1 inch for IOT displays up to the standard 1080p and 4K resolutions.

Overally the 'framebuffer' amd 'container' output translators manage standard displays as they VDU
manages graphics. In addition Containers can utilize GPU in a client.

Smaller units and custom displays (eink) have their own API to bridge.

As an alternative setup for HOST display, a more-powerful system can run one or more VOL and CONTAINERS.
Desktop machinery can run mutilply CONTAINERs for each display.

## Hardware

As VOL manifests as the CORE machine, a runtime with REPL and a VDU the hardware can scale independently to the _running suite_ the runtime and session.
Using a CORE of custom linux the hardware platform i only limited by build targets and will CPU scale accorindgly.

As the session-runtime and RUNTIME don't need the CORE = running as:

+ a distributed environment with the session runnning off the interating hardware
+ A RUNTIME running as an app (such as an exe) network connecting to a CORE


## Distribution

VOL is naturally distributed - meaning it is designed at the CORE and RUNTIME to work within more than one consistent platform.
The main CORE linux image is small with the VOL machinery mataining the entire system.
A visual connection may be XDISPLAY or Framebuffer but a better choice is the CONTAINER running on isolated from the CORE.

Core utilities and applications are distributed to other CORE or NODE machinery. Each Leaf performs a unique task to communicate back
into the VOL mesh - collected by the master system.

As an alternative setup for HOST display, a more-powerful system can run one or more VOL and CONTAINERS.
Desktop machinery can run mutilply CONTAINERs for each display.


The CORE is a best place for the main system, allowing a complete take-over. But the RUNTIME may exist on the HOST and designed to connect
as a NODE for remote session work.
