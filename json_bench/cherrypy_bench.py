import cherrypy


class HelloWorld:
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self):
        return {"hello": "world"}


cherrypy.quickstart(HelloWorld())
