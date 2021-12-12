# Data secruity

To secure the bios data, the values stored within bit memory should be tested upon read/write and periodically.

When a Byte is written or read, test the CRC of the target block. If the CRC fails the data is suspicious and should be revoked.

Through a periodical background checker, recompute the bits and test against the CRC record. This should occur outside the current system resource (off the main CPU) within a locked lower frame, with the ability to access lower memory.


## Why

At the root level the bits in RAM should be protected. This can occur much later however I feel it's important to bake the security tooling into the core. As this manifests as a _unikernel_, the "bios bits" are somewhat exposed, allowing a bad-actor to manipulate those bits through a shared-memory hack.

To mitigate the ability to randomly flip bits in a secure space we test these secure records in another location, on another CPU or sandboxed process. This has shared-memory view access of the monolith bios bits.

The CRC machine can compute bits upon request, and potentially store the value for a later test.


# Hard Protection

When enabled to "hard protect" for read or write will test the _current_ CRC for the action occurs. If the CRC is incorrect, the action will fail.

When protecting BIOS bits in a background mode, a r/w failure may occur in a full destruction of the owning service and/or the target process. If the target process is the BIOS, this will result in a catastrophic failure of the monolith and all VOL resources.

## Background flips

As this case notes a background bit flip, it may be too late to catch the bad-actor. A bad actor may be:

+ Software mismanagement
+ A hardware fault
+ Black-Hat hacking
+ Cosmic Ray

Recovery would by nice, but the first solution should be absolute security, with a complete wipe of the fautly data and a reset.


## Foreground (layer) flips

Any value written through the current context is subject to the security rules of that layer. In the lowest BIOS frame the bits are open to read write, however in upper frames (and the visual layer) The user writes are subject to AOP tests before the literal writes.


### Immediate Action

An immediate flip occurs during the read/write of a lowest frame change. In these cases the layer has access to the BIOS facade, where read/write is done through the root layers. The function tests the CRC before the entry and result in a memory fault if a failure occurs.

1. VOL is awake, BIOS bits are CRC safe
2. a bad actor flips a bios bit
3. The user performs a "read"
4. The function call fails yielding an error.


### Late action

1. VOL is awake, BIOS bits are CRC safe
2. a bad actor flips a bios bit
3. the background test marks a change
4. An error cascade through owning services.


# Verified Writes

For a stringent security routine the CRC service should allow access to read and write given a token or permissions from the user. This should occur as a separate step to the r/w action.

1. User makes a (unsaved) bit change
2. User _requests write access_
3. The CRC machine tests securities
4. Write "keypass" to the correct memory location
5. return a success response to the caller
6. The write occurs + A new CRC is calculated


## Access Request

The CRC service exists independently of the user services, on the message bus and shared-memory within its own MCU or CPU+thread.

Fundamentally it should not be possible to alter the service state manually, only asking _if X is okay_. The CRC machine requires access to the bits its protecting, however this may be a security fault itself. As such the _startup process_ for a single CRC validator reads bits as per its own temporary permissions.

1. CRC machine wake up
2. Receives "compute this" on a shared memory location
3. The value is stored against the known memory location
4. respond OK

Updates and tests similarly maintain no access questions. Tests should query if the current memory is okay:

1. receive "Is this okay" on a shared memory location
2. compute the CRC, asset equals on the same named memory location slotname
3. return response

An update should ask for a _write_ allowance. Without the pre-certification, the next CRC test will fail - likely within the function used to call _write_

1. User service requests a "Write CRC"
2. CRC Machine tests the user space
3. Write validation bits within the user space
4. respond with a write key
5. User performs a 'write', providing the bits and key
6. The write message tests the _given_ user space (hopefully the same), and the new key
7. respond OK.
8. strip bits from the user space.






