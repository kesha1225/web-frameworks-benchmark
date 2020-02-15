import falcon
import json


class Resource:
    def on_get(self, req, resp):
        resp.body = json.dumps({"hello": "world"})


app = falcon.API()
app.add_route('/json', Resource())
