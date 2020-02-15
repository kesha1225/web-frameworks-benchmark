import pycnic.core


class JSONHandler(pycnic.core.Handler):

    def get(self):
        return {"hello": "world"}


class app(pycnic.core.WSGI):
    routes = [
        ("/json", JSONHandler()),
    ]
