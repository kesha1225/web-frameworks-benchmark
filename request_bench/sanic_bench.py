from sanic import Sanic
import aiohttp
from request_bench.fetch_async import fetch

app = Sanic(name="testapp")


@app.route("/request")
async def test_request(request):
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return resp


app.run()
