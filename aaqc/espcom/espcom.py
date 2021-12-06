from serial import Serial

# ESP
BOP = b"\xAA"
EOP = b"\x55"


class EspCom:
    def __init__(self, port: str = "/dev/ttyACM0", rate: int = 115200):
        try:
            self.bus = Serial(port, rate)
        except Exception as err:
            raise Exception(f'Could not open serial port "{port}"\n{err}')

    def __exit__(self):
        self.bus.close()

    def send_packet(self, packet: bytearray):
        self.bus.write(packet)

    # Read a packet from the serial bus and return it as a bytearray
    def read_packet(self):
        while True:
            byte = self.bus.read()
            if byte == BOP:
                packet = self.bus.read(self.bus.in_waiting)
                if packet[-1] == EOP:
                    return packet
                else:
                    return None


if __name__ == "__main__":
    EspCom()
