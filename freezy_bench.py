from freezy import router
from freezy.request import Request
from freezy.response import Response
import json
import uvicorn

router = router.Router()


@router.route("/json/")
async def test_json(request: Request):
    return Response(json.dumps({"hello": "world"}).encode(),
                    content_type=b"application/json")


uvicorn.run(router)
