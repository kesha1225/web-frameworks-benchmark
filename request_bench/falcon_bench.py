import falcon
import requests
from request_bench.fetch_sync import fetch


class Resource:
    def on_get(self, req, resp):
        session = requests.session()
        resp = fetch(session)
        resp.body = resp


app = falcon.API()
app.add_route("/request", Resource())
