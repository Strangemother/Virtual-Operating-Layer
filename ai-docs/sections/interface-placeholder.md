---
Status: Draft
Last-Touched: 2025-09-12
Source: restructured-notes-2025.md
---
# Interface & Display Layer

Summary:
- Display Layer Purpose: Presents render strings (and broader visual content) from one or multiple VOL instances via a container with local service decoding inbound stream(s). (Source: [display (container).md](../../docs/display%20(container).md))
- Occipital Cortex Analogy: Visual pipeline conceptualized as topological view of interior information streamed into container-rendered contexts. (Source: [display (container).md](../../docs/display%20(container).md))
- Container Role: Mounted display driver receiving streams or single-shot render commands; central pipeline enables multiplexed visual output from many VOLs into unified rendering contexts. (Source: [display (container).md](../../docs/display%20(container).md))
- Layering Chain: HOST → VOL → DRIVER → CONTAINER → RENDER sequence where container offloads graphics from VOL and can host multiple sources. (Source: [display (container).md](../../docs/display%20(container).md))
- Rendering Context Types: Text, Vector (turtle style), Pixel (canvas), GL (OpenGL/WebGL) plus potential offload panels for host-native rendering (DirectX, DirectShow). (Source: [display (container).md](../../docs/display%20(container).md))
- Offload Rendering Panels: External host windows integrated via transparent portal overlays; container manages lifecycle while delegating draw to host-driven engines. (Source: [display (container).md](../../docs/display%20(container).md))
- Extended Container Capabilities: May bridge audio, hardware inputs, software (RPC/session) feedback beyond pure visual output. (Source: [display (container).md](../../docs/display%20(container).md))
- Layer Acquisition: Apps obtain ID-assigned draw/display layers through RPC pipeline; ownership allows direct content placement per layer. (Source: [display (container).md](../../docs/display%20(container).md))
- Base Layer Facilities: System-styled text with design submission + streaming; vector base for SVG-like live drawing; pixel canvas for mid-tier graphics; full GL for 2D/3D environment with primitives, lighting, animation. (Source: [display (container).md](../../docs/display%20(container).md))
- Input Distribution: Inputs (HID, host drivers, GPIO) flow from container or runtime nodes into mesh; translator adapts input/output data to container format. (Source: [inputs.md](../../docs/inputs.md))
- Input Agnosticism: Devices anywhere in mesh can supply input resources shared without distinction; nodes may lack inputs (pure computational or display). (Source: [inputs.md](../../docs/inputs.md))
- Facade Purpose: Remaps underlying C/Python functions into VOL-specific contextual objects; abstracts logical steps for runtime, file access, mesh state propagation. (Source: [Facade.md](../../docs/Facade.md))
- Files API Facade: Provides structured exposure (root → transport (ftp) → directories → file) simplifying complex path resolution. (Source: [Facade.md](../../docs/Facade.md))
- Mesh State Propagation: State interface changes broadcast across pre-authorised network; facade may mediate local to remote object change communications. (Source: [Facade.md](../../docs/Facade.md))
- Branding Name: “Celestia Blue” chosen to evoke openness/connectivity; retains VOL descriptor; future OS form under its own kernel. (Source: [name.md](../../docs/branding/name.md))
- Colour Coding Scheme: Color states (black, blue, red, green, white, yellow, pink) designate privacy, ownership, power mode, openness, or TBD semantics; only descriptors provided—operational bindings unspecified. (Source: [colour-coding.md](../../docs/branding/colour-coding.md))

Incomplete: Container stream protocol
Needed:
- Message/frame format for multi-VOL multiplex
- Ordering & synchronization guarantees across layer IDs
Candidate Sources: [display (container).md](../../docs/display%20(container).md)

Incomplete: Layer ID lifecycle
Needed:
- Allocation / release procedure
- Conflict resolution when two apps request same layer type
Candidate Sources: [display (container).md](../../docs/display%20(container).md)

Incomplete: Offload panel integration rules
Needed:
- Event focus & input routing between transparent host window and container layers
- Z-index / stacking policy with overlay video or external engine
Candidate Sources: [display (container).md](../../docs/display%20(container).md), [inputs.md](../../docs/inputs.md)

Incomplete: Translator specification (inputs)
Needed:
- Minimal translator API (receive, normalize, dispatch)
- Latency / buffering strategy for high-frequency inputs
Candidate Sources: [inputs.md](../../docs/inputs.md)

Incomplete: Facade mapping registry
Needed:
- Storage of exposed symbol map (e.g., bios.puts → put)
- Collision handling for duplicate function names
Candidate Sources: [Facade.md](../../docs/Facade.md)

Incomplete: Mesh state facade semantics
Needed:
- Consistency model (eventual vs immediate) for propagated state
- Conflict reconciliation when concurrent changes occur
Candidate Sources: [Facade.md](../../docs/Facade.md), [inputs.md](../../docs/inputs.md)

Incomplete: Branding color operational binding
Needed:
- What each color state concretely toggles (permissions, modes)
- Transition rules and authorization requirements
Candidate Sources: [colour-coding.md](../../docs/branding/colour-coding.md), [name.md](../../docs/branding/name.md)

Incomplete: 3D layer capability boundaries
Needed:
- Guaranteed primitive/shader baseline vs optional features
- Performance constraints for multiplexed GL contexts
Candidate Sources: [display (container).md](../../docs/display%20(container).md)

Verbatim scope: Extracted strictly from cited interface documents (display layer, inputs, facade, branding).
