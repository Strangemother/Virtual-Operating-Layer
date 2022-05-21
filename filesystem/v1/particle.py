"""Base point for the filesystem
"""
import local
from log import log
import zlib
from pyhashxx import Hashxx
from pyhashxx import hashxx
import os


class Particles(object):
    """A manager to assist with particles.
    """

    def __init__(self, grain=None):
        # Announce.
        self.grain = grain
        log.info(f'NEW Particles {grain}')

    def reference_grain(self):
        """Return the references for all particles
        """
        header_info = self.grain.info()
        return header_info

    def resolve(self):
        """Return the content of the paticles, resolved and in order -
        ready for flat digestion.

        Essentially convert the pointers to real text and bytes.
        """
        log.info('Particles::resolve')
        refs = self.reference_grain()
        if refs.valid is False:
            log.warn('Failed refs.')
            return


class HashMixin(object):

    def crc(self, byte_string):
        return hex(zlib.crc32(byte_string) & 0xffffffff)

    def hash(self, byte_string, seed=0):
        hasher = Hashxx(seed=0) # seed is optional
        hasher.update(b'Hello')
        hasher.update(b' ')
        print(hasher.digest()) # Prints 1401757748
        hasher.update(b'World!')
        print(hasher.digest()) # Prints 198612872

    def hash_one(self, *a):
        a = hashxx(b'Hello World!')
        b = hashxx(b'Hello', b' ', b'World!')
        c = hashxx((b'Hello', b' ', b'World!'))
        d = hashxx((b'Hello', b' '), (b'World!',))
        # All return 198612872
        assert len(set([a,b,c,d])) == 1
        seed_changed = hashxx(b'Hello World!', seed=1)
        assert a != seed_changed



class Particle(HashMixin):
    """A particle handles its own content and reference to data structure
    fundamentally a particle returns content from its configured store or endpoint.

    A particle may access the bare-metal; therefore maintains it's own open/close
    for its internal pointer. The particle manager (owned by a grain) manages the
    pointer location and ordered reconstruction of many particles.

    This particle may have a sibilings to complete the internal data. the keys
    are referenced with the particle; accessible though a graph reference caller
    (or on the data).

    The Particle may be considered as in-memory, local bytes or even remote -
    such as FTP.
    """
    def __init__(self, reference, name=None, **kw):
        self.reference = reference
        self.name = name
        self.kw = kw

    def content():
        """Return the phyical information of this particle resovled and at
        seek point.
        """

    def local_header(self):
        """Return a local header definition from the HEADER reference if it
        exists. A byte particle may not have a _correct_ local reference if
        the particle was accessed through a space or membrane without references.

        This may occur and the particle or grain can announce this to potentially
        resolve elsewhere.
        """

    def write(self, byte_string, byte_chunk=None):
        """Given literal bytes string open or continue the particle
        """

        # n amount of bytes to step per reference chunk. Each unit is shuffled
        # through the write
        BYTE_CHUNK = byte_chunk or 16
        chunks = lambda c,s:[(i, s[c*i:c*i+c]) for i,x in enumerate(s[::c])]
        res = set()
        for index, byte_16 in chunks(BYTE_CHUNK, byte_string):
                res.add(self.write1(index, byte_16, BYTE_CHUNK))
        return res

    def write1(self, index, chunk, bytes_int):
        """Given a single chunk of a byte string, write to the particle
        content.
        The index defines the current position in the bytes enumeration.
        The chunk will be up bytes length up to bytes_int but may not
        be the length of bytes_int."""
        log.debug(f'Write({bytes_int}): "{chunk}"')

        return True

    def close(self):
        """Close references to the particle, shutting logs and writing
        references through the local header.
        """
        self.open = False

    def prime(self):
        """Access the asset as required in a pre-flight stage, the next incoming
        task is expected crud
        """
        self.open = True

    def __enter__(self):
        log.debug('- prime enter particle')
        self.prime()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('- close exit particle')
        self.close()

MEM = {}

class MemoryParticle(Particle):
    """A particle type accepting data to store in memory as binary, bytes or text
    stream. As this does not create persistent data the address may be transient
    (for the life of the particle) and should not be applied to a hash chain
    as this object will not pass.

    The fs may use a memory particle for fluid motion of particles when traversing
    to a persistent space. A particle may tranform to another particle type through
    natural usage; i.e Memory => Disk produces a byteparticle
    """


class ByteParticle(Particle):
    """A particle type accepting bytes. Like a File
    """
    def prime(self):
        """Open a write location ready for write, expecting the next incoming
        method write1
        """
        fn = self.name
        name = f"{self.reference}-{fn}"
        filename = os.path.join('scratch/store/', name)
        self.file = open(filename, 'w')
        return super().prime()

    def close(self):
        self.file.close()
        return super().close()

    def write1(self, index, chunk, bytes_int):
        log.debug(f'write1({index}): {len(chunk)} as size {bytes_int}')
        self.file.write(chunk)
        return True
