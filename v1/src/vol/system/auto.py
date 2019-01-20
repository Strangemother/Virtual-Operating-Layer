"""
Automatically installs the core system features for the boot.

As this is a virtual layer we must consider the BIOD as a sandbox and
centralization of commands. Loading usually consists of Master Boot Record >
 Partition REcord > Grub > Kernel > Init > Runtime

 This is extrapolated as we need to BOOT the VOL, accessing multiple endpoints
 and waking API VDUs USB etc.

Therefore a KERNEL in this case is a ZIM-SEM with procedual records for boot.
This is CRC signed, with IO only for the BIOS.

This flow Performs:
    BIOS    Autoload core config finding the _kernel_ zim-sem
    MBR     write  A base layer of coms to the open runtime
    *SEM     MBR chain to handoff - Executing the LOAD
            - The SEM contains all potent records for auto execute.
              The sequence will call the KERNAL
    KERNEL  A SEM with event read - isolating the SEM, MBR, BIOS
            - The Kernel SEM includes config and settings for base allowances.

In a virtual OS, this low-level kernel is offset to the container. Therefore the _kernel_
is the base of all VOL. Read/write is done through isolation and encrypted.

At KERNEL - the init layer loads the base of code for the VOL.

+ Hardware / API initialisation
+ Module and compiled drivers
+ First instance of editable API.


"""
from ctypes import string_at
from sys import getsizeof
from binascii import hexlify


def main():
    return auto_main()


def read_mem(a):
    res = string_at(id(a), getsizeof(a))
    return hexlify(res)


def auto_main():
    """Create the base system. Recording the core records and booting a bios.
    """
    # GET Boot record
    # BOOT Record
    """After the boot is open, it'll write to a specific location written to the BIOS
    zim-sem during compilation. This writes the required parameters to the
    initial mcom location.
    """
    print('Auto')

    # load bois.
    # This is a self executing VOL biod with configurations
    # all built into one sem. the load paramters UDP and Tape to a Master Boot Record.
    # Kernels are referenced by address
    #
    # read SEM for
    #   base config
    #   first execution statements
    #   boot apis
    #   Import and boot basic app base.
        # import something?
        # send event
        # wait execute
        # read mcom
        # execute statements
        # sent finish event
        # offload to mbr

    # Load MBR
        # read config from mcom event
        # ready core hardware/api
        # import kernels
        # import boot record sem
        # read boot record options
            # ? keyboard interrupt
            # ? load menus / built in config
            # ? password
        # memory load given kernel
        # sent event
        # offload - wait for closer before offload.

    # load kernel
        # read comfig from mcom event
        # load drivers
        # manage and close MBR
        # load software
        # ...



if __name__ == '__main__':
    main()
