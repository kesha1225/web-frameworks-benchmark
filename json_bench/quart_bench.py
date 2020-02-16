from quart import Quart

app = Quart(__name__)


@app.route("/json")
async def test_json():
    return {"hello": "world"}


app.run()
