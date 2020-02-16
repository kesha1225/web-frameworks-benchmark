import requests
from request_bench.fetch_sync import fetch


def test_request(request):
    session = requests.session()
    resp = fetch(session)
    return resp
