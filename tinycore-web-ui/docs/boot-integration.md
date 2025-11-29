# TinyCore Linux Boot Integration Guide

Complete guide for integrating the TinyCore UI Manager into the boot process to capture output from the earliest stages.

## TinyCore Boot Sequence Overview

```
┌─────────────────────────────────────────────┐
│  1. BIOS/UEFI                               │
│     - Hardware POST                         │
│     - Load bootloader from disk             │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  2. ISOLINUX/GRUB Bootloader                │
│     - Load kernel (vmlinuz)                 │
│     - Load initrd (core.gz)                 │
│     - Pass boot parameters                  │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  3. Linux Kernel Starts                     │
│     - Decompress initrd to RAM              │
│     - Mount initramfs as /                  │
│     - Initialize hardware drivers           │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  4. Init Script (/init in initrd)           │
│     - Mount /proc, /sys, /dev               │
│     - Load modules                          │
│     - Run /opt/bootsync.sh                  │
│     - Run /opt/bootlocal.sh                 │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  5. User Space Services                     │
│     - Start network                         │
│     - Mount extensions                      │
│     - Start getty (login prompts)           │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  6. X11/Desktop (if configured)             │
│     - Start X server                        │
│     - Launch window manager                 │
└─────────────────────────────────────────────┘
```

## Phase 1: Basic Boot Integration

### Step 1: Install TinyCore Manager as Extension

Create a TinyCore extension (.tcz) for your manager:

```bash
# Directory structure
/tmp/tinycore-manager.tcz/
├── usr/
│   └── local/
│       ├── bin/
│       │   └── tinycore-manager          # Main daemon
│       ├── lib/
│       │   └── tinycore-manager/         # Python modules
│       └── share/
│           └── doc/
│               └── tinycore-manager/
└── usr/
    └── local/
        └── tce.installed/
            └── tinycore-manager          # Post-install script
```

**Post-install script** (`/usr/local/tce.installed/tinycore-manager`):
```bash
#!/bin/sh
# Runs after extension is loaded

# Create config directory
mkdir -p /etc/tinycore-manager

# Create default config if doesn't exist
if [ ! -f /etc/tinycore-manager/config.json ]; then
    cat > /etc/tinycore-manager/config.json <<'EOF'
{
  "listen": "0.0.0.0:8080",
  "collectors": ["boot", "pty", "system"],
  "capture_boot_logs": true
}
EOF
fi

# Make persistent (optional)
echo "/etc/tinycore-manager" >> /opt/.filetool.lst
```

### Step 2: Start Manager Early in Boot

Edit `/opt/bootlocal.sh` (runs early in boot, before most services):

```bash
#!/bin/sh
# /opt/bootlocal.sh - TinyCore early boot script

# Capture kernel boot messages immediately
echo "Starting TinyCore UI Manager..."

# Start the manager daemon in background
/usr/local/bin/tinycore-manager daemon \
    --config /etc/tinycore-manager/config.json \
    --log /var/log/tinycore-manager.log \
    > /dev/null 2>&1 &

# Wait for daemon to be ready
sleep 2

# Send boot logs to manager
dmesg | /usr/local/bin/tinycore-manager capture --source kernel-ring-buffer

# Continue with normal boot
# ... rest of your bootlocal.sh
```

Make it persistent:
```bash
sudo cp /opt/bootlocal.sh /mnt/sda1/tce/
echo "/opt/bootlocal.sh" >> /opt/.filetool.lst
sudo filetool.sh -b
```

### Step 3: Capture Boot Messages

Create a boot collector module:

**File**: `manager/tinycore_manager/collectors/boot_collector.py`

```python
"""
Boot Collector - Captures system boot logs and early messages.
"""

import asyncio
import subprocess
import os
from typing import Optional, Callable
from datetime import datetime


class BootCollector:
    """Captures boot logs from various sources."""
    
    def __init__(self, emit_callback: Callable):
        self.emit = emit_callback
        self.boot_start_time = datetime.now()
    
    async def capture_all(self):
        """Capture all boot-related logs."""
        await asyncio.gather(
            self.capture_kernel_log(),
            self.capture_boot_messages(),
            self.capture_hardware_info(),
            return_exceptions=True
        )
    
    async def capture_kernel_log(self):
        """Capture kernel ring buffer (dmesg)."""
        try:
            result = subprocess.run(
                ['dmesg', '--color=never'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                
                # Emit as log resource
                self.emit('resource.create', {
                    'id': 'boot:kernel-log',
                    'payload': {
                        'source': 'kernel',
                        'timestamp': self.boot_start_time.isoformat(),
                        'lines': lines,
                        'raw': result.stdout
                    },
                    'meta': {
                        'component': 'log.v1',
                        'version': 1
                    }
                })
                
                print(f"✓ Captured {len(lines)} kernel log lines")
        
        except Exception as e:
            print(f"Failed to capture kernel log: {e}")
    
    async def capture_boot_messages(self):
        """Capture boot messages from /var/log/messages."""
        log_file = '/var/log/messages'
        
        if not os.path.exists(log_file):
            return
        
        try:
            with open(log_file, 'r') as f:
                lines = f.readlines()
            
            self.emit('resource.create', {
                'id': 'boot:syslog',
                'payload': {
                    'source': 'syslog',
                    'timestamp': self.boot_start_time.isoformat(),
                    'lines': [line.strip() for line in lines],
                    'raw': ''.join(lines)
                },
                'meta': {
                    'component': 'log.v1',
                    'version': 1
                }
            })
            
            print(f"✓ Captured {len(lines)} syslog lines")
        
        except Exception as e:
            print(f"Failed to capture syslog: {e}")
    
    async def capture_hardware_info(self):
        """Capture hardware information."""
        hardware = {}
        
        # CPU info
        try:
            with open('/proc/cpuinfo', 'r') as f:
                cpuinfo = f.read()
                # Parse CPU model
                for line in cpuinfo.split('\n'):
                    if line.startswith('model name'):
                        hardware['cpu'] = line.split(':', 1)[1].strip()
                        break
        except:
            pass
        
        # Memory info
        try:
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal'):
                        kb = int(line.split()[1])
                        hardware['memory_mb'] = kb // 1024
                        break
        except:
            pass
        
        # Disk info
        try:
            result = subprocess.run(
                ['df', '-h'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                hardware['disks'] = result.stdout
        except:
            pass
        
        # Network interfaces
        try:
            result = subprocess.run(
                ['ip', 'addr'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                hardware['network'] = result.stdout
        except:
            pass
        
        # Emit hardware info
        self.emit('resource.create', {
            'id': 'boot:hardware',
            'payload': hardware,
            'meta': {
                'component': 'hardware.v1',
                'version': 1
            }
        })
        
        print(f"✓ Captured hardware info")
    
    async def watch_boot_progress(self):
        """Monitor boot progress in real-time."""
        # Watch for new dmesg entries
        proc = await asyncio.create_subprocess_exec(
            'dmesg', '--follow', '--color=never',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        while True:
            line = await proc.stdout.readline()
            if not line:
                break
            
            decoded = line.decode('utf-8', errors='replace').strip()
            
            # Emit real-time boot message
            self.emit('boot.message', {
                'id': 'boot:live',
                'payload': {
                    'message': decoded,
                    'timestamp': datetime.now().isoformat()
                }
            })


# Integration example
if __name__ == '__main__':
    import sys
    
    def print_event(event_type: str, data: dict):
        print(f"{event_type}: {data}")
    
    async def main():
        collector = BootCollector(emit_callback=print_event)
        await collector.capture_all()
    
    asyncio.run(main())
```

## Phase 2: Kernel Console Redirection

### Step 1: Configure Kernel Boot Parameters

Edit bootloader config to redirect console output:

**For ISOLINUX** (`/mnt/sda1/boot/isolinux/isolinux.cfg`):
```
DEFAULT tinycore
LABEL tinycore
    KERNEL /boot/vmlinuz
    APPEND initrd=/boot/core.gz console=tty0 console=ttyS0,115200n8
```

**For GRUB** (`/boot/grub/grub.cfg`):
```
menuentry "TinyCore with UI Manager" {
    linux /boot/vmlinuz console=tty0 console=ttyS0,115200n8 loglevel=7
    initrd /boot/core.gz
}
```

Parameters explained:
- `console=tty0` - Keep output on local display
- `console=ttyS0,115200n8` - Also send to serial port (115200 baud, 8N1)
- `loglevel=7` - Debug level (0=panic, 7=debug)

### Step 2: Capture Serial Console

Add serial console capture to your manager:

**File**: `manager/tinycore_manager/collectors/serial_collector.py`

```python
"""
Serial Console Collector - Captures kernel/boot messages from serial port.
"""

import asyncio
import serial
from typing import Callable


class SerialCollector:
    """Captures output from serial console."""
    
    def __init__(self, port: str = '/dev/ttyS0', baudrate: int = 115200, 
                 emit_callback: Callable = None):
        self.port = port
        self.baudrate = baudrate
        self.emit = emit_callback or (lambda *args: None)
        self.running = False
    
    async def start(self):
        """Start capturing serial console."""
        try:
            ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )
            
            self.running = True
            print(f"✓ Serial console capture started on {self.port}")
            
            # Emit initial resource
            self.emit('resource.create', {
                'id': 'boot:serial-console',
                'payload': {
                    'port': self.port,
                    'baudrate': self.baudrate,
                    'state': 'capturing'
                },
                'meta': {
                    'component': 'console.v1',
                    'version': 1
                }
            })
            
            # Read loop
            buffer = ""
            while self.running:
                if ser.in_waiting > 0:
                    chunk = ser.read(ser.in_waiting).decode('utf-8', errors='replace')
                    buffer += chunk
                    
                    # Emit line by line
                    while '\n' in buffer:
                        line, buffer = buffer.split('\n', 1)
                        
                        self.emit('console.data', {
                            'id': 'boot:serial-console',
                            'payload': {
                                'line': line,
                                'source': 'serial'
                            }
                        })
                else:
                    await asyncio.sleep(0.01)
        
        except Exception as e:
            print(f"Serial console error: {e}")
    
    def stop(self):
        """Stop capturing."""
        self.running = False
```

## Phase 3: Network Console (Remote Capture)

For capturing boot logs over the network (useful for remote/headless systems):

### Step 1: Configure netconsole

Add to kernel boot parameters:
```
netconsole=6666@192.168.1.100/eth0,6667@192.168.1.200/
```

This sends kernel messages via UDP to `192.168.1.200:6667`.

### Step 2: Capture Network Console

**File**: `manager/tinycore_manager/collectors/netconsole_collector.py`

```python
"""
Network Console Collector - Captures kernel messages via UDP.
"""

import asyncio
from typing import Callable


class NetconsoleCollector:
    """Captures kernel netconsole output via UDP."""
    
    def __init__(self, port: int = 6666, emit_callback: Callable = None):
        self.port = port
        self.emit = emit_callback or (lambda *args: None)
    
    async def start(self):
        """Start UDP listener for netconsole."""
        
        class NetconsoleProtocol(asyncio.DatagramProtocol):
            def __init__(self, collector):
                self.collector = collector
            
            def datagram_received(self, data, addr):
                try:
                    message = data.decode('utf-8', errors='replace').strip()
                    
                    # Emit kernel message
                    self.collector.emit('console.data', {
                        'id': 'boot:netconsole',
                        'payload': {
                            'message': message,
                            'source': 'netconsole',
                            'from': f"{addr[0]}:{addr[1]}"
                        }
                    })
                except Exception as e:
                    print(f"Netconsole parse error: {e}")
        
        # Create UDP listener
        loop = asyncio.get_running_loop()
        transport, protocol = await loop.create_datagram_endpoint(
            lambda: NetconsoleProtocol(self),
            local_addr=('0.0.0.0', self.port)
        )
        
        print(f"✓ Netconsole listening on UDP port {self.port}")
        
        # Emit resource
        self.emit('resource.create', {
            'id': 'boot:netconsole',
            'payload': {
                'port': self.port,
                'state': 'listening'
            },
            'meta': {
                'component': 'console.v1',
                'version': 1
            }
        })
```

## Phase 4: Complete Integration

Update main daemon to start all boot collectors:

**File**: `manager/tinycore_manager/main.py`

```python
#!/usr/bin/env python3
"""
TinyCore Manager - Main daemon entrypoint.
"""

import asyncio
import argparse
import signal
import sys

# Import collectors
from tinycore_manager.collectors.boot_collector import BootCollector
from tinycore_manager.collectors.pty_collector import PTYCollector
from tinycore_manager.collectors.serial_collector import SerialCollector
from tinycore_manager.collectors.netconsole_collector import NetconsoleCollector


class TinyCoreManager:
    """Main manager daemon."""
    
    def __init__(self, config: dict):
        self.config = config
        self.collectors = {}
        self.running = False
    
    def emit_event(self, event_type: str, data: dict):
        """Central event emission (routes to transports)."""
        # TODO: Send to resource registry and transports
        print(f"EVENT: {event_type} - {data.get('id', 'unknown')}")
    
    async def start(self):
        """Start all collectors and transports."""
        self.running = True
        print("=" * 80)
        print("TinyCore UI Manager Starting")
        print("=" * 80)
        
        tasks = []
        
        # Start boot collector (capture early logs)
        if 'boot' in self.config.get('collectors', []):
            boot = BootCollector(emit_callback=self.emit_event)
            self.collectors['boot'] = boot
            tasks.append(boot.capture_all())
            print("✓ Boot collector initialized")
        
        # Start PTY collector (terminals)
        if 'pty' in self.config.get('collectors', []):
            pty = PTYCollector(emit_callback=self.emit_event)
            self.collectors['pty'] = pty
            print("✓ PTY collector initialized")
        
        # Start serial console collector (optional)
        if 'serial' in self.config.get('collectors', []):
            serial = SerialCollector(emit_callback=self.emit_event)
            self.collectors['serial'] = serial
            tasks.append(serial.start())
            print("✓ Serial collector initialized")
        
        # Start netconsole collector (optional)
        if 'netconsole' in self.config.get('collectors', []):
            netconsole = NetconsoleCollector(
                port=self.config.get('netconsole_port', 6666),
                emit_callback=self.emit_event
            )
            self.collectors['netconsole'] = netconsole
            tasks.append(netconsole.start())
            print("✓ Netconsole collector initialized")
        
        print("=" * 80)
        print(f"✓ Manager ready - Listening on {self.config.get('listen', '0.0.0.0:8080')}")
        print("=" * 80)
        
        # Run all collector tasks
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        
        # Keep running
        while self.running:
            await asyncio.sleep(1)
    
    def stop(self):
        """Stop all collectors."""
        print("\n\nShutting down...")
        self.running = False
        
        for name, collector in self.collectors.items():
            if hasattr(collector, 'stop'):
                collector.stop()


def main():
    parser = argparse.ArgumentParser(description='TinyCore UI Manager')
    parser.add_argument('command', choices=['daemon', 'capture'], 
                       help='Command to run')
    parser.add_argument('--config', default='/etc/tinycore-manager/config.json',
                       help='Config file path')
    parser.add_argument('--source', help='Capture source (for capture command)')
    
    args = parser.parse_args()
    
    if args.command == 'daemon':
        # Load config
        import json
        try:
            with open(args.config, 'r') as f:
                config = json.load(f)
        except FileNotFoundError:
            config = {
                'listen': '0.0.0.0:8080',
                'collectors': ['boot', 'pty']
            }
        
        # Create manager
        manager = TinyCoreManager(config)
        
        # Handle signals
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, manager.stop)
        
        # Run
        try:
            loop.run_until_complete(manager.start())
        except KeyboardInterrupt:
            pass
        finally:
            loop.close()
    
    elif args.command == 'capture':
        # One-shot capture (called from bootlocal.sh)
        async def capture():
            boot = BootCollector(emit_callback=lambda *args: None)
            if args.source == 'kernel-ring-buffer':
                await boot.capture_kernel_log()
        
        asyncio.run(capture())


if __name__ == '__main__':
    main()
```

## Phase 5: Web UI Integration

Update your web UI to display boot logs:

```javascript
// In test_pty_viewer_xterm.html or new boot viewer

ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    
    if (msg.type === 'resource.create' && msg.id === 'boot:kernel-log') {
        // Display kernel boot log
        const lines = msg.payload.lines;
        term.writeln('\x1b[33m=== Kernel Boot Log ===\x1b[0m');
        lines.forEach(line => term.writeln(line));
    }
    
    if (msg.type === 'boot.message') {
        // Real-time boot message
        term.writeln(`\x1b[36m[BOOT]\x1b[0m ${msg.payload.message}`);
    }
    
    if (msg.type === 'terminal.data') {
        // Regular terminal output
        term.write(msg.payload.chunk);
    }
};
```

## Testing

1. **Install the extension:**
```bash
cd /tmp/tinycore-manager
sudo mksquashfs . tinycore-manager.tcz
sudo cp tinycore-manager.tcz /mnt/sda1/tce/optional/
echo "tinycore-manager.tcz" >> /mnt/sda1/tce/onboot.lst
```

2. **Reboot and verify:**
```bash
sudo reboot
```

3. **Check logs:**
```bash
tail -f /var/log/tinycore-manager.log
```

4. **View in browser:**
Open `http://your-ip:8000/test_pty_viewer_xterm.html`

You should see:
- Kernel boot messages
- Hardware info
- Real-time system logs
- Terminal sessions

## Next Steps

- [ ] Add framebuffer capture for graphical boot splash
- [ ] Implement replay/recording of boot sequences
- [ ] Add boot performance metrics (time to service startup)
- [ ] Create dedicated boot log viewer UI component
- [ ] Integrate with systemd journal (if migrating from busybox init)

You now have complete visibility from kernel boot through user space! 🚀
