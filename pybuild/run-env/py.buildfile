# Manage a python environment - created in the target directory.


ENV pyenv
PIP smpq flask
PIP INSTALL flask
PIP REMOVE smpq


EXEC print('Python callout using Arg "apples": ${apples}')
EXEC myfunc(session)
