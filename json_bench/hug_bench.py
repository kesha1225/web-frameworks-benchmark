import hug


@hug.get("/json")
def test_json():
    return {"hello": "world"}


#  hug -f hug_bench.py
