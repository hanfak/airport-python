import unittest
from mock import Mock
from lib.airport import Airport

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()

    def test_0_defaults(self):
        """airport is empty"""
        self.assertEqual(self.airport.planes, [])

    def test_1a_instruct_to_land(self):
        """plane in airport after landing"""
        self.airport.instruct_to_land(self.plane)
        number_of_planes = self.airport.planes
        self.assertEqual(1, len(number_of_planes))

    def test_1b_instruct_to_land(self):
        """aiport hanger filled with one plane"""
        self.airport.instruct_to_land(self.plane)
        self.assertIn(self.plane, self.airport.planes)

    def test_1c_instruct_to_land(self):
        """aiport instruct_to_land calls land on """
        self.airport.instruct_to_land(self.plane)
        self.plane.land.assert_called_with()