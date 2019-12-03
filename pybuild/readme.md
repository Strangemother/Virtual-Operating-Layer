Run simple procedural commands for using python - mostly for python
buildouts.

Supply a `buildfile` or `myfile.buildfile` or `.buildfile` to the builder script.
It will run all the commands, with inline templating, caching, downloading - etc...

+ Manage stages

Some commands for example:


## Settings

Set a key value or filename content as settings for the build.

    SETTINGS key value
    SETTINGS filename.json

## TARGET

Set the output directory for the procedural stages. If the `TARGET` is not defined, the default `build/` is used relative from the `CWD`.

    TARGET foldername


## PRINT

Echo inline the statements provided, resolving templates for internal settings.

    PRINT A simple phrase
    PRINT "class python print style for target:", TARGET
    PRINT ${TARGET}


## CWD

Set the current working directory. If undefined the default the currrent working directory is used.


    $ /user/me/myapp/> pybuild .
    # CWD is /user/me/myapp/


## CMD

Run a standard terminal command, executing inline and waiting for the result

    CMD ls -lah

## EXEC

run a python inline statement. Waiting on the result

    EXEC print(global().keys())
    EXEC os.path.basename(${TARGET})


## EXECUTE

Run a python file as inline statements, allowing an `EXEC` to more than a single expression. Provide a python filepath, or a python filepath and target function


    EXECUTE ./my/file.py
    EXECUTE /home/user/app/file.py:run_func

## INCLUDE

Include another `buildfile` for inline execution.


## COPY

Copy a file or folder from the given `target` directory to the `destination` directory.
If the `destination` is ommited, the `TARGET` is used.

    COPY TARGET [DEST]

Copy a content of the target directory to the root of the target direcory, relative from the current working directory.

    target:
        buildfile
        dir/
            file1.txt
            file2.txt


    COPY ./dir/

    destination:
        file1.txt
        file2.txt

This is the same as `COPY dir .`. If the `CWD` current working directory is not changed, it's the `buildfile` location directory.

Provide a second argument to copy the content of a directory to a directory within the destination

    COPY ./dir ./sub-dir

    destination:
        ./sub-dir/
            file1.txt
            file2.txt


Copy everything from the current working directory to the destination directory:

    COPY . .

Each `period` is a relative directory from the `CWD` and `TARGET` respectively. By design this will not copy the `buildfile`.
