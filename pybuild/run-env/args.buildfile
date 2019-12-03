ARG apples foo
ARG ls_com ls -lah
# green color
ARG ${apples} color
# ADD a key value, or apply a filename.
SETTINGS ./${apples}.json
INCLUDE ./otherbuild.buildfile
