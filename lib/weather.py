from random import randint

class Weather(object):
    def is_stormy(self):
        return randint(0,9) > 7
