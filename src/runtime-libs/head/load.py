
def load(bios, scope, head, system):
    bios.puts("Load scope_callable into head")
    bios.puts(scope, ROOT)

    for name in ROOT:
        try:
            if name.startswith('__'):
                bios.puts('Skipping', name)
                continue
            v = getattr(scope, name)
            setattr(head, name, v)
            bios.puts("Set", v, "to", name, level=2)
        except TypeError:
            bios.puts('Will not import', name)
    bios.puts('Load complete')
    global IMPORT
    IMPORT = scope.__import__
    scope.system = system
    return head


def monty(count=0):
    return 'Cake {}'.format(count)


def __import__(name, _globals=None, _locals=None, fromlist=(), level=0):
    print("BIOS LOAD", name)
    if name in SECONDARY:
        print('Load SECONDARY function')
        return None
    return IMPORT(name, _globals, _locals, fromlist, level)


