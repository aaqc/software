#!/usr/bin/python
import asyncio
from websocket_aaqc import Websocket


async def main():
    server = Websocket("wss://api.aaqc.svaren.dev/gateway")

    for x in range(0, 100):
        response = await server.send_message(
            server, {"type": "ping"}, nonce="alve_svaren"
        )
        print(response)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
