from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/json")
async def json_test(request):
    return web.json_response({"hello": "world"})


app = web.Application()
app.add_routes(routes)
web.run_app(app)
