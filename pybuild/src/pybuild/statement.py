class Statement(object):

    def __init__(self, expand=False, inactive=False, **kwargs):
        """expand: Does this statement contain many statements"""
        self.expand = expand
        self.inactive = inactive
        self.callback = kwargs.get('callback', None)
        self.__dict__.update(kwargs)

