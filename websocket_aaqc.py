#!/usr/bin/python
from asyncio.tasks import sleep
import sys, json, asyncio, websockets, json
from time import sleep


# Server address
uri = "wss://api.aaqc.svaren.dev/gateway"


class Websocket:
    def __init__(self, uri, drone_id):
        self.uri = uri
        self.drone_id = drone_id
        dots = "*" * len(drone_id) * 3
        print(
            f"{dots}\nStarting websocket listenr\nURI: {uri}\nDrone ID: {drone_id}\n{dots}\n"
        )

    async def listener(self):
        try:
            print(await self.websocket.recv())
        except:
            print("Cant listen, retrying...")

    async def __aenter__(self):
        self._conn = websockets.connect(
            uri if uri != None else "wss://api.aaqc.svaren.dev/gateway"
        )
        self.websocket = await self._conn.__aenter__()
        asyncio.ensure_future(self.listener())
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()

    async def close(self):
        sleep(1)
        await self._conn.__aexit__(*sys.exc_info())

    async def send_message(self, server, json_message: dict, nonce: str):
        json_message["nonce"] = nonce
        async with server as echo:
            await echo.send(json.dumps(json_message))
            while True:
                response = await echo.receive()
                response = json.loads(response)
                try:
                    if response["type"] != "auth" and response["nonce"] == nonce:
                        return response
                except Exception as e:
                    return {"error": e}
