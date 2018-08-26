# The read tape is a procedural file for IO byte writing to a volatile
# memory pointer for instructions loaded into a tape reader.

# The Read tape is the BIOS WAKE STATE file - providing an initial pointer of
# memory input to the BIOS - offloading from the HOST containter.

"""For input A tape loads from seek(0) and continues until a stop statment.

This module is loaded into a instuction reader and compiled into a BIOS
Additional instructions after compilation may be applied with ALLOWED bios
compiled instructions.

These allow runtime changes I expect not secure at the top level.
This is essentially a BIOS app; allowing secured mini language for runtime compilation

After this point the BIOS will post, using the instructions.
These instructions run exposed apps for the bios.

Mostly this is to ensure pluggability in the future for aspects I cannot consider.
Elements I won't be writing myself; such as loading kernel components from a network
as this will expose the runtime - and slow the boot process, but a user may need it.

Encryption of the BIOS is a consideration. Building a BIOS App and adding routines
to a TAPE -
A Single instruction is compiled into a relative C statement into the BIOS (in this case)

"""
OUT file
