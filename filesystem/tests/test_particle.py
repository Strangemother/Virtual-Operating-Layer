import unittest
import fs
from unittest import mock

class TestParticle(unittest.TestCase):

    #@mock.patch('fs.Space.write')
    def test_byte_particle_enter_open_true(self):
        """Ensure enure flips boolean 'on'
        """
        bp = fs.Particle()
        with bp:
            self.assertEqual(bp.open, True)
        self.assertEqual(bp.open, False)


    @mock.patch('fs.Particle.write1')
    def test_particle_write_write1(self, write1):
        """Call to write with 4byte chunk calls write1
        """
        bp = fs.Particle()
        bp.write('thisfourpartdata', byte_chunk=4)
        self.assertEqual(write1.call_count, 4)

        write1.reset_mock()
        bp.write('thisfourpartdata', byte_chunk=8)
        self.assertEqual(write1.call_count, 2)
