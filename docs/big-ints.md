# Draft 1

Wrapping a large integer through multple CPUs, such that the total of all numbers (nX) is equal to the original input value. I feel 10^100 is enough but 10^303 (centillion) is the goal.

For now we'll focus on general 32/64 bit integers, with 5 (dual core) CPUs, minus 2 cores for overhead and bus. As such A raw parallel int may have roughly 10^256  (32bits * 8 cores) - more likely 224 bits, leaving room for an address thread (core #0.)

Each unit is broken into the bit graph, a distributes as N tasks (matching the CPU). Each core is responsible for one part of the number. Any computation is done on the _part_ and messaged to the bus.

