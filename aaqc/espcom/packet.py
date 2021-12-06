# from serial import Serial

class packet:
    def __init__(self, packet-size: int, opcode: int=0, data: dict={}):
        self.size = packet-size
        self.opcode = opcode
        self.data = data
