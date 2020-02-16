import aiohttp


async def fetch(session: aiohttp.ClientSession):
    async with session.get("http://google.com") as resp:
        return await resp.text()
