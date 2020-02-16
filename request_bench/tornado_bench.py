import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        resp = await client.fetch("http://www.google.com")
        self.write(resp)


def make_app():
    return tornado.web.Application([(r"/request", MainHandler),])


app = make_app()
app.listen(8000)
tornado.ioloop.IOLoop.current().start()
