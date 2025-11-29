# Wayland Bridge Collector Pattern

## Overview
The Wayland bridge collector enables unmodified GUI applications to run as managed resources within the TinyCore UI. It acts as a lightweight Wayland compositor, capturing window surfaces from client applications and streaming them as video/canvas data to the web UI.

## Architecture

```
┌─────────────────────────────────────┐
│  GUI Apps (Firefox, GIMP, etc)     │
│  - Wayland client protocol          │
│  - Renders to wl_surface buffers    │
└─────────────┬───────────────────────┘
              │ Wayland protocol (Unix socket)
┌─────────────▼───────────────────────┐
│  Minimal Wayland Compositor         │
│  - wl_compositor, wl_shell          │
│  - DMA-BUF / SHM buffer import      │
│  - Per-window surface tracking      │
└─────────────┬───────────────────────┘
              │ Surface buffers
┌─────────────▼───────────────────────┐
│  Wayland Collector                  │
│  - Surface-to-resource mapping      │
│  - Frame capture (via DMA-BUF)      │
│  - Encoder pipeline (H264/VP9)      │
│  - Input routing (pointer/kbd)      │
└─────────────┬───────────────────────┘
              │ Resource events + streams
┌─────────────▼───────────────────────┐
│  Resource Registry + Stream Coord.  │
│  - Creates window:* resources       │
│  - Negotiates WebRTC/canvas stream  │
└─────────────┬───────────────────────┘
              │ Control + media
┌─────────────▼───────────────────────┐
│  Transport Layer                    │
│  - Control: WebSocket (metadata)    │
│  - Media: WebRTC DataChannel/SRTP   │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│  Web UI                             │
│  - <canvas> or <video> per window   │
│  - Pointer/keyboard event capture   │
└─────────────────────────────────────┘
```

## Design Principles

### Compositor Philosophy
Unlike traditional compositors (Weston, KWin), the Wayland bridge is **stateless** and **presentation-agnostic**:
- No window decorations—UI draws those in HTML/CSS
- No internal layout engine—web UI handles positioning
- No local rendering—all buffers are captured and streamed

The compositor's sole job is to:
1. Accept Wayland client connections
2. Import surface buffers (DMA-BUF or SHM)
3. Forward buffer updates to the collector
4. Route input events back to focused clients

### Buffer Handling Strategies

#### A. Zero-Copy (DMA-BUF + Hardware Encoding)
Best for performance-critical apps (video players, games):
```
GPU Memory
┌─────────────────┐
│ Client Buffer   │ (EGL/Vulkan surface)
└────────┬────────┘
         │ DMA-BUF FD passed via wl_linux_dmabuf
┌────────▼────────┐
│ Compositor      │ (imports DMA-BUF)
└────────┬────────┘
         │ FD + metadata
┌────────▼────────┐
│ H264 Encoder    │ (VA-API/NVENC reads GPU buffer directly)
└────────┬────────┘
         │ Encoded frames
┌────────▼────────┐
│ WebRTC Pipeline │
└─────────────────┘
```

Pros: No CPU copies, low latency
Cons: Requires GPU with VA-API/NVENC support

#### B. Shared Memory + Software Encoding
Fallback for CPU-rendered apps:
```
┌─────────────────┐
│ Client Buffer   │ (Cairo software surface)
└────────┬────────┘
         │ wl_shm pool
┌────────▼────────┐
│ Compositor      │ (memcpy to staging buffer)
└────────┬────────┘
         │ Raw pixels
┌────────▼────────┐
│ libx264/libvpx  │ (software encoding)
└────────┬────────┘
         │ Encoded frames
┌────────▼────────┐
│ WebRTC Pipeline │
└─────────────────┘
```

Pros: Works everywhere
Cons: Higher CPU usage, potential latency

#### C. Canvas Streaming (Low-Bandwidth)
For static/infrequent updates (text editors, terminals with GUI):
```
┌────────────────┐
│ Client Buffer  │
└────────┬───────┘
         │ wl_surface.commit
┌────────▼───────┐
│ Compositor     │ (damage tracking)
└────────┬───────┘
         │ Only changed regions
┌────────▼───────┐
│ PNG/WebP Enc.  │ (lossless compression)
└────────┬───────┘
         │ Image data
┌────────▼───────┐
│ WebSocket      │ (control channel)
└────────┬───────┘
         │
┌────────▼───────┐
│ Canvas2D/WebGL │ (browser composites)
└────────────────┘
```

Pros: Ultra-low bandwidth for static content
Cons: Not suitable for animation/video

## Event Flow

### 1. Window Creation
Wayland client creates surface:
```wayland
wl_compositor.create_surface() → wl_surface
xdg_wm_base.get_xdg_surface() → xdg_surface
xdg_surface.get_toplevel() → xdg_toplevel
xdg_toplevel.set_title("My App")
wl_surface.commit()
```

Compositor notifies collector → emits resource:
```json
{
  "type": "resource.create",
  "id": "window:wl-firefox-1a2b",
  "payload": {
    "title": "Mozilla Firefox",
    "appId": "firefox",
    "geometry": { "width": 1280, "height": 720 },
    "state": "active",
    "capabilities": ["resize", "move", "close"]
  },
  "meta": {
    "component": "window.v1",
    "version": 1
  }
}
```

### 2. Buffer Attachment & Streaming
Client attaches buffer:
```wayland
wl_surface.attach(buffer, 0, 0)
wl_surface.damage(0, 0, 1280, 720)
wl_surface.commit()
```

Collector initiates stream:
```json
{
  "type": "stream.start",
  "id": "stream:window:wl-firefox-1a2b",
  "payload": {
    "resource": "window:wl-firefox-1a2b",
    "media": {
      "kind": "video",
      "codec": "H264",
      "profile": "baseline",
      "width": 1280,
      "height": 720,
      "fps": 30
    },
    "transport": {
      "kind": "webrtc",
      "offer": "v=0\r\no=- ..."
    }
  }
}
```

Web UI responds with SDP answer, establishes WebRTC connection, begins receiving frames.

### 3. Damage Tracking & Adaptive Encoding
Compositor tracks damaged regions per frame:
```c
struct surface_damage {
    int32_t x, y, width, height;
};
```

Collector adapts encoding:
- **Full damage** (entire surface): Encode as I-frame
- **Partial damage** (e.g., text cursor): Encode as P-frame with motion vectors
- **No damage**: Skip frame (send keep-alive)

Quality tuning:
- Monitor WebRTC stats (packet loss, RTT)
- Adjust bitrate dynamically (500 kbps → 5 Mbps)
- Switch codecs if bandwidth changes (H264 ↔ VP9)

### 4. Input Handling
Web UI captures pointer event:
```json
{
  "type": "event.input",
  "target": "window:wl-firefox-1a2b",
  "payload": {
    "kind": "pointer",
    "event": "motion",
    "x": 640,
    "y": 360,
    "buttons": 0,
    "timestamp": 1700304000123
  }
}
```

Collector translates to Wayland:
```wayland
wl_pointer.enter(surface, x, y)
wl_pointer.motion(time, x, y)
```

Client receives event, updates cursor, re-renders → new buffer → stream update.

### 5. Window State Changes
UI emits geometry change:
```json
{
  "type": "event.input",
  "target": "window:wl-firefox-1a2b",
  "payload": {
    "kind": "resize",
    "geometry": { "width": 1920, "height": 1080 }
  }
}
```

Collector sends Wayland configure:
```wayland
xdg_toplevel.configure(1920, 1080, [])
```

Client resizes, commits new buffer → collector updates stream resolution:
```json
{
  "type": "resource.patch",
  "id": "window:wl-firefox-1a2b",
  "payload": [
    { "op": "replace", "path": "/geometry/width", "value": 1920 },
    { "op": "replace", "path": "/geometry/height", "value": 1080 }
  ]
}
```

Encoder pipeline reconfigures for new dimensions.

### 6. Window Destruction
Client destroys surface:
```wayland
xdg_toplevel.destroy()
wl_surface.destroy()
```

Collector stops stream and deletes resource:
```json
{
  "type": "stream.stop",
  "id": "stream:window:wl-firefox-1a2b",
  "meta": { "reason": "surface_destroyed" }
}
```
```json
{
  "type": "resource.delete",
  "id": "window:wl-firefox-1a2b",
  "meta": { "reason": "closed" }
}
```

## Implementation Stack

### Compositor Foundation
**Option A: wlroots** (Recommended)
- C library with batteries-included (input, output, protocols)
- Used by Sway, Wayfire—battle-tested
- Provides: `wlr_compositor`, `wlr_xdg_shell`, `wlr_dmabuf`

**Option B: libwayland + custom protocols**
- More control, higher complexity
- Implement `wl_compositor`, `xdg_shell`, `linux_dmabuf` from scratch

### Video Encoding
- **VA-API** (Intel/AMD): `libva`, `gstreamer-vaapi`
- **NVENC** (NVIDIA): FFmpeg with `--enable-nvenc`
- **Software**: `libx264`, `libvpx` (VP9)

### WebRTC Integration
- **libdatachannel** (C++): Lightweight RTC stack
- **Pion** (Go): If building in Go
- **aiortc** (Python): Async Python implementation
- **GStreamer WebRTC**: Full pipeline integration

### Language Choices
- **Nim + wlroots**: Best performance, can bind C libraries directly
- **C/C++**: Maximum control, verbose
- **Rust + smithay**: Memory-safe compositor toolkit (newer, smaller ecosystem)
- **Python + PyWayland**: Prototyping only (too slow for production)

## Performance Optimizations

### 1. Frame Pacing
Don't encode faster than display refresh:
```nim
const TARGET_FPS = 60
const FRAME_TIME_US = 1_000_000 div TARGET_FPS

while running:
  let start = getMonoTime()
  captureAndEncode()
  let elapsed = (getMonoTime() - start).inMicroseconds
  if elapsed < FRAME_TIME_US:
    sleep((FRAME_TIME_US - elapsed) div 1000)
```

### 2. Encoder Presets
Balance quality vs. latency:
- **ultrafast**: <1ms encode, lower quality (for game streaming)
- **medium**: ~5ms encode, good quality (default)
- **slow**: 10-20ms encode, best quality (video playback)

### 3. Regional Encoding
For multi-window scenarios, encode only visible/damaged windows:
```python
for window in windows:
    if window.is_occluded():
        continue  # Skip fully hidden windows
    if not window.has_damage():
        continue  # No changes since last frame
    encode_window(window)
```

### 4. Adaptive Bitrate
Monitor transport stats:
```python
if packet_loss > 5%:
    bitrate *= 0.8  # Reduce by 20%
elif buffer_fill < 30%:
    bitrate *= 1.1  # Increase by 10%
```

## Security Considerations

### Wayland Socket Isolation
Run each GUI app in its own compositor instance with unique sockets:
```
/run/user/1000/wayland-app1
/run/user/1000/wayland-app2
```

Prevents apps from sniffing each other's input or injecting events.

### Buffer Validation
- Check buffer dimensions don't exceed limits (prevent DoS)
- Validate DMA-BUF file descriptors (ensure they're from legitimate GPU)
- Rate-limit buffer submissions

### WebRTC Authentication
- DTLS-SRTP for encrypted media streams
- TURN server with credentials for NAT traversal
- Optional: mTLS for control channel

## Integration Example

```python
# Pseudo-code showing collector integration

class WaylandCollector:
    def __init__(self, registry, stream_coordinator):
        self.registry = registry
        self.streams = stream_coordinator
        self.compositor = WlrCompositor()  # wlroots wrapper
        self.windows = {}
        
        # Hook compositor events
        self.compositor.on('surface_create', self.on_surface_create)
        self.compositor.on('surface_commit', self.on_surface_commit)
        self.compositor.on('surface_destroy', self.on_surface_destroy)
    
    def on_surface_create(self, surface):
        resource_id = f"window:wl-{surface.id}"
        
        # Register resource
        self.registry.create(resource_id, {
            'title': surface.title,
            'geometry': {'width': surface.width, 'height': surface.height}
        }, component='window.v1')
        
        # Create encoder + WebRTC sender
        stream = self.streams.create_video_stream(
            resource_id,
            codec='H264',
            resolution=(surface.width, surface.height)
        )
        
        self.windows[resource_id] = {
            'surface': surface,
            'stream': stream,
            'encoder': H264Encoder(stream)
        }
    
    def on_surface_commit(self, surface):
        resource_id = f"window:wl-{surface.id}"
        window = self.windows.get(resource_id)
        if not window:
            return
        
        # Get buffer (DMA-BUF or SHM)
        buffer = surface.current_buffer()
        
        # Encode and send
        frame = window['encoder'].encode(buffer)
        window['stream'].send(frame)
    
    def on_surface_destroy(self, surface):
        resource_id = f"window:wl-{surface.id}"
        window = self.windows.pop(resource_id, None)
        if window:
            window['stream'].close()
            self.registry.delete(resource_id)
    
    def handle_input(self, event):
        """Route input from web UI to Wayland client."""
        target = event['target']
        window = self.windows.get(target)
        if not window:
            return
        
        surface = window['surface']
        payload = event['payload']
        
        if payload['kind'] == 'pointer':
            surface.send_pointer_motion(payload['x'], payload['y'])
        elif payload['kind'] == 'keyboard':
            surface.send_key(payload['key'], payload['state'])
```

## Future Enhancements
- **PipeWire integration**: Use PipeWire as buffer transport (lower overhead than custom encoding)
- **Vulkan direct scan-out**: Zero-copy path for Vulkan-native apps
- **Multi-GPU support**: Route apps to specific GPUs based on capability/load
- **Collaborative mode**: Multiple web clients view same window (screen sharing)
- **Recording/replay**: Capture Wayland protocol + buffers for debugging
