The manifest exists in the VOL container `home/` accessible by the HOST, SYSTEM, VOL and Container as a whole. It fundamentally drives the configurations of the VOL container. Any patial settings may exist in here.

Consider it like a master-boot or init settings for the container - initially set by default and overridden after boot.

The manifest is available as read-only during runtime.

## Keys

### Name

The name field provides a friendly name ID to use across all applications.
