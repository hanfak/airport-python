from random import randint

class Weather(object):
    def is_stormy(self):
        return self.chances() > 7

    def chances(self):
        return randint(0,9)
