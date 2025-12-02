import osproc, os, tables, strutils, threadpool, times

type
  ProcessInfo = object
    process: Process
    pid: int
    command: string

var processes: seq[ProcessInfo] = @[]
var running = true

proc spawnApp(command: string, args: openArray[string] = []): ProcessInfo =
  ## Spawn a new process and return its info
  let process = startProcess(command, args = args, options = {poParentStreams})
  let pid = process.processID()
  echo "Spawned: ", command, " (PID: ", pid, ")"
  return ProcessInfo(process: process, pid: pid, command: command)

proc killProcess(pid: int): bool =
  ## Kill a process by PID, return true if successful
  for i, info in processes:
    if info.pid == pid:
      try:
        info.process.kill()
        echo "Killed process: ", info.command, " (PID: ", pid, ")"
        return true
      except:
        echo "Failed to kill PID: ", pid
        return false
  echo "PID not found: ", pid
  return false

proc getProcessMemory(pid: int): string =
  ## Get memory usage for a process in MB
  try:
    let output = execProcess("ps", args = ["-p", $pid, "-o", "rss="])
    let rssKB = parseInt(output.strip())
    let rssMB = rssKB.float / 1024.0
    return formatFloat(rssMB, ffDecimal, 2) & " MB"
  except:
    return "N/A"

proc listActiveProcesses() =
  ## List all active processes with memory usage
  echo ""
  echo "Active processes:"
  var hasActive = false
  for info in processes:
    if info.process.running():
      let mem = getProcessMemory(info.pid)
      echo "  ", info.command, ": ", info.pid, " (", mem, ")"
      hasActive = true
  if not hasActive:
    echo "  (none)"
  echo ""

proc monitorLoop() {.thread.} =
  ## Background thread that monitors memory every second
  while running:
    sleep(1000)
    if running:
      stdout.write("\r\x1b[K")  # Clear line
      var stats: seq[string] = @[]
      for info in processes:
        if info.process.running():
          let mem = getProcessMemory(info.pid)
          stats.add("PID " & $info.pid & ": " & mem)
      if stats.len > 0:
        stdout.write("[Memory] " & stats.join(" | "))
        stdout.flushFile()

proc main() =
  echo "Process Spawner - Starting applications..."
  echo ""
  
  # Spawn different types of applications (longer running for testing)
  processes.add(spawnApp("python3", ["-c", "import time; time.sleep(30); print('Python done')"]))
  processes.add(spawnApp("bash", ["-c", "sleep 30; echo 'Bash done'"]))
  processes.add(spawnApp("sleep", ["30"]))
  
  listActiveProcesses()
  
  echo "Commands:"
  echo "  - Type a PID to kill that process"
  echo "  - Type 'list' to show active processes"
  echo "  - Type 'quit' to exit and kill all"
  echo ""
  echo "Memory monitoring updates every 1 second..."
  echo ""
  
  # Start memory monitoring thread
  var monitorThread: Thread[void]
  createThread(monitorThread, monitorLoop)
  
  # Interactive loop
  while true:
    # Check if any processes are still running
    var anyRunning = false
    for info in processes:
      if info.process.running():
        anyRunning = true
        break
    
    if not anyRunning:
      echo ""
      echo "All processes have completed"
      break
    
    stdout.write("\nEnter command: ")
    stdout.flushFile()
    let input = readLine(stdin).strip()
    
    if input == "quit":
      echo "Killing all processes..."
      for info in processes:
        if info.process.running():
          info.process.kill()
      break
    elif input == "list":
      listActiveProcesses()
    else:
      try:
        let pid = parseInt(input)
        discard killProcess(pid)
      except ValueError:
        echo "Invalid input. Enter a PID number, 'list', or 'quit'"
  
  # Stop monitoring thread
  running = false
  sleep(1500)  # Give thread time to exit
  
  echo ""
  echo "Cleaning up..."
  
  # Wait for all processes to finish
  for info in processes:
    if info.process.running():
      discard info.process.waitForExit()
  
  echo "All processes terminated"

when isMainModule:
  main()
