## container:

    An interface driver for connecting a vol to a display interface - sent to the container


## sequence:

The first system procedure

https://github.com/Strangemother/Virtual-Operating-Layer/blob/master/v1/docs/os-runtime.md


### POST (KERNEL)

After the blank repl is loaded, the `sequence` manages all initial apps until the user space.

loaded from a kernel config for proc order.
+ ram V
+ proc allocator
+ Permission layer
+ HOST manager
+ deployment.yaml
+ pre image
+ init config
+ Step to first phase

Configuration is a mixure of HOST CLI arguments, bios, deployment, 'burnt-in' (ram cache), init config.
