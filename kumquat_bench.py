from kumquat.application import Kumquat
from kumquat.response import TextResponse, JsonResponse, HTMLResponse
from kumquat.request import Request
from kumquat.response import SimpleResponse, TemplateResponse

app = Kumquat()


@app.get("/json")
async def test_json(request: Request, response: SimpleResponse):
    return {"hello": "world"}


app.run()
