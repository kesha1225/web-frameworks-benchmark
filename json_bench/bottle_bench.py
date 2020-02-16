import bottle

app = bottle.Bottle()


@app.route("/json")
def test_json():
    return {"hello": "world"}


app.run()
