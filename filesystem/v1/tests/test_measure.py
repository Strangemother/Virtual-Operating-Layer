import unittest
import fs
from unittest import mock
from measure import Size

class TestSize(unittest.TestCase):

    #@mock.patch('fs.Space.write')
    def test_gb_setter(self):
        s = Size()
        s.gb = 1
        assert s.gb == 1
        assert s._gb == 1
