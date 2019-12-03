"""all fs installations maintain a base configuration on the system
If one does not exist a new instance is instantiated.

Consider this like the MBR of the FS, requiring some base configuration before
working. Fundamentally like a keystore for a file key place. At highlevel this
is implemented as a db - as low-level this is a fuse exposed api to a base
registry communicating to a higher level abstraction for cross cpu communication.

The local system defines a base of applications and a memory base recording all
references.
"""
import os
import sqlite3
from log import log


HEADER_DB_NAME = 'db.sqlite3'


def get_or_create():
    """Return the local header instance.
    """
    if os.path.exists(HEADER_DB_NAME) is False:
        create(HEADER_DB_NAME)

    return sqlite3.connect(HEADER_DB_NAME)


def create(name):
    """Create a new header dabatabase
    """
    conn = sqlite3.connect(name)


def grain(name):
    """Resolve the grain from the local reference - return raw grain data
    """
    _type = 'grain'
    pointer = get_local()
    # HeaderReference
    pointer.get(_type, name)
    return pointer


def get_local():
    """Called (anonymously) by the API to return a reference for file
    calls and pointers.
    If a local does not exist a new instance is instansiated and applied to
    memory. Depending upon configuration this may be live or lazy.
    """
    conn = get_or_create()
    return HeaderReference(conn)


class HeaderReference(object):
    """Abstraction of the local header db reference. use for pointer
    collection and calls. This is meta data about the actual content; stored
    with a particle on a service somewhere
    """
    def __init__(self, connection):
        self.connection = connection
        self.valid = None

    def cursor(self):
        return self.connection.cursor()

    def prime_fetch(self, reference, name):
        ek = f'SELECT * FROM local_{reference} WHERE name="{name}"'
        return self.execute(ek)

    def execute(self, ek):
        log.info(f'prime_fetch {ek}')
        c = self.cursor()
        try:
            c.execute(ek)
            self.valid = True
        except sqlite3.OperationalError as e:
            log.error(f'!! HeaderReference::prime_fetch execute fail: "{e}"')
            log.error(f"Statement: {ek}")
            self.valid = False
        return c

    def add(self, reference, name, value):
        """Add a file entry to the local reference with the given name -
        The content for the record is """
        ek = f'INSERT INTO local_{reference} (name, content) VALUES ("{name}", "{value}")'
        log.info(f'Perform insert {ek}')
        c = self.execute(ek)
        self.connection.commit()
        return True


    def get(self, reference, name):
        """Call the value from the database 'reference' using the name
        as a unique key.
        """
        iterator = self.prime_fetch(reference, name)
        return iterator
