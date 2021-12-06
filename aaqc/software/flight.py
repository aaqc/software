from aaqc.espcom.packet import *
from aaqc.software.connection import *


class DroneFlight:
    def __init__(self):
        print("Init sensorer")
        compose_packet("sensor_init", [])

        print("Open websocket")
        self.connection = Websocket()

    def begin(self):
        print("Begin flight")
        compose_packet("take_off", [])
        self.connection.send("take_off")

        print("Send camera footage")

    def force_stop(self):
        print("Force stop")
        print("Stop motor")

    def land(self):
        print("Landing")

    def end(self):
        print("End flight")
        print("")
