import flask
import requests
from request_bench.fetch_sync import fetch

app = flask.Flask(__name__)


@app.route("/request")
def test_request():
    session = requests.session()
    resp = fetch(session)
    return resp
