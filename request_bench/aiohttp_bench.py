from aiohttp import web
import aiohttp
from request_bench.fetch_async import fetch

routes = web.RouteTableDef()


@routes.get("/request")
async def request_test(request):
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return web.Response(text=resp)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
