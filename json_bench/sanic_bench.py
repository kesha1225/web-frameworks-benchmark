from sanic import Sanic
from sanic.response import json

app = Sanic(name="testapp")


@app.route("/json")
async def test_json(request):
    return json({"hello": "world"})


app.run()
