import os
import manifest

class Extends:
    """A structure of methods for key replacement streategies

    when replacing a settings key, the functionality for override may
    be goverened over the default replace key.
    """
    def REPLACE(self, a, b):
        return b

    def APPEND(self, a, b):
        a.append(b)
        return b

    def SET(self, a, b):
        sa = set(a)
        sr =sa.union(set(b))
        return tuple(sr)


UNITS = (
    'host.asset_loader',
)

EX = Extends()
KEYS = [
    ('name', EX.REPLACE,),
    ('keys', EX.APPEND,),
    ('units', EX.SET,),
]

def key_map(config):
    gl = globals()
    res = {}
    kk = KEYS
    print('Type', type(kk), len(kk), kk)
    for index, x in enumerate(kk):
        # print('Type', type(kk), len(kk), kk)
        # print('keys item', index, x)
        name, method = x
        glv = gl.get(name.upper())
        val = config.get(name)
        if val:
            res[name] = method(glv, val,)
    return res


def resolve(home):
    man_file = manifest.load(os.path.join(home, 'HOST'))
    km = key_map(man_file)

    return MANIFEST_WRAPPER(km)


class MANIFEST_WRAPPER(object):

    def __init__(self, d):
        self.__dict__.update(d)

    def __repr__(self):
        return repr(self.__dict__)
