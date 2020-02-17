from japronto import Application
import aiohttp


async def fetch(session_: aiohttp.ClientSession):
    async with session_.get("http://google.com") as resp:
        resp = await resp.text()
        await session_.close()
        return resp


async def test_request(request):
    session = aiohttp.ClientSession()
    return request.Response(text=await fetch(session))


app = Application()
app.router.add_route('/request', test_request)
app.run()
