class Plane(object):
    def __init__(self):
        self.__at_airport = False

    def land(self):
        self.__at_airport = True

    def take_off(self):
        self.__at_airport = False

    def is_at_airport(self):
        return self.__at_airport
