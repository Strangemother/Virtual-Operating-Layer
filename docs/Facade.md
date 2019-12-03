# System Functional Facades

+ For remapping the under lying C and python functions into a VOL specific location
+ Produce the assignments through contexual objects for natural mesh resoltion

## Runtime

At runtime exposure and production, functions from the 'core' imports exist
as overflow from C, ASM and Python functions. Relocate these functions early
with a facade. When accessing the functionality of the facade, any logical
steps required aren't seen by the API.
The simplest example would be a C 'put' string function.

    Function:
        put

    Expose:
        bios.puts

    Result:
        callable function



## Files API

In the standard APP, File (FS) or walking Terminal scenarios, the Facade acts as
a pointer through VOL logical steps.

    Function:
        data.ftp.home.foo.bar.baz.[test.txt]

    Expose:

        data: ROOT
            ftp[name=home]
            dir=foo.bar.baz
            file=test.txt

    Result:
        File Handler


## Mesh State API

A vol persists a State system across a mesh within a pre-authorised network.
Using the mesh state [object] perpetuates the change across the network.
Other mesh states will act accordingly.

This interface may be handled through a facade. Each functional call can communicate
a local change to a remote object.
