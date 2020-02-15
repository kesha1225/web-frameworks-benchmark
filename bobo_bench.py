import bobo


@bobo.query('/json', content_type='application/json')
def test_json():
    return {"hello": "world"}


app = bobo.Application(bobo_resources=__name__)
