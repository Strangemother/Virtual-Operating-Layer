# TinyCore Host Manager Prototype

This directory contains the Python scaffolding for the TinyCore host manager described in `docs/host-manager.md`.

## Layout
- `tinycore_manager/config.py` – dataclasses and CLI parsing.
- `tinycore_manager/registry.py` – in-memory resource registry + diff helpers.
- `tinycore_manager/collectors/` – pluggable collectors (metrics, PTY, stubs).
- `tinycore_manager/transports/` – transports such as WebSocket control plane.
- `tinycore_manager/main.py` – CLI entrypoint that wires everything together.

## Development
```bash
cd manager
python -m tinycore_manager.main --dry-run
```

This command validates the config, instantiates the registry and transport stubs, and exits. Future milestones will add long-running asyncio services and real collectors.
