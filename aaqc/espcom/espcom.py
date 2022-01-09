from serial import Serial


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


if __name__ == "__main__":
    EspCom()
