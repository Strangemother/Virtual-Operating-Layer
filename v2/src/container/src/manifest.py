"""Load a manifest
"""

import yaml

def load(filename):
    with open(filename) as stream:
        return yaml.load(stream)
