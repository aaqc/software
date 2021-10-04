#!/usr/bin/python
import aiohttp
import asyncio


async def get_url(url:str):
    url = f"https://api.aaqc.svaren.dev/{url}"
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            if resp.content_type == "text/plain":
                return await resp.text()
            else:
                return await resp.json()
    except:
        return {"status" : "error"}
    

async def ping():
    res = await get_url("ping")
    return True if res == "pong" else False




async def main():
    print(await ping())    
    
asyncio.run(main())