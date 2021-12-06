from serial import Serial


class EspCom:
    def __init__(self, port: str = "/dev/ttyACM0", rate: str = "0"):
        self.bus = Serial(port, rate)

    def __exit__(self):
        self.bus.close()

    def send_packet(self, packet: bytearray):
        self.bus.write(packet)
