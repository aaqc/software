#!/usr/bin/python
import asyncio
from websocket_aaqc import Websocket

async def main():
    server = Websocket("wss://api.aaqc.svaren.dev/gateway")
    
    response = await server.send_message(server, {"type":"ping"}, nonce = "alve_svaren")
    print(response)

    while True:
        pass


if __name__ == "__main__":
    asyncio.run(main())
    