import unittest
from mock import MagicMock
from lib.airport import Airport

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = MagicMock()
        self.weather = MagicMock()
        self.weather.is_stormy = MagicMock(return_value=False)

    def test_0_defaults(self):
        """airport is empty"""
        self.assertEqual(self.airport.planes, [])

    def test_0a_defaults(self):
        """airport has default capacity"""
        self.assertEqual(self.airport.capacity, 20)

    def test_0b_defaults(self):
        """airport can change capacity"""
        self.airport = Airport(5)
        self.assertEqual(self.airport.capacity, 5)

    def test_1a_instruct_to_land(self):
        """plane in airport after landing"""
        self.airport.instruct_to_land(self.plane, self.weather)
        number_of_planes = self.airport.planes
        self.assertEqual(1, len(number_of_planes))

    def test_1b_instruct_to_land(self):
        """aiport hanger filled with one plane"""
        self.airport.instruct_to_land(self.plane, self.weather)
        self.assertIn(self.plane, self.airport.planes)

    def test_1c_instruct_to_land(self):
        """aiport instruct_to_land calls land on plane"""
        self.airport.instruct_to_land(self.plane, self.weather)
        self.plane.land.assert_called_with()

    def test_1d_instruct_to_land(self):
        """plane cannot land if already in airport"""
        self.airport.instruct_to_land(self.plane, self.weather)
        with self.assertRaisesRegexp(Exception, 'Plane already at airport'):
            self.airport.instruct_to_land(self.plane, self.weather)

    def test_1e_instruct_to_land(self):
        """plane cannot land if airport is full"""
        for number in range(1,21):
            self.diff_plane = MagicMock()
            self.airport.instruct_to_land(self.diff_plane, self.weather)
        with self.assertRaisesRegexp(Exception, 'Airport is full: Take off plane'):
            self.airport.instruct_to_land(self.plane, self.weather)

    def test_1f_instruct_to_land(self):
        """plane cannot land if stormy weather"""
        self.weather.is_stormy = MagicMock(return_value=True)
        with self.assertRaisesRegexp(Exception, 'Plane cannot land: weather is stormy'):
            self.airport.instruct_to_land(self.plane, self.weather)

    def test_2a_instruct_take_off(self):
        """plane is not in airport after take off"""
        self.airport.instruct_to_land(self.plane, self.weather)
        self.airport.instruct_take_off(self.plane, self.weather)
        number_of_planes = self.airport.planes
        self.assertEqual(0, len(number_of_planes))

    def test_2b_instruct_take_off(self):
        """aiport instruct_take_off calls take_off on plane"""
        self.airport.instruct_to_land(self.plane, self.weather)
        self.airport.instruct_take_off(self.plane, self.weather)
        self.plane.take_off.assert_called_with()

    def test_2c_instruct_take_off(self):
        """plane cannot take off if not at airport"""
        with self.assertRaisesRegexp(Exception, 'Plane not at airport: land plane first'):
            self.airport.instruct_take_off(self.plane, self.weather)

    def test_2d_instruct_take_off(self):
        """plane cannot take off if stormy weather"""
        self.airport.instruct_to_land(self.plane, self.weather)
        self.weather.is_stormy = MagicMock(return_value=True)
        with self.assertRaisesRegexp(Exception, 'Plane cannot take off: weather is stormy'):
            self.airport.instruct_take_off(self.plane, self.weather)
