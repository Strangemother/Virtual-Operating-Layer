All the content about the filesystem. At the moment called 'VFS'

+ https://www.win.tue.nl/~aeb/linux/Large-Disk.html
+ https://en.wikipedia.org/wiki/GUID_Partition_Table

# goal

The FS designed for linear and graph storage
hemmoengous,
built for real, abstract or distributed content.
Compatible with disk or object based storage
With custom service integration.
natural backups and historical changes
partial or full encryption
will work with any file system type such as EXT4, NTFS or even minix
Core throughput to base IO - SATA communication or core bytes and binary

# Future goal

transparent bridge of volatile and persistent storage - for a future of flat high-speed data devices without the RAM <> DISK divide.

## filesystem


The base IO for persistent data stored locally within freely addressable memory. Dubbed a VFS for "Virtual [Operating Layer] File System" _(*another name?)_ with CLI pinched from C standard STDIO

+ `open`, `close`... and other base operations
+ Encryption, Decryption, Auto hashing.

Extending further than traditional file data. A example _file_ consists of some meta data, a data dictionary and data segments defined as hash managed blocks of bytes.

As a quick overview:

+ A _file_ is a random access dictionary of addresses to uneven chunks of bytes within memory
+ Each _file_ maintains a recorded hash of the current state calculated upon each write to a file structure.
+ The `filesystem` maintains an open hash until a file is closed writing to _file_ meta
+ meta of a file holds VOL persistent information of the _file_ data dictionary such as local name and immediate hash.

The data segments exist without an associated file loaning addresses through a linear dictionary only accessible through the `filesystem`. A virtually allocated memory table persists a record of real memory location to a given hash address.

This serves as a safety mechanism for overwriting addresses. Moving data segments is not required; as a file does not maintain a _linear_ address list. Therefore a data segment does not need to live with a _file_

    filesystem
        open
        close


    fileio -> write byte --> put to MEM on assigned ADDRESS -> spill to new segments
                         |
                         |-> calculate persistent hash
     -> save close       |-> write hash to meta -> put floating segments to persistent -> clean mem


