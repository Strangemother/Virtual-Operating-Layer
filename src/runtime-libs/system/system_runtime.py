""""The system class defines the master header for class importing on
the terinal root:

    > system.foo

"""
from bios import puts

class BlackListException(Exception):

    def __init__(self, name, errors):
        message = 'Blacklist name "{}"'.format(name)
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.errors = errors


class DiscoveryExecutor:
    """A utility to find executable comands for the layer 0 teminal.
    """
    def find(self, name):
        """Given a string return an executable"""
        puts('DiscoveryExecutor::find "{}"'.format(name), level=2)

        if name in self.blacklist:
            raise BlackListException(name)
            return



class System(DiscoveryExecutor):

    def __init__(self, scope=None):
        self._scope = scope
        self.blacklist = ()

    def __getattr__(self, key):
        return key

    def __getitem__(self, key):
        if key == 'self':
            return self

        if key == 'foo':
            return self._scope

        if hasattr(self, key):
            return getattr(self, key)
        return "< %s" % key

    def __import__(self, *a, **kw):
        return "import"

    def foo(self):
        return 'bar'
