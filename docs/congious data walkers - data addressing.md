# congious data walkers

This file addresses the challenges for congious data addresses, such as _bits_ in the RAM.

Our current classical method denotes congious bits, where we write a sequence of data to the memory (both disk and ram) for us to later read that information. Consider an WAV file where the information is aligned in order, or perhaps chunks of 4KB.

When reading this information back, we assign a pointer, and a memory allocation - an expected width of information to yield from disk.

In this state it allows us to _read_ "bits" from the data store and start reading them. The memory allocation (albeit manual such as C strings, or _automatic_ such as a javascript string) is set to match the data size.

In early computing this was the best foot forward; All memory or _RAM_ was accessible. You could "peek", "write" (and still can in some scenarios) any bits in memory. In todays computing this is highly unwanted. And we have a range of protections to ensure an _apps memory_,  _resources_, and _actions_ are enclosed.

We protect ourselves through a range of protection _rings_, user permissioning, app sandboxings, all the way down to _Memory_ or _buffer_ overflows. In all states, there is a gaurd and sentry, maintaining walls around executing source. These barriers protect us from unwanted actions albeit accidental or neferious in nature.

---

These required walls are built in response to concurrent and everchanging technological advancements. For good reason, we've compounded layers of security on-top-off functioning domains. We had a _computer_ and quickly needed more than one person to use one machine. We had 16 bit machinery and upgraded to 32bit. We quickly outgrew Global Descriptor Tables, and now they are a quiet footnote inthe POST of a _BIOS_.

When we press the _on_ switch, we boot into circa ~1970's. It quickly tests itself, pops a quick beep of delight and POSTs straight past the early 80's. We wait for a moment as the mid 80's are tested and mounted, pushing quickly into the early 90's.
I remember the excitment as a child, Watching 16bits of loading screen for a moment, followed by a glowing slow breath of the mid 90's.

We're not done. Gone are the days of the metronic cricket, vibrating its thoughts into life. Or the deep bussing purr of the hard-drive. Mounting serial ports, Printer Ports, and fancy credit card slot drive things winking their welcome blinks. We zip into the early teens where floats can count atoms, and _true color_ debands the once flickering glow of chunky VDU's.

---

In todays machinery RAM  allocation is so large it needs RAM. Disks sector counts need sectors of addresses, Perhipheral counts need subnets, and we're running out of IP addresses.

It's insane.

> That was also a lot for an introduction into congious data walkers!


## Back to the start - congious data walkers

This file addresses the challenges for congious data addresses, such as _bits_ in the RAM.

Our current classical method denotes congious bits. But that's old news. Let's skip ahead past 2020 where RAM and "disk" are fast and big and cheap and potentially remote.

...
