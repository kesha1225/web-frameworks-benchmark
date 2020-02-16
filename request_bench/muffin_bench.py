import muffin
import requests
from request_bench.fetch_sync import fetch

app = muffin.Application("web")


@app.register("/request")
def test_request(request):
    session = requests.session()
    resp = fetch(session)
    return resp


app.manage()
