"""
The general file io
"""
import fs
from log import log
from measure import Size

REFERENCE = 'pointername'
expected = 'there is no spoon but there is an apple and some eggs.'

def main():
    """A Simple put and get appliance. Initially apply the REFERENCE with the
    'expected' data to the FS, the read back (returning as a colloid of particles)
    """
    put()
    throughput()


def put():
    """A Standard put or store example - applying content though the 'aggoleramte'
    """
    log.info(f'Put {REFERENCE}')
    fs.agglomerate(REFERENCE, expected)


def throughput():
    # Read a string through the IO.

    value = fs.colloid(REFERENCE)
    if value != expected:
        log.error('fs.colloid did not return the expected value')
        log.info(f'expected    {expected}')
        log.warn(f'value    {value}')
    else:
        log.info(f'fs.colloid successfully returned {value}')


if __name__ == '__main__':
    main()
