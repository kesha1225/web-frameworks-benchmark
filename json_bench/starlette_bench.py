from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn


async def json_test(request):
    return JSONResponse({"hello": "world"})


app = Starlette(routes=[Route("/json", json_test),])

uvicorn.run(app)
