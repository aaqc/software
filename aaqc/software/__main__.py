#!/usr/bin/python
import asyncio
from .connection import Websocket
from .utils import get_drone_id, register_drone
from .flight import DroneFlight
from os import _exit


async def main(drone_id):
    try:
        server = Websocket("wss://api.aaqc.svaren.dev/gateway", drone_id)
        response = await server.send_message(
            server, {"type": "ping"}, nonce="alve_svaren"
        )
        print(response)
    except Exception as e:
        print(e)
        _exit(0)


if __name__ == "__main__":
    drone_id = get_drone_id()
    if drone_id == None:
        drone_id = str(input("Enter drone_id: "))
        register_drone(drone_id)
        drone_id = get_drone_id()
    loop = asyncio.get_event_loop()
    loop.create_task(main(drone_id=drone_id))
    loop.run_forever()
