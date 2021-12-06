from aaqc.espcom.packet import *
from aaqc.software.connection import *
from aaqc.software.utils import get_gps_coords


class DroneFlight:
    def __init__(self):
        print("Init sensorer")
        compose_packet("sensor_init", [])

        print("Open websocket")
        self.connection = Websocket()

    def __gps__(self):
        self.gps_coordinates = get_gps_coords()
        return self.gps_coordinates

    def save_gps(self):
        print("Save gps")
        self.gps_coordinates = get_gps_coords()

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
