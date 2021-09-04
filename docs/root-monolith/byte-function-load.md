
1. The memory module can access a HOST vol file (relative to the install position)
2. Another monolith function can load memory byte arrays as a compiled executable
3. The os can access the executable at the loaded memory address

The memory unit allows access to byte lists, and hosts those within the RAM as _cast_ chunks of expected memory. OS operations may request a memory pointer at an address, and load the bytes into the compiler, converting the memory byte array to a executable byte array.

The code allocator stores the "chunk" of ready-to-use executable to a register point under a predicable function name.

The code data may be collected from the memory module through an os operation request. The code chunk may be a pre-compiled code object waiting as a HOST file object (text file of bytes), or generated through a macro compiler through the terminal. In both cases the content resolves through the memory collector.
