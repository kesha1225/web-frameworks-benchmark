import requests


def fetch(session: requests.session):
    resp = session.get("http://google.com")
    return resp.text
