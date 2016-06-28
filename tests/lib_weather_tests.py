import unittest
import random
from lib.weather import Weather

class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_1a_is_stormy(self):
        """weather is stormy"""
        random.seed( 2 )
        self.assertTrue(self.weather.is_stormy())

    def test_1b_is_stormy(self):
        """weather is not stormy"""
        random.seed( 9 )
        self.assertFalse(self.weather.is_stormy())
