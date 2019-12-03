"""Base point for the filesystem
"""
import local
from log import log
import zlib
from pyhashxx import Hashxx
from pyhashxx import hashxx
from particle import ByteParticle, Particles

def agglomerate(name, value):
    """Apply the given value to the fs with the name.
    The incoming data is anonymous therefore the relative pointer is
    pulled from the user space.

    Essentially it's a store procedure like filename, however the store point
    is magically captured.

        fs.agglomerate('thing.name', 'some content to record; new or appended.')

    The agglomerate procedure will find the best location to store 'name',
    write the value, and add the store record to the local header.
    """
    print('agglomerate', name)
    pointer, space = _locate(name)
    content_result = _write(space, value)
    return_result = _record(pointer, space, content_result)
    # return meta.
    log.info("return meta.")
    return return_result


def _locate(name):
    """Given a store name, determine the best location to apply the incoming
    particle of content.
    Return local pointer and remote space.

    Fetch the local filesystem pointer and analyse for the best space.
    return a pointer and space used for the next write and record.
    """
    fs = get_fs()
    # Reference all managed user spaces, for a check across all services
    # through the membrane.
    # The space understands the user session, membrane connection,
    # and other properties to yield a successful push-down.
    space = fs.space(name)
    # get or write space
    #   Fetching the local
    #   performing a record append
    #   allocate write spaces
    #   View services and assert a best place

    # fetch the local primed pointer; the header space storing the record.
    log.info("get space")
    pointer = local.get_local()
    return pointer, space


def _write(space, value):
    """Given a prime space location, write the value and return a result entity.
    """
    # Add the new value in the correct location
    # give the store ID to the pointer add

    # It's a particle of content here, applied to the (given) pointer store location
    # to create or append the value content.

    # Get the future store location inspecting the pointer and space.
    # returns an entity for recording the name.
    log.info(f'Write "{value}" to space "{space}"')
    space.write(value)
    return space.get_id()


def _record(pointer, space, result):
    """Record the record action performed with the write function in the local
    refernence header.
    """
    # Store a local record of content location for the particle name.
    log.info(f'Recording to local as particle to pointer: {pointer}')
    pointer.add('particle', space, result)
    return True


def colloid(name):
    """return all the particles within a colloid

    A Colloid represents a 'read' like function to collect and resolve particles
    through an association of names or space. A Colloid refers to one or more
    paritcles. When Applying a colloid, you create one or more paricles associated
    by a grain. The colloid will fetch the particles under the grain."""
    # get a pointer
    # read the headers
    # return the particle colloid

    """The return the most relevant pointer
    for the user and their assets."""
    fs = get_fs()
    """Resolve the named header address, containing all references
    to the content; particles."""
    grain = fs.grain(name)
    """Fetch a list of particles for the grain. In a smaller request, this
    list is small. With larger sets (an aggregate) the particles will not
    constitute a complete aggregate (file)"""
    particles = grain.particles()

    """Actuate the build strategy of the content, returning a complete
    data source. As this _completes_ the entire fs chain and loads into memory,
    it should only occur for smaller colloids. Alternatively a lazy reader.
    """
    return particles.resolve()


# A Store of named pointers.
POINTERS = {}

def get_fs():
    """Return the most relevant file pointer. If one does not exist a new pointer
    is created.
    The pointer is relative to a users requirements. the returned fs provides
    access to grains and particles for aggregate resolution.

    A Pointer identifies the vfs loader and its authentication. By default a
    memory pointer should exist for a system defined by an initial load-out.

    A pointer may birth from a new system or thread.
    """

    # return the 'current' (zeroth) file system or generate a new one.
    return POINTERS.get(0, FS())


class Space(object):
    """A space bind a working read write location for the user, given through
    a series of checks for the best location.
    """

    def __init__(self, **config):
        """Config includes:
            name
        """
        self.config = config
        self._write_id = -1

    def __str__(self):
        return f'Space({id(self)})::{self.config["name"]}'

    def write(self, value):
        """Put the content of the file into the store location.
        return the expected state.
        """
        ParticleClass = ByteParticle
        log.log(55, f'writing {len(value)} bytes using {ParticleClass}')
        # write bytes to file, return write location.
        ptl = ParticleClass(
            # The current owner
            reference=id(self),
            # The value content stored has no reference to name,
            # but may use it during particle invention.
            name=self.config['name'],
            )

        with ptl:
            ptl.write(value)

        # open file, put content
        # get address (for later resolve)
        return True

    def get_id(self):
        """Return the ID of the last write or current writing.
        """
        return self._write_id


class Permissions(object):
    """A working space to the FS to brige local user permissions
    to the working FS through anonymous calls.
    """
    pass


class FS(object):
    """A class for connecting to and working with the internal filesystem.
    """

    def __init__(self):
        # Announce.
        log.info('NEW FS')

    def space(self, name):
        """Instigate a space for the user to apply particle content. This should
        factor the user, sessiom, thread - essentially everything to facilitate
        a write to the particle chain.

        The next call to the return entity is likely a 'write'. Consider:

        + user session
        + system variables
        + membrane
        + permissions
        + thread
        + remoteness (HOST?)
        """

        log.info('Discover user space')
        space = Space(name=name)
        """
        The space discovery is offset to the main machine, into the kernel to
        reference allowed spaces. If the user session space bridge is not defined
        a new one should be generated - assuming such events as NEW system or WAKE
        a session for example.
        """
        # get user session
        # Check secret asset location for any previous caches
        # check permissions for access
        # through system globals to access the membrane
        # Communicate across the membrane for valid services
        # check threads and remotes for viable locations
        # select the best space through magic inspection of spaces and name.
        # return a space writer; a manager for file passing.
        return space

    def grain(self, name):
        """Return a particle grain reference unit
        """
        log.info('FS::grain')
        return Grain(name, owner=id(self))


class Grain(object):
    """A grain presents particles of content to an aggregate or raw reader.
    Identify a grain with a name, the reference information (pointers) resolve
    locations and other meta.

    The grain maintains connection abilities and host information for successful
    particle data.
    Although a particle may be fetched, it may be unreadable without the
    grain pointer reference.

    + store locations
    + meta data Access abilities
    + read headers
    + maintain connection with the Header store
    + held my an aggregate

    """

    def __init__(self, identifier=None, owner=None):
        # announce
        self.identifier = identifier
        self.owner = owner

    def info(self):
        """Return the information of the grain from the header
        """
        return local.grain(self.identifier)

    def particles(self):
        """Return all collective endpoints for the grain.
        """
        return Particles(self)
