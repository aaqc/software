#!/usr/bin/python
from asyncio.tasks import sleep
import sys, json
import asyncio
import websockets

#Server address
#ws://localhost:8000/gateway

class Websocket():
    async def __aenter__(self, uri:str = 'ws://localhost:8000/gateway'):
        self._conn = websockets.connect( uri )
        self.websocket = await self._conn.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()

    async def close(self):
        await self.websocket.close()

async def send_message(server, json_message:dict, nonce:str):
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


async def main():
    server = Websocket()
    response = await send_message(server, {"type":"ping"}, nonce = "1200lol")
    print(response)
        
if __name__ == "__main__":
    asyncio.run(main())