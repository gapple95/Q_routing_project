class Packet:
    def __init__(self, time_stamp, _source, _destination, _next):
        self.time_stamp = time_stamp
        self.source = _source
        self.destination = _destination
        self.next = _next
