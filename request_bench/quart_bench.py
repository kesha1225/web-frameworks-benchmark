from quart import Quart
import aiohttp
from request_bench.fetch_async import fetch

app = Quart(__name__)


@app.route("/request")
async def test_request():
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return resp


app.run()
