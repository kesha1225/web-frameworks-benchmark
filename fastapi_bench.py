from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/json/")
async def test_json():
    return {"hello": "world"}

uvicorn.run(app)
