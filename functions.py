#!/usr/bin/python
import aiohttp
import asyncio
from os import _exit, path
import json


def get_drone_id():
    if path.isfile("drone_info.json"):
        try:
            f = open("drone_info.json")
            data = json.load(f)
            if "drone_id" in data:
                drone_id = data["drone_id"]
                return drone_id
            else:
                print(
                    "Failed to read file, 'drone_id' dosen't exist in drone_info.json"
                )
            _exit(0)
        except Exception as e:
            print(f"Failed to read drone_info.json\n, Error: {e}")
            _exit(0)
    else:
        print("You need to register a drone, before runing the software.")
        _exit(0)


async def get_url(url: str):
    url = f"https://api.aaqc.svaren.dev/{url}"
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            if resp.content_type == "text/plain":
                return await resp.text()
            else:
                return await resp.json()
    except:
        return {"status": "error"}


async def ping():
    res = await get_url("ping")
    return True if res == "pong" else False


if __name__ == "__main__":

    async def main():
        print(await ping())

    asyncio.run(main())
