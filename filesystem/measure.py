# https://en.wikipedia.org/wiki/Orders_of_magnitude_(data)

def main():
    BytesSize().load_store()
    print(entries.items)

    sz = Size(10, 'mb')
    print("size", sz, sz.kilobyte)
    print( int(sz.kilobyte), 10000 )

class EntryHost(object):

    def __init__(self):
        self.items = []
        self.sizes = {}

    def add(self, entry, size):
        self.items.append(entry)
        self.sizes[size.name] = size

    def filter(self, key):
        res = ()
        for entry in self.items:
            if entry.match(key):
                res += (entry,)
        return res

    def get(self, key):
        m = self.filter(key)

        if len(m) > 1:
            print('More than one returned')

        if len(m) > 0:
            return m[0]

entries = EntryHost()


class Size(object):

    def __init__(self, value=None, units=None):
        self.value = value
        self.units = units

    def get_value_unit(self):
        """Parse and return a tuple given the internal one or more values"""
        if self.units is None:
            # Assume value as a unit.
            self.assume_unit = True

    def __getattr__(self, key):
        """Request another size conversion through named entry instance.
        """
        print('? Find', key)
        entry = entries.get(key)
        if entry:
            entry.modifier = self
            return entry

    def load_store(self):
        """Bind thi instance to the entries list with computed entry
        changes stored against this size"""
        for key in dir(self):
            if key.startswith('__'):
                continue
            _entry = getattr(self, key)
            if isinstance(_entry, Entry):
                self.load_entry(key, _entry)

    @property
    def name(self):
        return self.__class__.__name__

    def load_entry(self, key, entry):
        print('- Load', key, entry)
        entry.longs.append(key)
        entry.groups.append(self.name)
        entries.add(entry, self)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.value}, {self.units}>"

    @property
    def gb(self):
        return self._gb

    @gb.setter
    def gb(self, fl):
        self._gb = fl



class Entry(object):
    """An entry contains vars to compute up a chain of resolution to a marker.
    The compution is lazy
    """
    def __init__(self, shorts, value=None, units=None, longs=None, **kw):
        """Given short names, value and long names store unit computed.
        The units will traverse up a tree, resolving the value of the this
        entry.

            Entry(None, 1, 'bit')
            Entry('b', 8, 'bits')
            Entry("KB", 1_024, "Bytes")
        """
        if (shorts is not None) and (value is None):
            value = shorts
            shorts = None
        # only string, convert to iterable.
        if isinstance(shorts, str): shorts = [shorts]
        if isinstance(units, str): units = [units]

        if (value is None) and (units is None):
            # shorts is value only; other args are class defaults.
            value = 1
            units = shorts
            shorts = None

        self.longs = longs or []
        self.groups = []
        self.shorts = shorts or []
        self.value = value
        self.units = units
        self.modifier = kw.get('modifier', None)

    def match(self, key):
        """Given a key, match the long and shorts for the key value.
        return boolean for success
        """
        if key in self.longs: return True
        if key in self.shorts: return True

        return False

    def load_store(self):
        """record this entry for usage within the chain."""

    def compute(self):
        """Use internal values to compute a final value
        """
        mf = self.modifier

    def get_chain(self):
        """Return a list of ordered comput chains for the value to 1.
        """

    def __int__(self):
        """Return the computed value as an int
        """
        return self.compute()

    def __repr__(self):
        return f"<{self.__class__.__module__}.{self.__str__()}, {self.longs}>"

    def __str__(self):
        return f'Entry("{self.shorts}": {self.value} {self.units} :: {self.modifier})'



class Other(Size):
    """Some other arbitrary sizes to represent alternative loads.
    """
    floppy = Entry('fdd', 1.44, 'mb')


class BytesSize(Size):
    bit = Entry(None, 1, 'bit')
    nibble = Entry('nb', 4, 'bits')
    byte = Entry('b', 8, 'bits')
    kilobyte = Entry("KB", 1_024, "Bytes")
    megabyte = Entry("MB", 1_024, "Kilobytes")
    gigabyte = Entry("GB", 1_024, "Megabytes")
    terabyte = Entry("TB", 1_024, "Gigabytes")
    petabyte = Entry("PB", 1_024, "Terabytes")
    exabyte = Entry("EB", 1_024, "Petabytes")
    zettabyte = Entry("ZB", 1_024, "exabyte")
    yottabyte = Entry("YB", 1_024, "zettabyte")

def ChainEntry(*a):
    pass

class ByteChain(Size):
    ordered = (
        ChainEntry('kilobyte', "KB", 1024, "Bytes"),
        ChainEntry('megabyte', "MB"),
        ChainEntry('gigabyte', "GB"),
        ChainEntry('terabyte', "TB"),
        ChainEntry('petabyte', "PB"),
        ChainEntry('exabyte', "EB"),
        ChainEntry('zettabyte', "ZB"),
        ChainEntry('yottabyte', "YB"),
    )


class Animal(Size):
    horse = Entry(14.9, units='horsepower')

def test_animal():
    Size(1, 'horse') == Size(14.9, 'horsepower')
    Size(2, 'horses').horsepower == 29.8

def test_entry():
    e = Entry()
    e.units = 'month'
    assert e.plural == "months"


class BytesExtended(Size):
    unibit = Entry(1, units="bit", longs=['sniff'])
    dibit = Entry(2, units="bits", longs=['crumb', 'quad', 'quarter', 'taste',
                                          'tayste', 'tidbit', 'tydbit', 'lick',
                                          'lyck', 'semi-nibble'])
    tribit = Entry(3, units="bits", longs=['triad', 'triade', 'tribble'])
    pentad = Entry(5, units="bits", longs=['pentade', 'nickel', 'nyckle'])
    byte_old = Entry(6, units="bits", longs=["(in early IBM machines using BCD alphamerics)", 'hexad', 'hexade', 'sextet'])
    heptad = Entry(7, units="bits", longs=['heptade'])
    octet = Entry(8, units="bits", longs=['now usually called byte'])
    declet = Entry(10, units="bits", longs=['decle','deckle', 'dyme'])
    slab = Entry(12, units="bits", longs=[])
    parcel = Entry(15, units="bits", notes=["(on CDC 6600 and CDC 7600)"])
    doublet = Entry(16, units="bits", longs=['wyde', "parcel (on Cray-1)",
                                            'plate', 'playte', 'chomp',
                                            "chawmp (on a 32-bit machine)"])
    chomp = Entry(18, units="bits", longs=["chawmp (on a 36-bit machine)"])
    quadlet = Entry(32, units="bits", longs=['tetra', 'dinner', 'dynner',
                                             'gawble (on a 32-bit machine)'])
    gobble = Entry(48, units="bits", longs=['gawble'])
    octlet = Entry(64, units="bits", longs=['octa'])
    bentobox = Entry(96, units="bits", longs=['(in ITRON OS)'])
    hexlet = Entry(128, units="bits",)
    # 16 bytes:
    # # paragraph (on Intel x86 processors).
    # 6 trits: tryte.


class TimeSize(Size):
    second =       Entry("s", 1)
    minute =       Entry("m", '60 seconds')
    hour =         Entry("h", '60 minutes')
    day =          Entry("d", '24 hours')
    year =         Entry("y", '12 months')
    week =         Entry("w", '7 days')
    month =        Entry("m", '28~31 days')
    zeptosecond =  Entry('10^−21 s')
    attosecond =   Entry('10^−18 s')
    femtosecond =  Entry('10^−15 s')
    picosecond =   Entry('10^−12 s')
    nanosecond =   Entry('10^−9 s')
    shake =        Entry('10^−8 s')
    microsecond =  Entry('10^−6 s')
    millisecond =  Entry('0.001s')
    centisecond =  Entry('0.01s')
    jiffy =        Entry('1/60s')
    decisecond =   Entry('0.1s')
    moment =       Entry('1/40th of an hour')
    moment =       Entry('90 seconds')
    fortnight =    Entry('14 days 2 weeks')
    decasecond =   Entry('10 seconds')
    hectosecond =  Entry('100 seconds')
    ke =           Entry('864 seconds')
    kilosecond =   Entry('1,000 seconds')
    megasecond =   Entry('1,000,000 seconds')
    lunar =        Entry('27.2~29.5 days')
    february =     Entry('28~29 days')
    quarter =      Entry('3 months')
    season =       Entry('3 months')
    common =       Entry('365 days')
    tropical =     Entry('365.24219 days')
    gregorian =    Entry('365.2425 days')
    julian =       Entry('365.25 days')
    sidereal =     Entry('365.256363004 days')
    leap =         Entry('366 days')
    biennium =     Entry('2 years')
    triennium =    Entry('3 years')
    olympiad =     Entry('4 year cycle')
    lustrum =      Entry('5 years')
    decade =       Entry('10 years')
    indiction =    Entry('15 years')
    generation =   Entry('17~36 years')
    gigasecond =   Entry('1,000,000,000 seconds')
    jubilee =      Entry('50 years')
    lifespan =     Entry('85~82 years')
    century =      Entry('100 years')
    millennium =   Entry('1,000 years')
    kiloannum =    Entry('1,000 years')
    terasecond =   Entry('10^12 seconds')
    megaannum =    Entry('1,000,000 years')
    petasecond =   Entry('10^15 seconds')
    galactic =     Entry('230 million years')
    eon =          Entry('500 million years')
    gigaannum =    Entry('1,000,000,000 years')
    exasecond =    Entry('10^18 seconds')
    teraannum =    Entry('1,000,000,000,000 years')
    zettasecond =  Entry('10^21 seconds')
    petaannum =    Entry('1,000,000,000,000,000 years')
    yottasecond =  Entry('1024 seconds')


def test_floppy_to_cd():
    Entry('FDD', 1.44, 'mb', 'floppy')
    Entry('CD', 700, 'mb', ['cd-rom', 'compact'])
    floppy_count = 486.111111111

    assert Size('1 CD') == Size(floppy_count, 'fdd')



def test_bytes_range():
    assert Size("Kilobyte") == Size("1024 Bytes")
    assert Size("Megabyte") == Size("1024 Kilobytes")
    assert Size("Gigabyte") == Size("1024 Megabytes", )
    assert Size("Gigabyte") == Size('1,048,576 Kilobytes')
    assert Size("Terabyte") == Size("1024 Gigabytes")
    assert Size("Petabyte") == Size("1024 Terabytes" )
    assert Size("Petabyte") == Size('1,048,576 Gigabytes')
    assert Size("Exabyte")  == Size("1024 Petabytes")
    assert Size("Zettabyte") == Size("1024 Exabytes")
    assert Size("Yottabyte") == Size("1024 Zettabytes" )
    assert Size("Yottabyte") == Size('1,208,925,819,614,629,174,706,176 bytes')


def test_number_input():
    valid = (
        1,
        1.0,
        12.2,
        1_024,
        "1.1",
        "12.2",
        "1024",
        "1_024",
        "1,234,123",
        "1_234_123",
        )

    for key in valid:
        assert Size(key, unit='bytes').is_valid()


def test_kb():
    # Kilobytes (KB)  Megabytes (MB) decimal  Megabytes (MB) binary
    # 1 KB    0.001 MB    0.0009765625 MB
    line("5 KB", "  0.005 MB",    "0.0048828125 MB")
    line("10 KB", " 0.01 MB", "0.009765625 MB")
    line("15 KB", " 0.015 MB",    "0.0146484375 MB")
    line("20 KB", " 0.02 MB", "0.01953125 MB")
    line("25 KB", " 0.025 MB",    "0.0244140625 MB")
    line("30 KB", " 0.03 MB", "0.029296875 MB")
    line("35 KB", " 0.035 MB",    "0.0341796875 MB")
    line("40 KB", " 0.04 MB", "0.0390625 MB")
    line("45 KB", " 0.045 MB",    "0.0439453125 MB")
    line("50 KB", " 0.05 MB", "0.048828125 MB")
    line("55 KB", " 0.055 MB",    "0.0537109375 MB")
    line("60 KB", " 0.06 MB", "0.05859375 MB")
    line("65 KB", " 0.065 MB",    "0.0634765625 MB")
    line("70 KB", " 0.07 MB", "0.068359375 MB")
    line("75 KB", " 0.075 MB",    "0.0732421875 MB")
    line("80 KB", " 0.08 MB", "0.078125 MB")
    line("85 KB", " 0.085 MB",    "0.0830078125 MB")
    line("90 KB", " 0.09 MB", "0.087890625 MB")
    line("95 KB", " 0.095 MB",    "0.0927734375 MB")
    line("100 KB", "0.1 MB",  "0.09765625 MB")
    line("105 KB", "0.105 MB",    "0.1025390625 MB")
    line("110 KB", "0.11 MB", "0.107421875 MB")
    line("115 KB", "0.115 MB",    "0.1123046875 MB")
    line("120 KB", "0.12 MB", "0.1171875 MB")
    line("125 KB", "0.125 MB",    "0.1220703125 MB")
    line("130 KB", "0.13 MB", "0.126953125 MB")
    line("135 KB", "0.135 MB",    "0.1318359375 MB")
    line("140 KB", "0.14 MB", "0.13671875 MB")
    line("145 KB", "0.145 MB",    "0.1416015625 MB")
    line("150 KB", "0.15 MB", "0.146484375 MB")
    line("155 KB", "0.155 MB",    "0.1513671875 MB")
    line("160 KB", "0.16 MB", "0.15625 MB")
    line("165 KB", "0.165 MB",    "0.1611328125 MB")
    line("170 KB", "0.17 MB", "0.166015625 MB")
    line("175 KB", "0.175 MB",    "0.1708984375 MB")
    line("180 KB", "0.18 MB", "0.17578125 MB")
    line("185 KB", "0.185 MB",    "0.1806640625 MB")
    line("190 KB", "0.19 MB", "0.185546875 MB")
    line("195 KB", "0.195 MB",    "0.1904296875 MB")
    line("200 KB", "0.2 MB",  "0.1953125 MB")
    line("205 KB", "0.205 MB",    "0.2001953125 MB")
    line("210 KB", "0.21 MB", "0.205078125 MB")
    line("215 KB", "0.215 MB",    "0.2099609375 MB")
    line("220 KB", "0.22 MB", "0.21484375 MB")
    line("225 KB", "0.225 MB",    "0.2197265625 MB")
    line("230 KB", "0.23 MB", "0.224609375 MB")
    line("235 KB", "0.235 MB",    "0.2294921875 MB")
    line("240 KB", "0.24 MB", "0.234375 MB")
    line("245 KB", "0.245 MB",    "0.2392578125 MB")
    line("250 KB", "0.25 MB", "0.244140625 MB")
    line("255 KB", "0.255 MB",    "0.2490234375 MB")
    line("260 KB", "0.26 MB", "0.25390625 MB")
    line("265 KB", "0.265 MB",    "0.2587890625 MB")
    line("270 KB", "0.27 MB", "0.263671875 MB")
    line("275 KB", "0.275 MB",    "0.2685546875 MB")
    line("280 KB", "0.28 MB", "0.2734375 MB")
    line("285 KB", "0.285 MB",    "0.2783203125 MB")
    line("290 KB", "0.29 MB", "0.283203125 MB")
    line("295 KB", "0.295 MB",    "0.2880859375 MB")
    line("300 KB", "0.3 MB",  "0.29296875 MB")
    line("305 KB", "0.305 MB",    "0.2978515625 MB")
    line("310 KB", "0.31 MB", "0.302734375 MB")
    line("315 KB", "0.315 MB",    "0.3076171875 MB")
    line("320 KB", "0.32 MB", "0.3125 MB")
    line("325 KB", "0.325 MB",    "0.3173828125 MB")
    line("330 KB", "0.33 MB", "0.322265625 MB")
    line("335 KB", "0.335 MB",    "0.3271484375 MB")
    line("340 KB", "0.34 MB", "0.33203125 MB")
    line("345 KB", "0.345 MB",    "0.3369140625 MB")
    line("350 KB", "0.35 MB", "0.341796875 MB")
    line("355 KB", "0.355 MB",    "0.3466796875 MB")
    line("360 KB", "0.36 MB", "0.3515625 MB")
    line("365 KB", "0.365 MB",    "0.3564453125 MB")
    line("370 KB", "0.37 MB", "0.361328125 MB")
    line("375 KB", "0.375 MB",    "0.3662109375 MB")
    line("380 KB", "0.38 MB", "0.37109375 MB")
    line("385 KB", "0.385 MB",    "0.3759765625 MB")
    line("390 KB", "0.39 MB", "0.380859375 MB")
    line("395 KB", "0.395 MB",    "0.3857421875 MB")
    line("400 KB", "0.4 MB",  "0.390625 MB")
    line("405 KB", "0.405 MB",    "0.3955078125 MB")
    line("410 KB", "0.41 MB", "0.400390625 MB")
    line("415 KB", "0.415 MB",    "0.4052734375 MB")
    line("420 KB", "0.42 MB", "0.41015625 MB")
    line("425 KB", "0.425 MB",    "0.4150390625 MB")
    line("430 KB", "0.43 MB", "0.419921875 MB")
    line("435 KB", "0.435 MB",    "0.4248046875 MB")
    line("440 KB", "0.44 MB", "0.4296875 MB")
    line("445 KB", "0.445 MB",    "0.4345703125 MB")
    line("450 KB", "0.45 MB", "0.439453125 MB")
    line("455 KB", "0.455 MB",    "0.4443359375 MB")
    line("460 KB", "0.46 MB", "0.44921875 MB")
    line("465 KB", "0.465 MB",    "0.4541015625 MB")
    line("470 KB", "0.47 MB", "0.458984375 MB")
    line("475 KB", "0.475 MB",    "0.4638671875 MB")
    line("480 KB", "0.48 MB", "0.46875 MB")
    line("485 KB", "0.485 MB",    "0.4736328125 MB")
    line("490 KB", "0.49 MB", "0.478515625 MB")
    line("495 KB", "0.495 MB",    "0.4833984375 MB")
    line("500 KB", "0.5 MB",  "0.48828125 MB")


if __name__ == '__main__':
    main()
