class BIOS_TAPE:
    """Read a tape an execute functionality"""

    def __init__(self):
        """In an expected env:
            0  readable
        """
        self.uuid_radix_name = 'bb4b7146-d16f-4c06-8a95-871e8b5d5ae6'
        print('testing path with')
        _os = os
        print('OS', _os)
        _path = os.path
        print('path', _path)
        _exists = os.path.exists
        print('exists', _exists)
        print('uuid', self.uuid_radix_name)
        try:

            pr = _exists(self.uuid_radix_name)
            print('Function: {}'.format(pr))
        except Exception as e:
            print('An error {}'.format(e))
            pr = False
        print('New Tape')

        if pr is False:

            print('No Root Tape in fileno:', self.uuid_radix_name)
            self.new_tape()
            time.sleep(.3)

        print('Complete existence of', self.uuid_radix_name)

        root_tape, fileno = self.init_tape()

        if root_tape is False:
            puts('Created new tape')
            root_tape, fileno = self.init_tape()
            puts('New tape', root_tape, fileno)

        if root_tape is False:
            puts('!! No BIOS Tape.')

        self.tape_data = self.read_tape(fileno)

    def init_tape(self):
        """Open the existing tape if available, returning (boolean, fileno)"""
        print( 'ATTEMPT BIOS_TAPE', self.uuid_radix_name, 'with 32914')
        fileno = self.open(self.uuid_radix_name, 32914)
        print('TAPE fileno', fileno)
        # return if BIOS Tape file exists at the gven location,
        # this should load for instructions
        return fileno != TAPE_MISSING, fileno

    def open(self, tape_id, access_id):
        """Open a file descriptor to the HOST RAM given a tape_id to
        assist compilation of the data asset
        """

        # Open bios tape at current source location (ugly.)
        # and read the input strategy.
        try:
            puts('Opening', tape_id, 'with access', access_id)
            bios_tape_stream = os.open(tape_id, access_id)
            return bios_tape_stream
        except FileNotFoundError:
            puts('Tape missing')
            return TAPE_MISSING
        except Exception as e:
            puts('!! Catastrophic failure with bios tape', str(e))
            return TAPE_MISSING

    def new_tape(self):
        """Produce a new BIOD RAM tape using the given ID. The mandatory BIOS
        inatructions are measured and set. A new tape is saved.

        Return the tape fileno

        This is a byte array for file access loadout"""
        puts('Creating new bios tape with 34193')
        try:
            vv = os.O_RDWR|os.O_RANDOM|os.O_BINARY|os.O_CREAT

            fileno = os.open(self.uuid_radix_name, vv)# mode='wb')
        except Exception as e:
            puts('Error with open', str(e))
            fileno = -2

        if fileno < 1:
            return False

        if os.path.exists(self.uuid_radix_name) is False:
            puts(BEEP + 'ERROR: Cannot produce BIOS Tape.')
            # sys.exit(1)

        puts('New Tape', fileno)
        self.write_new_tape(fileno)
        os.close(fileno)

    def read_tape(self, fileno):
        """Read in a bios tape and configure"""

        os.lseek(fileno, 0, 0)
        # Read as much as needed to capture the first
        # word within the string.
        first = os.read(fileno, 10)

        if len(first) == 0:
            puts('Corrupt tape. Delete => Renew')
            self.write_new_tape(fileno)
            time.sleep(.2)
            os.lseek(fileno, 0, 0)
            first = os.read(fileno, 10)

        puts('Inspecting:', first)
        size = ()
        for byte in first:
            # Capture first space
            if byte == 32:
                break
            size += (byte,)
        # string to int of bytes for the next cut
        puts('Reading tape size', size, 'of', first)
        incoming_bytes_len = int(bytes(size))
        puts('Bytes', incoming_bytes_len)

        os.lseek(fileno, 0, 0)
        bios_stamp = os.read(fileno, incoming_bytes_len)
        # remove the size header and [space]
        bios_stamp = bios_stamp[len(size) + 1:]
        result = {}

        # First byte
        result['wake_state'] = int(bytes([bios_stamp[0]]))
        # second byte.
        result['output_fd'] = int(bytes([bios_stamp[1]]))
        # 16 bytes for id
        result['uuid'] = bytes(bios_stamp[2:18])
        # Anything else is the version string
        result['version'] = bios_stamp[20:].decode('utf')

        #puts('bios_stamp:', bios_stamp)
        puts('wake_state:', result['wake_state'])
        puts('output_fd: ', result['output_fd'])
        puts('uuid:      ', result['uuid'])
        puts('version:   ', result['version'])

        result['lib_names'] = self.get_lib(fileno, incoming_bytes_len)
        puts('importing: ', result['lib_names'])
        return result

    def get_lib(self, fileno, init_byte):
        os.lseek(fileno, init_byte, 0)
        first = os.read(fileno, 10)

        size = ()
        for byte in first:
            # Capture first space
            if byte == 32:
                break
            size += (byte,)
        # string to int of bytes for the next cut
        incoming_bytes_len = int(bytes(size))

        os.lseek(fileno, init_byte + 1 + len(size), 0)
        lib_bytes = os.read(fileno, incoming_bytes_len)
        lib_splits = lib_bytes.decode('utf')
        return lib_splits.split('|')

    def write_new_tape(self, fileno):
        """write a new tape into the given tape fileno."""

        puts('Writing new tape')
        write = os.write
        lines = ()
        # vol phase state.
        lines += (b'0', )
        # Address pointer of the the ram file.
        # Booting in the same env this should be the same every time.
        lines += (bytes(str(fileno), 'utf'), )
        # 16 byte given uuid of the BIOS - templated in.
        lines += (b'\xbbKqF\xd1oL\x06\x8a\x95\x87\x1e\x8b]Z\xe6', )
        # selected kernel
        kernel_version = b"Kerbechet-(0, 0, 1)"
        # The amount of bytes for a pointer when reading the kernel string.
        lines += (bytes(str(len(kernel_version)), 'utf'), )
        lines += (kernel_version, )

        # write in STDOUT fileno
        total = sum(map(len, lines))
        len_total = len(bytes(str(total), 'utf'))
        total += len_total + 1
        os.write(fileno,  bytes("{} ".format( str(total)), 'utf') )

        # os.write(b'\x00')
        for bv in lines:
            os.write(fileno, bv)

        os.lseek(fileno, 0, 0)
        read_t = int(os.read(fileno, 2))
        assert total == read_t

        # Write a version string
        os.lseek(fileno, total - len(kernel_version), 0)
        read_kernel = os.read(fileno, len(kernel_version))
        assert read_kernel == kernel_version

        puts('Writing libs')
        os.lseek(fileno, total, 0)
        libline = bytes("|".join(list(('bios_os',))), 'utf')
        #os.write(fileno, bytes(str(len(libline)), 'utf'))
        os.write(fileno,  bytes("{} ".format( len(libline)), 'utf') )
        os.write(fileno, libline)
        puts('Complete')


class Tape(BIOS_TAPE):
    pass

