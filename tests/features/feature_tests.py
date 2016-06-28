import unittest
from mock import MagicMock
from lib.airport import Airport
from lib.plane import Plane
from lib.weather import Weather


class TestUserStory(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Plane()
        self.weather = Weather()
        self.weather.is_stormy = MagicMock(return_value=False)

    def test_user_story_1_plane_lands(self):
        # As an air traffic controller
        # So I can get passengers to a destination
        # I want to instruct a plane to land at an airport and confirm that it has landed
        self.airport.instruct_to_land(self.plane, self.weather)
        self.assertIn(self.plane, self.airport.planes)
        self.assertTrue(self.plane.is_at_airport())

    def test_user_story_2_plane_takes_off(self):
        # As an air traffic controller
        # So I can get passengers on the way to their destination
        # I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport
        self.airport.instruct_to_land(self.plane, self.weather)
        self.airport.instruct_take_off(self.plane, self.weather)
        self.assertNotIn(self.plane, self.airport.planes)
        self.assertFalse(self.plane.is_at_airport())

    def test_user_story_3_plane_lands_when_airport_empty(self):
        # As an air traffic controller
        # To ensure safety
        # I want to prevent landing when the airport is full
        for number in range(1,21):
            self.diff_plane = Plane()
            self.airport.instruct_to_land(self.diff_plane, self.weather)
        with self.assertRaisesRegexp(Exception, 'Airport is full: Take off plane'):
            self.airport.instruct_to_land(self.plane, self.weather)

    def test_user_story_4_airport_capacity_changeable(self):
        # As the system designer
        # So that the software can be used for many different airports
        # I would like a default airport capacity that can be overridden as appropriate
        self.airport = Airport(5)
        for number in range(1,6):
            self.diff_plane = Plane()
            self.weather.is_stormy = MagicMock(return_value=False)
            self.airport.instruct_to_land(self.diff_plane, self.weather)
        print self.airport.planes
        with self.assertRaisesRegexp(Exception, 'Airport is full: Take off plane'):
            self.airport.instruct_to_land(self.plane, self.weather)

    def test_user_story_5_no_take_off_when_stormy(self):
        # As an air traffic controller
        # To ensure safety
        # I want to prevent takeoff when weather is stormy
        self.airport.instruct_to_land(self.plane, self.weather)
        self.weather.is_stormy = MagicMock(return_value=True)
        with self.assertRaisesRegexp(Exception, 'Plane cannot take off: weather is stormy'):
            self.airport.instruct_take_off(self.plane, self.weather)

    def test_user_story_6_no_landing_when_stormy(self):
        # As an air traffic controller
        # To ensure safety
        # I want to prevent landing when weather is stormy
        self.weather.is_stormy = MagicMock(return_value=True)
        with self.assertRaisesRegexp(Exception, 'Plane cannot land: weather is stormy'):
            self.airport.instruct_to_land(self.plane, self.weather)
