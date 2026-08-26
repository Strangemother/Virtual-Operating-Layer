import std/[os, strutils]

type
  HostMemory = object
    totalBytes: uint64
    availableBytes: uint64

proc readMeminfoKiB(label: string): uint64 =
  for line in readFile("/proc/meminfo").splitLines():
    let fields = line.splitWhitespace()

    if fields.len >= 2 and fields[0] == label:
      # /proc/meminfo reports these values in KiB.
      return parseUInt(fields[1])

  raise newException(IOError, "Missing " & label & " in /proc/meminfo")

proc getHostMemory(): HostMemory =
  result.totalBytes =
    readMeminfoKiB("MemTotal:") * 1024'u64

  result.availableBytes =
    readMeminfoKiB("MemAvailable:") * 1024'u64

proc toMiB(bytes: uint64): uint64 =
  bytes div (1024'u64 * 1024'u64)

when isMainModule:
  let memory = getHostMemory()

  echo "Total RAM:      ", toMiB(memory.totalBytes), " MiB"
  echo "Available RAM:  ", toMiB(memory.availableBytes), " MiB"