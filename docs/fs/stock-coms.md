Elements to bridge

## IPFS

A Particle and Grain can store content into an IPFS graph, storing the content hash
into the local header. Retrieval of the data should be primed and returned as a
particle shard.

## SCSI

Raw device SCSI And ACHI throughput for base device communuication.
This extends to LBA and SDA based communication for raw _byte_ and sector retrieval.

Note: Old style cylinder, sector allocations of data doesn't exist in with
post mechanical disk devices. As such all content will focus on a future of NVMe and other PCIe compatible devices.

## FTP/S3

First and foremost abstracting FTP/SFTP, S3 and general object storage to facilitate long term and distant backups.


## Network

Classic connection for abstracted VOL drives and services. This is essentially a
byte-for-byte transport over the wire to a transparent recevier, marked as a storage
device. The translation and procotol method are FS and VOL defined.

+ Byte like transport
+ encrypt with aes or stream cipher
+ emit through connected coms devices: wifi, bluetooth, lora ftp etc..
+ Transport with stream RPC such as GRPC
+ parity bits through reed solomon bit care



# Allocation

All types of throughput and connected devices are allocated a job or a set of jobs.
Through VOL the concept of 'files' is abstracted into a custom streaming procotol of file chunks and read keys. A particle persists a connection to its data chunk through an allocation of type; such as local, memory, ftp, s3 etc...

+ Allocation a usage: memory extend, spill, cold store, ram etc...
+ Connection methods and credentials
+ Mapping protocols and translation functions


# Ram local memory

The RAM or local memory as a concept will be phased out, in favour of one session - a session ram allocated for user functionality. As all information is expected to be a 'stream' state, the ram caches a locally persisted system (VOL) of which stream are received per stack.

A Stack is essentially a sandboxed process - like a task without a parent. The stack manages its work communicating any expected results into the local memory. This may be RAM or a file pointer. The return value is digested by the waiting process to seek the RAM pointers and access particle content.

As such the ram is mainly for passing and loading file and :memory: data pointers. The master VOL probably isn't loaded on the FS memory system, therefore CPU cycles and RAM are purely for the passing of pointers through tasks.

Note: The VOL interface will collect lazy particle through the aggregate -> grain header reference (a pointer) and seek to resolve each particle as required. This removes memory overhead as _seeked_ pointers are always a subset of the overall aggregate (a file)

---

A Particle represents a single chunk given from any connected allocation. When resolved the content is moved to a read space and a seek pointer is given to the owning process.
We're assuming (always) the FS is disconnected from the owning process original caller and any sub tasks, such as local memory, db or even ftp calls.
Upon sucessesful resolution of a particle chunk, the content is handled by transport and translation layers to yeild a pointer to a local reference.

The local reference is essentially a RAM pointer, but it's wrapped in a Particle type as a descriptor for the original caller. The Paricle API can return the content as a seek stream for the digestor.
