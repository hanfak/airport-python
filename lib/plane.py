class Plane(object):
    def __init__(self):
        self.at_airport = False

    def land(self):
        self.at_airport = True

    def take_off(self):
        self.at_airport = False

    def is_at_airport(self):
        return self.at_airport
