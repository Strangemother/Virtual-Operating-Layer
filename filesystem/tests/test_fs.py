import unittest
import fs
from unittest import mock

class TestFileSystem(unittest.TestCase):

    @mock.patch('fs.Space.write')
    def test_through(self, space_write):
        """General goal throughput - unloaded agglomerate calls to a space write
        """
        REFERENCE = 'pointername'
        expected = 'there is no spoon.'
        fs.agglomerate(REFERENCE, expected)
        space_write.assert_called_with(expected)

    @mock.patch('fs.Space.get_id', return_value=2020)
    @mock.patch('fs.local.HeaderReference.add', return_value=mock.Mock())
    def test_get_id(self, header_ref__add, space_get_id):
        """Calling agglomerate will execute the get_id once.
        """
        # Ensure the get_id function is called.
        REFERENCE = 'pointername'
        expected = 'there is no spoon'
        fs.agglomerate(REFERENCE, expected)
        space_get_id.assert_called_once()

        # Ensure the add function was walled with the given id.
        header_ref__add.assert_called_once()
        #('particle', None, 2020)
        call = header_ref__add.mock_calls[0]
        last_attr = call[1][2]
        self.assertEqual(last_attr, 2020)
