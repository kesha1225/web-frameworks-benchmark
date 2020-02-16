from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import requests
from request_bench.fetch_sync import fetch


def test_request(request):
    session = requests.session()
    resp = fetch(session)
    return resp


with Configurator() as config:
    config.add_route("test_request", "/request")
    config.add_view(test_request, route_name="test_request")
    app = config.make_wsgi_app()
server = make_server("127.0.0.1", 8000, app)
server.serve_forever()
