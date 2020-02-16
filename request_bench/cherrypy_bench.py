import cherrypy
import requests
from request_bench.fetch_sync import fetch


class HelloWorld:
    @cherrypy.expose
    def request(self):
        session = requests.session()
        resp = fetch(session)
        return resp


cherrypy.quickstart(HelloWorld())
