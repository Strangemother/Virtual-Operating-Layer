# TinyCore Boot Integration - Quick Reference

## Boot Capture Flow

```
BIOS → Bootloader → Kernel → Init → Services → Desktop
  ↓         ↓          ↓       ↓        ↓         ↓
Serial   Console    dmesg   Script  Syslog    GUI
         redirect            hooks
```

## Integration Points (in boot order)

### 1. BIOS/Firmware (Optional - Hardware dependent)
**Capture via:** Serial port, IPMI/BMC for servers  
**Access:** Hardware-specific, usually serial console at 115200 baud

### 2. Bootloader (ISOLINUX/GRUB)
**File:** `/mnt/sda1/boot/isolinux/isolinux.cfg`  
**Add to kernel line:**
```
console=tty0 console=ttyS0,115200n8 loglevel=7
```
- `console=tty0` - Keep local display working
- `console=ttyS0` - Also output to serial port
- `loglevel=7` - Maximum kernel verbosity

### 3. Kernel Boot Messages
**Capture immediately after boot:**
```bash
dmesg > /tmp/kernel-boot.log
```
**Real-time monitoring:**
```bash
dmesg --follow
```

### 4. Init System Hook
**File:** `/opt/bootlocal.sh` (runs early, before services)  
**Add:**
```bash
# Start your UI manager daemon first
/usr/local/bin/tinycore-manager daemon &

# Send it the boot logs
dmesg | /usr/local/bin/tinycore-manager capture
```

**Make persistent:**
```bash
echo "/opt/bootlocal.sh" >> /opt/.filetool.lst
filetool.sh -b
```

### 5. Service Logs
**Capture from:** `/var/log/messages` or `/var/log/syslog`  
**Monitor real-time:**
```bash
tail -f /var/log/messages
```

### 6. TTY/Console Sessions
**Replace getty with your capture tool:**
```
# /etc/inittab
tty1::respawn:/usr/local/bin/your-getty-wrapper /dev/tty1
```

## Data Sources Summary

| Source | Location | What It Contains |
|--------|----------|------------------|
| Kernel ring buffer | `dmesg` | Hardware init, driver messages, kernel errors |
| System log | `/var/log/messages` | Service startups, daemon messages |
| Serial console | `/dev/ttyS0` | Real-time kernel + bootloader output |
| Boot parameters | `/proc/cmdline` | Kernel boot options used |
| Hardware info | `/proc/cpuinfo`, `/proc/meminfo` | CPU, RAM, devices |
| Network console | UDP port 6666 | Remote kernel messages (if configured) |

## Minimal Setup (3 Steps)

### Step 1: Add Manager to Boot
```bash
# /opt/bootlocal.sh
/usr/local/bin/tinycore-manager daemon &
```

### Step 2: Capture Kernel Log
```bash
# After daemon starts
dmesg | /usr/local/bin/tinycore-manager capture
```

### Step 3: Make Persistent
```bash
echo "/opt/bootlocal.sh" >> /opt/.filetool.lst
filetool.sh -b
```

## Advanced: Network Boot Capture

### Enable netconsole (in bootloader config)
```
netconsole=6666@192.168.1.100/eth0,6667@192.168.1.200/
```
Sends kernel messages via UDP to `192.168.1.200:6667`

### Receive on remote machine
```bash
# Listen for kernel messages
nc -u -l 6667
```

Or integrate into your manager daemon as UDP listener.

## Event Flow in Your UI Manager

```
Boot Stage          → Collector           → Resource Event
─────────────────────────────────────────────────────────
Bootloader output   → Serial Collector    → boot:console
Kernel messages     → dmesg reader        → boot:kernel-log  
Hardware detection  → /proc parser        → boot:hardware
Service startup     → syslog tail         → boot:syslog
User login          → PTY Collector       → terminal:tty-*
```

## File Locations Reference

```
/opt/bootlocal.sh              Run commands at boot (before services)
/opt/bootsync.sh               Run commands at boot (parallel with services)
/opt/.filetool.lst             List of files to persist across reboots
/mnt/sda1/tce/                 Extensions directory
/mnt/sda1/boot/isolinux/       Bootloader config
/var/log/messages              System log (if syslog running)
/proc/cmdline                  Kernel boot parameters
/dev/ttyS0                     Serial port (usually COM1)
```

## Testing Your Integration

```bash
# 1. Check if manager is running
ps aux | grep tinycore-manager

# 2. View captured kernel log
cat /tmp/kernel-boot.log

# 3. Monitor real-time
dmesg --follow

# 4. Check network connectivity
curl http://localhost:8080/status

# 5. Test WebSocket from browser
# Open: http://your-ip:8000/test_pty_viewer_xterm.html
```

## Troubleshooting Quick Reference

| Problem | Check | Solution |
|---------|-------|----------|
| No boot logs | `/opt/bootlocal.sh` not running | Make it executable: `chmod +x` |
| Serial empty | Wrong port | Try `/dev/ttyS1`, check BIOS |
| Manager not starting | Missing dependencies | Check Python, websockets installed |
| Can't connect to WebSocket | Firewall | Open port 8080 |
| Logs truncated | `dmesg` buffer full | Increase `log_buf_len=1M` in kernel params |

## Next Steps Checklist

- [ ] Add manager to `/opt/bootlocal.sh`
- [ ] Test boot capture with `dmesg`
- [ ] Configure serial console (optional)
- [ ] Set up network console (optional)
- [ ] Create web UI viewer for boot logs
- [ ] Add real-time log streaming
- [ ] Implement boot performance metrics
