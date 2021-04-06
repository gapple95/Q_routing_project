import packet

class Node:
    s = 0
    def __init__(self, x, y, _id):
        self.x = x
        self.y = y
        self._id = _id
        self.queue = list()

    def receive(self, _packet):
        self.queue.append(_packet)

