from fastapi import FastAPI
import uvicorn
import aiohttp
from request_bench.fetch_async import fetch

app = FastAPI()


@app.get("/request")
async def test_request():
    session = aiohttp.ClientSession()
    resp = await fetch(session)
    return resp


uvicorn.run(app)
