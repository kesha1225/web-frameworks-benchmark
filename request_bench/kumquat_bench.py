from kumquat.application import Kumquat
from kumquat.request import Request
from kumquat.response import SimpleResponse
import aiohttp
from request_bench.fetch_async import fetch

app = Kumquat()


@app.get("/request")
async def test_request(request: Request, response: SimpleResponse):
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return resp


app.run()
