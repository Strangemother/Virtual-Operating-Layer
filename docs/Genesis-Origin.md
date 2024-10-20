# Origin Space (Genesis)

Each VOL system initiates from an origin, a foundational starting point. Notably, origins such as the Genesis are initially devoid of functionalities.

In many cases we must install functionality, such as a `radicle` to perform executions.

['__annotations__', '__builtins__', '__doc__', '__loader__', '__main__', '__name__', '__package__', '__spec__']

They're mostly blank in an empty origin space.

    ..: __name__
      : 'ORIGIN'

We can install a `radicle` to seed a new space:

    ..: import radicle
    SystemRoot::gain_Import: radicle
    ... new radicle
    radicle()

Some builtins will change:

    ..: __name__
      : '__radicle__'