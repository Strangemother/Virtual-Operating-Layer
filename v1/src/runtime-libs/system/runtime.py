""""The System module defines the runtime header for the entire VOL for all
calling methods. Replacing any produced global header references during the BIOD
boot, all calls propograte through the system

The System is directly responsible for leveraging the BIOD boot config and
runtime params; consider the memory allocation and process the zero layer
importables and permissions.
"""


class MyImporter(object):

    def find_module(self, module_name, package_path):
        # Return a loader
        print('find_module', module_name)
        return self

    def load_module(self, module_name):
        # Return a module
        print('load_module', module_name)
        return self

import sys


def configure(head, bios, scope, safe_only_system_execute=False):

    keys = tuple(scope().keys())

    system = System()

    for key in keys:
        if key == '__builtins__':
            _builtins = scope()[key]
            new_builtins = head.load(bios, _builtins, head, system)
            system._builtins = _builtins
            setattr(_builtins, 'system', system)
            scope()[key] = new_builtins
            continue
        print('Deleting', key)
        del scope()[key]

    bios.execute_system(system, scope()['__builtins__'])

    print('Stepping into system clean')
    del scope()['__builtins__'].load
    # del scope()['__builtins__'].__import__

    # sys.meta_path.append(MyImporter())

