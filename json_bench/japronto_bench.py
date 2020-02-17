from japronto import Application


def test_json(request):
    return request.Response(json={"hello": "world"})


app = Application()
app.router.add_route('/json', test_json)
app.run()
