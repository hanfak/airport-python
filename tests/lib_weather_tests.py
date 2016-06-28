import unittest
from mock import MagicMock
from lib.weather import Weather

class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_1a_is_stormy(self):
        """weather is stormy"""
        self.weather.chances = MagicMock(return_value=8)
        self.assertTrue(self.weather.is_stormy())

    def test_1b_is_stormy(self):
        """weather is not stormy"""
        self.weather.chances = MagicMock(return_value=3)
        self.assertFalse(self.weather.is_stormy())
