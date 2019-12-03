# Entry point to the post loader, running os management before user repl.
# Ran after a blank bios.

# + ram V
# + config manager.
# + proc allocator
# + permissions
# + HOST manager
# + deployment.yaml
# + pre image
# + init config
# + Step to first phase

class KernelConfig(object):

    def update(self, config):
        self.__dict__.update(config)

    def __getattr__(self, key):
        return self.__dict__.get(key)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


KC = KernelConfig()


def allocate():
    """First function for post(). Allocate and natural resources
    for the kernel procedure to run. This runs independent from the
    post as it configures the hardware space.
    """
    pass


def kernel_config(given_config):
    """return the configuration for the kernel post sequence,
    mixing and storing the given parameters.
    """
    KC.update(given_config)
    return KC


def post(given_config):
    """Called from the initiator, the post() function starts the allocation
    procedure and initial tests for the kernel procedure
    """
    allocate()
    kconfig = kernel_config(given_config)
    start_proc_allocator(kconfig)


def start_proc_allocator(config):
    """Start the main system resourcer for and IO base bus."""
    # proc allocator
    # persmissins system
    # host maanfer
    # deploy config
    pass
