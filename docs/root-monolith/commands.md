# Base commands

`echo` renders directly to the stdio lib "out" write.
`print` render to the view - preprocessing each var into the printable representation and apply a `\n` at the end.


## Standard pipes

### stdin

`stdin.readline()` accept UTF-8 formatted text terminated by `\n` (or `Enter` key during terminal wait). return into a frame variable for post processing

    ..: input = stdin.readline()
    ..: input

`stdin.read()` accepts a bytes stream including newline characters until `^Z` (CTRL-Z), terminates the receiver pipe and yields the result into the frame.


### stdout

The pipe for the standard out, used by `echo` and includes the `stdout.write()` function.
