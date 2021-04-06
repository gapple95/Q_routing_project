class Packet:
    def __init__(self, time_stamp, _sourceAddr, _destinationAddr):
        self.time_stamp = time_stamp
        self.sourceAddr = _sourceAddr
        self.destinationAddr = _destinationAddr