#!/usr/bin/python
import aiohttp
import asyncio
from os import path
import json


def get_drone_id():
    if path.isfile("drone_info.json"):
        try:
            f = open("drone_info.json")
            data = json.load(f)
            if "drone_id" in data:
                drone_id = data["drone_id"]
                if len(drone_id) != 0:
                    return drone_id
                else:
                    print("Failed to read drone_info.json, 'drone_id' cannot be empty")
                    return None
            else:
                print("Failed to read drone_info.json, 'drone_id' dosen't exist")
            return None
        except Exception as e:
            print(f"Failed to read drone_info.json\n, Error: {e}")
            return None
    else:
        print("You need to register a drone, before runing the software.")
    return None


def register_drone(drone_id: str):
    try:
        f = open("drone_info.json", "w")
        drone_info_json = {"drone_id": drone_id}
        json.dump(drone_info_json, f)
        f.close()
    except Exception as e:
        print(f"Failed to register a drone\n")
        return None


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


def get_gps_coords():
    return (0, 0)


if __name__ == "__main__":

    async def main():
        print(await ping())

    asyncio.run(main())
