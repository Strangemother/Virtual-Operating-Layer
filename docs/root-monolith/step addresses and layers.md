

Every "frame" has an address; used for ID and security. This is assigned to the executing chunk (or other assigned graph unit) by the event loop position - from the VOL core.

Given the application initiates at #0, and must step to #1. The first running function would allocate a position within #1. This executes two framed statemements.

    #0 -> #1 - #2
             - #3
             -> #4
                  ...

The application #3 receives a graph id `0/1/3`.
