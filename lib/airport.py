class Airport(object):
    def __init__(self):
        self.planes = []

    def instruct_to_land(self, plane):
        if plane in self.planes:
            raise Exception('Plane already at airport')
        plane.land()
        self.planes.append(plane)

    def instruct_take_off(self, plane):
        if plane not in self.planes:
            raise Exception("Plane not at airport: land plane first")
        plane.take_off()
        self.planes.remove(plane)
