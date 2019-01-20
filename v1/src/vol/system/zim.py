"""a zip module complete with internal crc for each key
zip implemented module to be executed from
self executing file (sef)

"""
import zipfile
import gzip
from datetime import datetime

MASTER = bytes('lock','UTF-8')

def main():
    name = 'foo.zip'
    internal = 'test.foo'
    write((internal, ['cake', 'berry', 'window', 'egg'], ), name, mode='a')
    print(read(name))


def write(data, file, mode='x'):

    _zip = zipfile.ZipFile(file,
        mode=mode,
        compression=zipfile.ZIP_STORED)

    filename, content = data
    write_procedural(filename, content, _zip)
    _zip.setpassword(MASTER)
    _zip.close()


def write_procedural(filename, data_lines, pkg):
    internal_file = filename
    tt = tuple(datetime.now().timetuple())[:6]

    for string in data_lines:
        print('write', string)
        info = zipfile.ZipInfo(filename=internal_file, date_time=tt)
        pkg.writestr(info, string)


def read(file):
    _zip = zipfile.ZipFile(file, mode='r')
    keys=  [
        'filename',
        'date_time',
        "create_system",
        "volume",
        "CRC",
        "compress_size",
        "file_size",
    ]

    lines = {}
    for inf in _zip.infolist():
        ds = tuple((x,getattr(inf, x),) for x in keys)

        if (inf.filename in lines) is False:
            lines[inf.filename] = ()

        with _zip.open(inf) as handle:
            lines[inf.filename] += ( handle.read(), )

    return lines

if __name__ == '__main__':
    main()
