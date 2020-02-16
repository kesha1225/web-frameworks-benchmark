import pycnic.core
import requests
from request_bench.fetch_sync import fetch


class JSONHandler(pycnic.core.Handler):
    def get(self):
        session = requests.session()
        resp = fetch(session)
        return resp


class app(pycnic.core.WSGI):
    routes = [
        ("/request", JSONHandler()),
    ]
