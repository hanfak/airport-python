class Airport(object):
    def __init__(self):
        self.planes = []

    def instruct_to_land(self, plane):
        plane.land()
        self.planes.append(plane)

    def instruct_take_off(self,plane):
        self.planes.remove(plane)
