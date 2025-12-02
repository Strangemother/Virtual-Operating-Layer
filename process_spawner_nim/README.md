# Process Spawner (Nim)

Spawns multiple child processes (Python, Bash, etc.) and tracks their PIDs.

## Features

- Spawn any number of processes with different commands
- Track PIDs of all spawned processes
- Wait for completion and get exit codes
- Works with Python, Bash, PowerShell, or any executable

## Compile

```bash
nim c process_spawner.nim
```

## Run

```bash
./process_spawner
```

## Example Output

```
Process Spawner - Starting applications...

Spawned: python3 (PID: 12345)
Spawned: bash (PID: 12346)
Spawned: sleep (PID: 12347)

Active PIDs:
  python3: 12345
  bash: 12346
  sleep: 12347

Waiting for all processes to complete...
Bash done
bash (PID 12346) exited with code: 0
Python done
python3 (PID 12345) exited with code: 0
sleep (PID 12347) exited with code: 0

All processes completed
```

## Customization

Edit the `main()` function to spawn different processes:

```nim
processes.add(spawnApp("powershell", ["-Command", "Write-Host 'Hello from PowerShell'"]))
processes.add(spawnApp("node", ["-e", "console.log('Hello from Node')"]))
```
