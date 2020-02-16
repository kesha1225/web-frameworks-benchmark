import hug
import requests
from request_bench.fetch_sync import fetch


@hug.get("/request")
def test_request():
    session = requests.session()
    resp = fetch(session)
    return resp


#  hug -f hug_bench.py
