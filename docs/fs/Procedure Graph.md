Procedure Graph

The "procedure graph" applies a linear ordered function set in a graph chain, consequently performing a "program" or application. every application exists as a key reference within a graph - namely the function name.

Initially this serves little function, other than a handy key reference. However futher abstracting this with a linear execution chain, An application may yield chain actions in parallell or linearly, through a combination of async execution and socket communication across all nodes within the a VOL ecosystem.

Later this is abstracted in to a VOL _AST_ like methodology, where routines are executed in a graph-like fashion and coded with application to utilise the "Graph nodes" lingistics.

1. A system has many functions
2. A user write linear instructions
3. The system accepts the text bytes and tokensizes to AST
4. Execution occur off the visual thread, communicating through sockets.

---

From the base we can introduce the base language construct, stepping from the turing complete _bios_ to the +1 layer - user space and local allocations. This layer initialises the "first run" routines such as an async event routine.

The fundamental application intiates a two step graph "A>B" and repeat. This is essentially a forever loop - without the loop. We then build AOP prodecures on top of the event loop, stacking vertically

Graph:

    #0: Step to #1
    #1: Step to #0


# Graph Layering (Security Rings)

The lower order graph nodes maintain a special place allowing or refusing protected procedures. If a function emits from #0/#0, The functions are in a protected mode with lesser drivers but a raised security level.

Consider this like "protected mode" in standard archiecture, where 16bit machinery and lower live within a protected security ring 0 to ensure higher level application. This is important within the Procedure graph, where the secure driven elements exist within frames without upper access

1. The system integration refers to at graph position #0
2. a user executes from a "Origin number" the existing graph origin

---

The user steps the graph manually - or flows through the nodes during each event phase, digesting the result for each step into a colloid.

    byte byte > Step > yield > byte byte > step > ...

As the user inputs bytes, the key is potentially tested and stepped. When the step occurs, the result is cached, digested, or immediately executed.
