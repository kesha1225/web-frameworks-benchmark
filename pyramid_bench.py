from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(renderer='json')
def test_json(request):
    return {"hello": "world"}


with Configurator() as config:
    config.add_route('test_json', '/json/')
    config.add_view(test_json, route_name='test_json', renderer='json')
    app = config.make_wsgi_app()
server = make_server('127.0.0.1', 8000, app)
server.serve_forever()
