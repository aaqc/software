from aaqc.software.connection import Websocket
from aaqc.espcom.espcom import ESPCom
from aaqc.software.utils import get_gps_coords, get_altitude


class DroneFlight:
    def __init__(self):
        print("Init sensorer")
        compose_packet("sensor_init", [])

        print("Open websocket")
        self.connection = Websocket()
        self.serial = ESPCom()

    # -------- Drone automatic control -----------------
    def begin(self):
        compose_packet("take_off", [])
        self.connection.send("take_off")

    def land(self):
        # land the drone and stop the motors
        pass

    def end(self):
        # SEND RIDE DATA AND info that the flight is over
        pass

    # ------------ Drone manual control -----------------
    def move_forward(self, param: list):
        self.serial.send("forward", param)

    def move_backward(self, param: list):
        self.serial.send("backward", param)

    def move_right(self, param: list):
        self.serial.send("right", param)

    def move_left(self, param: list):
        self.serial.send("left", param)

    def move_up(self, param: list):
        self.serial.send("increase_altitude", param)

    def move_down(self, param: list):
        self.serial.send("decrease_altitude", param)

    def move_turn_left(self, param: list):
        self.serial.send("turn_left", param)

    def move_turn_right(self, param: list):
        self.serial.send("turn_right", param)

    def move_stop(self, param: list):
        self.serial.send("stop", param)

    # ---------- Drone INFO -----------------
    def coordinates(self):
        self.coordinates = get_gps_coords()
        return self.coordinates

    def altitude(self):
        self.altitude = get_altitude()
        return self.altitude

    def get_battery_level(self):
        try:
            self.serial.send("get_battery_level", [])
            return self.serial.receive()
        except:
            self.connection.send_message({"error": "get_battery_level"}, "error")
            self.force_land()
            raise Exception("Could not get battery level")

    # -------- Emergency commands -----------------
    def force_stop(self):
        self.serial.send("force_stop", [])

    def force_land(self):
        gps_coords = self.connection()
        current_altitude = self.altitude()

        # GOOGLE API TO GET LANDING POINT
        # CANT LAND ON WATER, TREE, ETC

        # RUN land command
