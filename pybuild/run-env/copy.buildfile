# Copy a file to 'dest/foo.json'
COPY ../pybuild/foo.json
# copy a file into another destination
COPY ../pybuild/foo.json apples/otherfoo.json
# Copy this folder to 'dest/foo.json'
COPY ../pybuild/ /other/
# Copy buildfile dir content to dest
COPY . .
COPY ta tb tc td desta
#copy a backref targets,
# and anything in buildfile dir
# and anything in v1 examples to dest root
COPY ../pybuild/ . ../../v1/examples .
