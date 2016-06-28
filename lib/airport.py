class Airport(object):
    def __init__(self, capacity = 20):
        self.planes = []
        self.capacity = capacity

    def instruct_to_land(self, plane, weather):
        self.__check_weather_good_for_landing(weather)
        self.__check_airport_full()
        self.__check_plane_at_airport(plane)
        plane.land()
        self.planes.append(plane)

    def instruct_take_off(self, plane, weather):
        self.__check_weather_good_for_taking_off(weather)
        self.__check_plane_not_at_airport(plane)
        plane.take_off()
        self.planes.remove(plane)

    def __check_airport_full(self):
        if len(self.planes) == self.capacity:
            raise Exception('Airport is full: Take off plane')

    def __check_plane_at_airport(self, plane):
        if plane in self.planes:
            raise Exception('Plane already at airport')

    def __check_plane_not_at_airport(self, plane):
        if plane not in self.planes:
            raise Exception("Plane not at airport: land plane first")

    def __check_weather_good_for_landing(self, weather):
        if weather.is_stormy():
            raise Exception('Plane cannot land: weather is stormy')

    def __check_weather_good_for_taking_off(self, weather):
        if weather.is_stormy():
            raise Exception('Plane cannot take off: weather is stormy')
