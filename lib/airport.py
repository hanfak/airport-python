class Airport(object):
    def __init__(self):
        self.planes = []
        self.capacity = 20

    def instruct_to_land(self, plane):
        if len(self.planes) == self.capacity:
            raise Exception('Airport is full: Take off plane')
        if plane in self.planes:
            raise Exception('Plane already at airport')
        plane.land()
        self.planes.append(plane)

    def instruct_take_off(self, plane):
        if plane not in self.planes:
            raise Exception("Plane not at airport: land plane first")
        plane.take_off()
        self.planes.remove(plane)
