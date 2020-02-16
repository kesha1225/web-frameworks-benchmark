import bottle
import requests
from request_bench.fetch_sync import fetch

app = bottle.Bottle()


@app.route("/request")
def request_test():
    session = requests.session()
    resp = fetch(session)
    return resp


app.run()
