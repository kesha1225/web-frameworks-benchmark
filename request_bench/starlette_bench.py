from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import uvicorn
import aiohttp
from request_bench.fetch_async import fetch


async def request_test(request):
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return PlainTextResponse(resp)


app = Starlette(routes=[Route("/request", request_test),])

uvicorn.run(app)
