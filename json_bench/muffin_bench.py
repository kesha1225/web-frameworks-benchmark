import muffin

app = muffin.Application("web")


@app.register("/json")
def test_json(request):
    return {"hello": "world"}


muffin.run_app(app)
