""""The System module defines the runtime header for the entire VOL for all
calling methods. Replacing any produced global header references during the BIOD
boot, all calls propograte through the system

The System is directly responsible for leveraging the BIOD boot config and
runtime params; consider the memory allocation and process the zero layer
importables and permissions.
"""

class System:
    def __init__(self, original):
        self._original = original

    def __getattr__(self, key):
        return key

    def __getitem__(self, key):
        if key == 'foo':
            return self._original
        return "< %s" % key

    def foo(self):
        return 'bar'


def configure(bios, scope):
    keys = tuple(scope().keys())
    print(keys)
    for key in keys:
        print('Deleting', key)
        if key == '__builtins__':
            scope()[key] = System(scope()[key])
            continue
        del scope()[key]
