import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"hello": "world"})


def make_app():
    return tornado.web.Application([
        (r"/json/", MainHandler),
    ])


app = make_app()
app.listen(8000)
tornado.ioloop.IOLoop.current().start()
