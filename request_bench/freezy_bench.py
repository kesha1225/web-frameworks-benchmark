from freezy import router
from freezy.request import Request
from freezy.response import Response
import json
import uvicorn
import aiohttp
from request_bench.fetch_async import fetch


router = router.Router()


@router.route("/request")
async def test_request(request: Request):
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return Response(resp, content_type=b"text/plain")


uvicorn.run(router)
