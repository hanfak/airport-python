import unittest
from lib.airport import Airport
from lib.plane import Plane

class TestUserStory(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Plane()

    def test_user_story_1(self):
        # As an air traffic controller
        # So I can get passengers to a destination
        # I want to instruct a plane to land at an airport and confirm that it has landed
        self.airport.instruct_to_land(self.plane)
        self.assertIn(self.plane, self.airport.planes)
        self.assertTrue(self.plane.is_at_airport())

    def test_user_story_2(self):
        # As an air traffic controller
        # So I can get passengers on the way to their destination
        # I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport
        self.airport.instruct_to_land(self.plane)
        self.airport.instruct_take_off(self.plane)
        self.assertNotIn(self.plane, self.airport.planes)
        self.assertFalse(self.plane.is_at_airport())
