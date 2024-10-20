# Radicle

> Before the virtual operating layer can operate it needs a base or root runtime to instansiate system units and prepare the space for work. The `radicle` is a the root or _most core_ unit to run in a vol runtime.

The "Radicle" module acts as the first unit to instantiate a VOL instance.
Upon first load the v1.0 opens a runtime, complete with these components baked
into the core; The initial code builds a cell to become a VOL.

Functionally nothing exists before `radicle()`, attempting to use any functions
will bubble an error:

    ..: print
    ! NameError "name 'print' is not defined"
    ..: echo
    ! NameError "name 'echo' is not defined"

    ..: radicle
    ! NameError "name 'radicle' is not defined"

We can see from the core dunder, only the import exists:

    ..: __builtins__
      : {'__import__': <function import_installer at 0x0000000001D49C10>, '__loader_
    _': None}

To run, import and execute the `radicle()`

    import radicle
    radicle()
    print('Print function installed by the radicle:', radicle)

At this point the base functions are avaiable.


['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__', 'b', 'radicle']