from utils import get_drone_info
from connection import Websocket

all_errors = []


def error_handeling(error):
    all_errors.append(str(error))


class DroneFlight:
    def __init__(self):
        print("\n--------- Starting Drone ---------\n")

        # --------------- Init Drone Token ----------------
        try:
            self.drone_token = get_drone_info("token")
            print(f"Success - Init Drone Token: {self.drone_token}")
        except Exception as e:
            print(f"Failed - Init Drone Token")
            error_handeling(e)

        # ------------- Connect to Websocket --------------
        try:
            Websocket(drone_token=self.drone_token)
            print("Success - Init Websocket")
        except Exception as e:
            print("Failed - Init Websocket")
            error_handeling(e)

        # ------------- Connect to TCP footage -------------
        print("Success - Init TCP (Video)")

        # --------------- Init sensors ---------------------
        print("Success - Init sensor - All sensors\n")

        if all_errors != None:
            for error in all_errors:
                print(error)

    def begin(self):
        # Start motors and init path
        print("Begin flight")

    def new_path(self):
        # Add new path
        print("Add new flight path")

    def force_stop(self):
        # Force stop drone
        print("Force stop")

    def land(self):
        # Land
        print("Landing")

    def take_off(self):
        # Take off
        print("Take off")

    def end(self):
        # Stop motos and save flight path
        print("End flight")
        print("")


if __name__ == "__main__":
    DroneFlight()
