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
        """aiport instruct_to_land calls land on plane"""
        self.airport.instruct_to_land(self.plane)
        self.plane.land.assert_called_with()

    def test_2a_instruct_take_off(self):
        """plane is not in airport after take off"""
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_take_off(self.plane)
        number_of_planes = self.airport.planes
        self.assertEqual(0, len(number_of_planes))

    def test_2b_instruct_take_off(self):
        """aiport instruct_take_off calls take_off on plane"""
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_take_off(self.plane)
        self.plane.take_off.assert_called_with()

    def test_2c_instruct_take_off(self):
        """plane cannot take off if not at airport"""
        with self.assertRaisesRegexp(Exception, 'Plane not at airport: land plane first'):
            self.airport.instruct_take_off(self.plane)
