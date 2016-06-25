import unittest
from lib.plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_0_defaults(self):
        """Plane initially flying"""
        self.assertFalse(self.plane.at_airport)

    def test_1a_lands(self):
        """Plane at airport after landing"""
        self.plane.land()
        self.assertTrue(self.plane.at_airport)

    def test_2a_take_off(self):
        """Plane not at airport after takeing off"""
        self.plane.land()
        self.plane.take_off()
        self.assertFalse(self.plane.at_airport)
