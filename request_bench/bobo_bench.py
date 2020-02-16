import bobo
import requests
from request_bench.fetch_sync import fetch


@bobo.query("/request", content_type="text/plain")
def request_test():
    session = requests.session()
    resp = fetch(session)
    return resp


app = bobo.Application(bobo_resources=__name__)
