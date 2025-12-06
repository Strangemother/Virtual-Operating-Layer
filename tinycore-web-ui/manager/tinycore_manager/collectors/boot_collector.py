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
