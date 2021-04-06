class Packet:
    def __init__(self, time_stamp, _source, _destination, _prev, _next):
        self.time_stamp = time_stamp
        self.sourceAddr = _source
        self.destinationAddr = _destination