# Tape

> Previously undocumented but built as a PoC -  _data tape_ acts as a string of graph keys to process in a linear walk. The root system should have a written tape.

A Tape acts as a keygraph list for _persistent_ routines - such as booting the system. The tape dictates the route of the walk when the loop executes the graph pointers. Without a tape the walker will blindly step to the next best key (albeit nominated by the pointer or defines within the graph index).

> Read Phase-0.md for more.


fundamentally the VOL needs a root tape, to actuate any phase-0 steps, else the key graph may not understand a magic key - given the root nodes of a graph are protected.

